## Calculating Municipality-Level Variables from the PSA 2020 Census of Population and Housing Reports for the Creation of Choropleth Maps

Author: Jerome Maiquez

### Rationale
PSA CPH 2020 datasets (those that are available online) are messy. In the CPH 2020 Reports, a single column houses up to multiple grouping variables and geographic hierarchies (from region, to province, down to city/municipality). This makes it extremely difficult to perform analysis on relevant socio-demographic variables on the municipality scale.

The goal of this project is to transform the PSA CPH 2020 Reports datasets, to cleanly assign relevant census variables to each city/municipality, which must be assigned to a province and a region. After joining to a municipality vector layer, the ultimate product of this project is a set of choropleth maps for various socio-demographic themes, from population, to health & education, to service access, down to housing status.

Aside from the explicitly cartographic goal of creating choropleth maps, the resulting data from this project can also be used for sectoral vulnerability analysis at the city/municipality level. For example, access to safe drinking water sources is a critical component of a community's vulnerability to water scarcity and its impacts on health and quality of life.

### Objective
1. Parse PSA 2020 CPH Reports
    - Remove blank rows in `.xlsx` files
    - Fix indent level errors in `geolocation` column
    - Assign administrative level per location based on indent level
2. Calculate relevant variables (see below)
3. ~~Join to municipality shapefile via `address`~~
    - ~~Fix errors and mismatches for province names~~
    - ~~Concatenate `province` and `municipality` names into `address`~~
    - ~~Fuzzy match `address` for data and shapefile~~
    - ~~Merge (left join) with one-to-one validation~~
3. Join to municipality shapefile via three-level fuzzy join
    - Fuzzy join regions between CPH data and shapefile
    - Do same for provinces, then city/municipality

### Project Structure
- `data_inputs/`    : Raw data (PSA CPH reports)
- `data_outputs/`   : Output (mostly `.shp` files for now)
- `notebooks/`      : For prototyping workflows
- `scripts/`        : Local package for pre-processing
- `README.md`

### Relevant Variables (all municipality level)
1. Population Characteristics
    - Population
    - Working Age Population
    - Sex Ratio
    - Age Dependency Ratio
    - Literacy Rate
    - Mean Years of Schooling
    - Overseas Workers per 1,000 People
2. Household Characteristics ___(<sup>1</sup> Target category TBD)___
    - Building Type<sup>1</sup>
    - Percent Strong Material of Roof
    - Percent Strong Material of Outer Walls
    - Percent Safe Source of Drinking Water
    - Percent Safe Source of Cooking Water
    - Percent Improved Sanitation Facility
    - Method of Garbage Disposal<sup>1</sup>
    - Fuel for Lighting<sup>1</sup>
    - Fuel for Cooking<sup>1</sup>
    - Percent Internet Access
    - Presence of Household Conveniences<sup>1</sup>
    - Percent Secure Tenure Status

### Ways Forward
- Consider: must the processing workflow be refactored into scripts?
- Re-download CPH Reports to reset previous changes
- Once processing code is modularized, calculate other variables