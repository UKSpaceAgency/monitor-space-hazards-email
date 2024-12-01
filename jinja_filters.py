from datetime import datetime
from typing import Any


def to_affected_territories(value: dict[str, dict[str, Any]]) -> str:
    """England, Wales"""
    return ", ".join(
        [k.replace("_nation", "").replace("_", " ").title() for k, v in value.items() if v["probability"] > 0.0]
    )


def to_time_frame(value: list[str | datetime]) -> str:
    """20/09/2024 10:10:00 +/- 2160 mins"""
    time_frame_start = value[0] if isinstance(value[0], datetime) else datetime.fromisoformat(value[0])
    time_frame_end = value[1] if isinstance(value[1], datetime) else datetime.fromisoformat(value[1])
    delta = (time_frame_end - time_frame_start) / 2
    return (time_frame_start + delta).strftime(
        "%A %d %B %Y at %H:%M:%S +/- " + str(int(delta.total_seconds()) // 60) + " minutes"
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
