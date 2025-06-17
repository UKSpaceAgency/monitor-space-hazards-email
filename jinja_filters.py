from datetime import datetime
from typing import Any

jsonRegionsMap = {
  "england_nation": 'England',
  "northern_ireland_nation": "Northern Ireland",
  "scotland_nation": "Scotland",
  "wales_nation": "Wales",
  "east_of_england": "East of England",
  "east_midlands": "East Midlands",
  "london": "London",
  "north_east": "North East",
  "north_west": "North West",
  "south_east": "South East",
  "south_west": "South West",
  "west_midlands": "West Midlands",
  "yorkshire_and_north_humber": "Yorkshire and North Humber",
  "antrim_and_newtownabbey": "Antrim and Newtownabbey",
  "ards_and_north_down": "Ards and North Down",
  "armagh_city_banbridge_and_craigavon": "Armagh City, Banbridge and Craigavon",
  "belfast": "Belfast",
  "causeway_coast_and_glens": "Causeway Coast and Glens",
  "derry_and_strabane": "Derry and Strabane",
  "fermanagh_and_omagh": "Fermanagh and Omagh",
  "lisburn_and_castlereagh": "Lisburn and Castlereagh",
  "mid_and_east_antrim": "Mid and East Antrim",
  "mid_ulster": "Mid Ulster",
  "newry_mourne_and_down": "Newry, Mourne and Down",
  "central_scotland": "Central Scotland",
  "glasgow": "Glasgow",
  "highlands_and_islands": "Highlands and Islands",
  "lothian": "Lothian",
  "mid_scotland_and_fife": "Mid Scotland and Fife",
  "north_east_scotland": "North East Scotland",
  "south_scotland": "South Scotland",
  "west_scotland": "West Scotland",
  "north_wales": "North Wales",
  "mid_wales": "Mid Wales",
  "south_west_wales": "South West Wales",
  "south_east_wales": "South East Wales",
  "anguilla": "Anguilla",
  "bermuda": "Bermuda",
  "british_antarctic_territory": "British Antarctic Territory",
  "british_indian_ocean_territory": "British Indian Ocean Territory",
  "british_virgin_islands": "British Virgin Islands",
  "cayman_islands": "Cayman Islands",
  "falkland_islands": "Falkland Islands",
  "gibraltar": "Gibraltar",
  "montserrat": "Montserrat",
  "pitcairn_islands": "Pitcairn Islands",
  "saint_helena_ascension_and_tristan_da_cunha": "Saint Helena, Ascension and Tristan da Cunha",
  "south_georgia_and_the_south_sandwich_islands": "South Georgia and the South Sandwich Islands",
  "sovereign_base_areas_of_akrotiri_and_dhekelia": "Sovereign Base Areas of Akrotiri and Dhekelia",
  "turks_and_caicos_islands": "Turks and Caicos Islands",
  "isle_of_man": "Isle of Man",
  "jersey": "Jersey",
  "guernsey": "Guernsey",
  "uk_navarea": "UK NAVAREA",
  "shanwick_airspace": "Shanwick Oceanic FIR",
  "shanwick_oceanic_fir": "Shanwick Oceanic FIR",
  "london_fir": "London FIR",
  "scotland_fir": "Scotland FIR",
};

def to_affected_territories(value: dict[str, dict[str, Any]]) -> str:
    """England, Wales"""
    # return ", ".join(
    #     [k.replace("_nation", "").replace("_", " ").title() for k, v in value.items() if v["probability"] > 0.0]
    # )
    return ", ".join(
        [jsonRegionsMap[k] for k, v in value.items() if v["probability"] > 0.0]
    )
    


def to_time_frame(value: list[str | datetime]) -> str:
    """Sunday 20/09/2024 10:10:00 UTC +/- 2160 mins"""
    time_frame_start = value[0] if isinstance(value[0], datetime) else datetime.fromisoformat(value[0])
    time_frame_end = value[1] if isinstance(value[1], datetime) else datetime.fromisoformat(value[1])
    delta = (time_frame_end - time_frame_start) / 2
    return (time_frame_start + delta).strftime(
        "%A %d %B %Y at %H:%M:%S UTC +/- " + str(int(delta.total_seconds()) // 60) + " minutes"
    )


def to_risk(value: float) -> str:
    if value <= 0.01:
        return "Low"
    if value <= 0.05:
        return "Medium"
    return "High"


def to_full_country_name(value: str) -> str | None:
    country_dict = {
        "UK": "United Kingdom",
        "US": "United States",
        "JPN": "Japan",
        "PRC": "People's Republic of China",
        "CIS": "Commonwealth of Independent States",
        "ALG": "Algeria",
        "ARGN": "Argentina",
        "AC": "Asia Satellite Telecommunications Company",
        "AUS": "Australia",
        "AZER": "Azerbaijan",
        "BGD": "Bangladesh",
        "BELA": "Belarus",
        "BOL": "Bolivia",
        "BRAZ": "Brazil",
        "BGR": "Bulgaria",
        "CA": "Canada",
        "CHLE": "Chile",
        "CHBZ": "China/Brazil",
        "CZCH": "Czech Republic (Former Czechoslovakia)",
        "CZ": "Czechia",
        "DEN": "Denmark",
        "ECU": "Ecuador",
        "EGYP": "Egypt",
        "EST": "Estonia",
        "EUME": "European Organisation for the Exploitation of Meteorological Satellites",
        "ESA": "European Space Agency",
        "EUTE": "European Telecommunications Satellite Organization",
        "FR": "France",
        "FGER": "France/Germany",
        "FRIT": "France/Italy",
        "GER": "Germany",
        "GLOB": "Globalstar",
        "GREC": "Greece",
        "HUN": "Hungary",
        "IND": "India",
        "INDO": "Indonesia",
        "IM": "International Mobile Satellite Organization",
        "ISS": "International Space Station",
        "ITSO": "International Telecommunications Satellite Organization",
        "IRAN": "Iran",
        "IRAK": "Iraq",
        "ISRA": "Israel",
        "IT": "Italy",
        "KAZ": "Kazakhstan",
        "KEN": "Kenya",
        "KWT": "Kuwait",
        "LAOS": "Laos",
        "LTU": "Lithuania",
        "LUXE": "Luxembourg",
        "MALA": "Malaysia",
        "MEX": "Mexico",
        "MA": "Morocco",
        "NETH": "Netherlands",
        "NICO": "New ICO",
        "NZ": "New Zealand",
        "NIG": "Nigeria",
        "NATO": "North Atlantic Treaty Organization",
        "NKOR": "North Korea",
        "NOR": "Norway",
        "O3B": "O3B Networks",
        "ORB": "ORBCOMM",
        "PAKI": "Pakistan",
        "PER": "Peru",
        "RP": "Philippines",
        "POL": "Poland",
        "POR": "Portugal",
        "QAT": "Qatar",
        "RASC": "Regional African Satellite Communications Organization",
        "RWA": "Republic of Rwanda",
        "SVN": "Republic of Slovenia",
        "TUN": "Republic of Tunisia",
        "SAUD": "Saudi Arabia",
        "SEAL": "Sea Launch",
        "SING": "Singapore",
    }
    return country_dict.get(value, None)
