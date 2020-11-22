from typing import Optional, List


class Region:
    def __init__(self, code: Optional[str], country_code: Optional[str], iso_code: Optional[str],
                 name: Optional[str]) -> None:
        self.code = code
        self.country_code = country_code
        self.iso_code = iso_code
        self.name = name

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.code == other.code \
                   and self.country_code == other.country_code \
                   and self.iso_code == other.iso_code \
                   and self.name == other.name

        return False


class Regions:
    def __init__(self, regions: List[Region]) -> None:
        self.regions = regions

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.regions == other.regions

        return False
