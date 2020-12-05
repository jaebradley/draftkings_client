from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class RegionDetails:
    code: Optional[str]
    country_code: Optional[str]
    iso_code: Optional[str]
    name: Optional[str]


@dataclass(frozen=True)
class RegionsDetails:
    regions: List[RegionDetails]
