from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class Region:
    country_code: Optional[str]
    iso_region_code: Optional[str]
    name: Optional[str]
    region_code: Optional[str]


@dataclass(frozen=True)
class Regions:
    regions: List[Region]
