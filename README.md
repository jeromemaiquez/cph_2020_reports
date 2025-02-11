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

### Available Tables per CPH 2020 Report
##### 1. Report 2A - Demographic and Housing Characteristics

|Count|Table|
|-----|-----|
|1|**Occupied Housing Units** by City/Municipality: 1960-2020|
|2|Occupied Housing Units, Number of Households, Household Population, and **Ratio of Households and Household Population to Occupied Housing Units** by Type of Building, and City/Municipality: 2020|
|3|Occupied Housing Units by **Type of Building**, and **Number of Floors**, and City/Municipality: 2020|
|4|Occupied Housing Units by **Construction Materials of the Outer Walls and Roof**, and City/Municipality: 2020|
|5|Occupied Housing Units by **Construction Materials of the Floor** and **Finishing Materials of the Floor**, and City/Municipality: 2020|
|6|Occupied Housing Units by **Condition (State of Repair) of the Building**, **Year Built**, and City/Municipality: 2020|
|7|Occupied Housing Units by **Floor Area**, **Number of Occupants in Each Housing Unit**, and City/Municipality: 2020|
|8|Number of Households by Type of Building, **Tenure Status of the Housing Unit/Lot**, and City/Municipality: 2020|
|9|Number of Households Reporting **Land Ownership by Type of Land**, and City/Municipality: 2020|
|10|Number of Households by **Language/Dialect Generally Spoken at Home** and Province/Highly Urbanized City: 2020|
|11|Number of Households by **Place They Intend to Reside Five Years from the Time of the Census** and City/Municipality of Residence at Time of Census: 2020|

#### 2. Report 2A - Population Characteristics

|Count|Table|
|-----|-----|
|1|**Population Enumerated in Various Census** by City/Municipality: 1960 - 2020|
|2|Total Population by **Single-Year Age** and **Sex**: 2020|
|3|Total Population by **Age Group**, **Sex**, and City/Municipality: 2020|
|4|Total Population 10 Years Old and Over by Age Group, Sex, Marital Status, and City/Municipality: 2020|
|5|**Household Population** by Single-Year Age and Sex: 2020|
|6|Household Population by Age Group, Sex, and City/Municipality: 2020|
|7|Household Population 10 Years Old and Over by Age Group, Sex, Marital Status, and City/Municipality: 2020|
|8|Household Population with Registered Births by Age Group, Sex, and City/Municipality: 2020|
|9|Household Population 10 Years Old and Over by **Literacy Status**, Age Group, Sex, and City/Municipality: 2020|
|10|Household Population 5 Years Old and Over by **Highest Grade/Year Completed**, Sex, Age, and City/Municipality: 2020|
|11|Household Population 5 Years Old and Over by **Domain of Functional Difficulty**, Level of Severity, Age Group, Sex, and City/Municipality: 2020|
|12|Household Population by **Religious Affiliation** and Sex: 2020|
|13|Household Population by **Country of Citizenship** and Sex: 2020|
|14|Household Population by **Ethnicity** and Sex: 2020|
|15|Household Population 5 Years Old and Over by Sex, **Place of Present Residence**, **Residence of Mother at the Time of Birth of the Household Member**, and City/Municipality: 2020|
|16|Household Population 5 Years Old and Over by Sex, Place of Present Residence, **Place of Residence 5 Years Ago**, and City/Municipality: 2020|
|17|Overseas Workers 15 Years Old and Over by Highest Grade/Year Completed, Age Group, and Sex: 2020|
|18|Household Population by Relationship to Household Head, Household Size, and Province/Highly Urbanized City: 2020|
|19|Number of Households by Age Group and Sex of Household Head, Household Size, and City/Municipality: 2020|

#### 3. Report 2B - Demographic and Housing Characteristics

|Count|Table|
|-----|-----|
|1|Total Number of Households by City/Municipality: 2020|
|2|Households by Kind of Fuel for Lighting and City/Municipality: 2020|
|3|Households by Kind of Fuel for Cooking and City/Municipality: 2020|
|4|Households by Main Source of Water Supply for Drinking and City/Municipality: 2020|
|5|Households by Main Source of Water Supply for Cooking and City/Municipality: 2020|
|6|Households by Usual Manner of Garbage Disposal and City/Municipality: 2020|
|7|Households by Kind of Toilet Facility and City/Municipality: 2020|
|8|Households Reporting Presence of household conveniences/Information and communication technology (ICT) devices/Vehicles and City/Municipality: 2020|
|9|Households with Internet Access by City/Municipality: 2020|
|10|Households with Internet Use and Region: 2020|
|11|Households in Occupied Housing Units by Tenure Status of Housing Unit and City/Municipality: 2020|
|12|Owner-Households in Occupied Housing Units by Mode of Acquisition of Housing Unit and City/Municipality: 2020|
|13|Owner-Households Who Had Purchased Their Housing Units by Source of Financing of the Housing Unit and City/Municipality: 2020|
|14|Renter-Households in Occupied Housing Units by Monthly Rental of the Housing Unit and City/Municipality: 2020|

#### 4. Report 2B - Population Characteristics

|Count|Table|
|-----|-----|
|1|Household Population by Age Group, Sex, and City/Municipality: 2020|
|2|Household Population 5 to 24 Years Old Who Were Attending School at Anytime from June 2019 to May 2020 by Sex, and City/Municipality of Present Residence, and Place of School|
|3|Gainful Workers 15 Years Old and Over by Major Occupation Group, Age Group, Sex, and City/Municipality: 2020|
|4|Gainful Workers 15 Years Old and Over by Sex, City/Municipality of Present Residence, and Place of Work: 2020|
|5|Gainful Workers 15 Years Old and Over by Business or Industry Section, Age Group, Sex, and City/Municipality: 2020|
|6|Gainful Workers 15 Years Old and Over by Class of Worker, Age Group, Sex, and City/Municipality: 2020|
|7|Ever-Married Women Aged 15-49 Years by Age Group, Number of Children Ever Born Alive, and City/Municipality: 2020|
|8|Ever-Married Women Aged 15-49 Years by Age Group, Number of Children still Living, and City/Municipality: 2020|
|9|Ever-Married Women Aged 15-49 Years by Age Group, Number of Children Born Alive from 01 May 2019 to 30 April 2020, and City/Municipality: 2020|
|10|Ever-Married Women Aged 15-49 Years by Age Group, Age at First Marriage, and City/Municipality: 2020|

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

TEST