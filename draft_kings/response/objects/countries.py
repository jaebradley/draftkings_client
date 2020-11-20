from typing import Optional, List


class Country:
    def __init__(self, country_code: Optional[str], country_id: Optional[int], is_licensed: Optional[bool],
                 name: Optional[str]) -> None:
        self.country_code = country_code
        self.country_id = country_id
        self.is_licensed = is_licensed
        self.name = name

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.country_code == other.country_code \
                and self.country_id == other.country_id \
                and self.is_licensed == other.is_licensed \
                and self.name == other.name

        return False


class Countries:
    def __init__(self, countries: List[Country]) -> None:
        self.countries = countries

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.countries == other.countries

        return False
