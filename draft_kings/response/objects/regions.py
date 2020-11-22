from typing import Optional, List


class Region:
    def __init__(self, country_code: Optional[str], iso_region_code: Optional[str], name: Optional[str],
                 region_code: Optional[str]) -> None:
        self.country_code = country_code
        self.iso_region_code = iso_region_code
        self.name = name
        self.region_code = region_code

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.country_code == other.country_code \
                and self.iso_region_code == other.iso_region_code \
                and self.name == other.name \
                and self.region_code == other.region_code

        return False


class Regions:
    def __init__(self, regions: List[Region]):
        self.regions = regions

    def __eq__(self, other):
        if type(self) is type(other):
            return self.regions == other.regions

        return False
