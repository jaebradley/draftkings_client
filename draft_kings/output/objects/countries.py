from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class CountryDetails:
    code: Optional[str]
    country_id: Optional[int]
    is_licensed: Optional[bool]
    name: Optional[str]


@dataclass(frozen=True)
class CountriesDetails:
    countries: List[CountryDetails]
