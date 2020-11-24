from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class Country:
    country_code: Optional[str]
    country_id: Optional[int]
    is_licensed: Optional[bool]
    name: Optional[str]


@dataclass(frozen=True)
class Countries:
    countries: List[Country]
