## Calculating Municipality-Level Variables from the PSA 2020 Census of Population and Housing Reports

Author: Jerome Maiquez

### Rationale
Calculate relevant census variables, for potential use in sectoral vulnerability indices. For example, municipality-level rates of access to safe source of drinking water can be used as one sub-indicator of overall water access, which itself is a component of climate vulnerability in the water sector.

### Objective
1. Parse PSA 2020 CPH Reports
    - Remove blank rows in `.xlsx` files
    - Fix indent level errors in `geolocation` column
    - Assign administrative level per location based on indent level
2. Calculate relevant variables (see below)
3. Join to municipality shapefile via `address`
    - Fix errors and mismatches for province names
    - Concatenate `province` and `municipality` names into `address`
    - Fuzzy match `address` for data and shapefile
    - Merge (left join) with one-to-one validation

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