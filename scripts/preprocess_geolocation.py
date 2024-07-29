import pandas as pd
import geopandas as gpd
import numpy as np
from thefuzz import fuzz
from thefuzz import process as fzproc


def remove_national(df: pd.DataFrame, geoloc_col: str = "geolocation", natl_str: str = "PHILIPPINES"):
    is_national = df[geoloc_col] == natl_str
    return df[~is_national]


def assign_region(df: pd.DataFrame, geoloc_col: str = "geolocation", marker_col: str = "loc_marker", region_marker: str = "R", region_col: str = "region"):
    is_region = df[marker_col] == region_marker
    df.loc[is_region, region_col] = df.loc[is_region, geoloc_col]

    df[region_col] = df[region_col].ffill()
    return df[~is_region]


def assign_province(df: pd.DataFrame, geoloc_col: str = "geolocation", marker_col: str = "loc_marker", province_marker: str = "P", province_col: str = "province"):
    is_province = df[marker_col] == province_marker
    df.loc[is_province, province_col] = df.loc[is_province, geoloc_col]

    df[province_col] = df[province_col].ffill()
    return df[~is_province]

ncr_districts = {
    "METROPOLITAN MANILA FIRST DISTRICT": [
        "CITY OF MANILA"
    ],
    "METROPOLITAN MANILA SECOND DISTRICT": [
        "CITY OF MANDALUYONG",
        "CITY OF MARIKINA",
        "CITY OF PASIG",
        "QUEZON CITY",
        "CITY OF SAN JUAN"
    ],
    "METROPOLITAN MANILA THIRD DISTRICT": [
        "CITY OF CALOOCAN",
        "CITY OF MALABON",
        "CITY OF NAVOTAS",
        "CITY OF VALENZUELA"
    ],
    "METROPOLITAN MANILA FOURTH DISTRICT": [
        "CITY OF LAS PIÑAS",
        "CITY OF MAKATI",
        "CITY OF MUNTINLUPA",
        "CITY OF PARAÑAQUE",
        "PASAY CITY",
        "PATEROS",
        "CITY OF TAGUIG"
    ]
}

def assign_ncr_districts(df: pd.DataFrame, districts: dict = ncr_districts, geoloc_col: str = "geolocation", province_col: str = "province"):
    for district in districts:
        is_in_district = df[geoloc_col].isin(districts[district])
        df.loc[is_in_district, province_col] = district
    
    return df


def rename_interim_province(df: pd.DataFrame, province_col: str = "province", interim_str: str = "INTERIM PROVINCE 1", repl: str = "SPECIAL GEOGRAPHIC AREA"):
    is_interim = df[province_col] == interim_str
    df.loc[is_interim, province_col] = repl

    return df


def rename_city_isabela(df: pd.DataFrame, province_col: str = "province", muni_col: str = "geolocation", isabela_str: str = "CITY OF ISABELA", repl: str = "CITY OF ISABELA (NOT A PROVINCE)"):
    is_city_isabela = df[muni_col].str.contains(isabela_str)
    df.loc[is_city_isabela, province_col] = repl

    return df


def rename_provinces_with_independent_cities(df: pd.DataFrame, province_col: str = "province"):
    with_independent_city = (df[province_col].str.contains(r"^.* \(including .*\)$", regex=True)) \
                          | (df[province_col].str.contains(r"^.* \(excluding .*\)$", regex=True))

    df.loc[with_independent_city, province_col] = df.loc[with_independent_city, province_col].str.replace(r"^(.*) \(.*\)$", "\\1", regex=True)

    return df

geolocation_levels = ["region", "province", "municipality"]

def arrange_geolocation_levels(df: pd.DataFrame, col_names: list[str], geoloc_col: str = "geolocation", geoloc_levels: list[str] = geolocation_levels, marker_col: str = "loc_marker"):
    df = df.drop(columns=[marker_col]).rename(columns={geoloc_col: geoloc_levels[-1]})

    return df[geoloc_levels + ["n_households"] + col_names]