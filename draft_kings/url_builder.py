BASE_URL = 'https://www.draftkings.com'
API_BASE_URL = 'https://api.draftkings.com'


class URLBuilder:
    def __init__(self, base_path: str = BASE_URL, api_base_path: str = API_BASE_URL) -> None:
        self.base_path = base_path
        self.api_base_path = api_base_path

    def build_draft_group_url(self, draft_group_id: int) -> str:
        return f"{self.api_base_path}/draftgroups/v1/{draft_group_id}"

    def build_countries_url(self) -> str:
        return f"{self.api_base_path}/addresses/v1/countries"

    def build_regions_url(self, country_code: str) -> str:
        return f"{self.api_base_path}/addresses/v1/countries/{country_code}/regions"

    def build_contests_url(self) -> str:
        return f"{self.base_path}/lobby/getcontests"

    def build_available_players_url(self) -> str:
        return f"{self.base_path}/lineup/getavailableplayers"

    def build_draftables_url(self, draft_group_id: int) -> str:
        return f"{self.api_base_path}/draftgroups/v1/draftgroups/{draft_group_id}/draftables"

    def build_game_type_rules_url(self, game_type_id: int) -> str:
        return f"{self.api_base_path}/lineups/v1/gametypes/{game_type_id}/rules"
