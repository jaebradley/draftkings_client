BASE_URL = 'https://www.draftkings.com'
API_BASE_URL = 'https://api.draftkings.com'


class URLBuilder:
    def __init__(self, base_path: str = BASE_URL, api_base_path: str = API_BASE_URL) -> None:
        self.base_path = base_path
        self.api_base_path = api_base_path

    def build_draft_group_url(self, draft_group_id: int) -> str:
        return "{API_BASE_URL}/draftgroups/v1/{draft_group_id}".format(
            API_BASE_URL=self.api_base_path,
            draft_group_id=draft_group_id
        )

    def build_countries_url(self) -> str:
        return "{API_BASE_URL}/addresses/v1/countries".format(API_BASE_URL=self.api_base_path)

    def build_regions_url(self, country_code: str) -> str:
        return "{API_BASE_URL}/addresses/v1/countries/{country_code}/regions".format(
            API_BASE_URL=self.api_base_path,
            country_code=country_code,
        )

    def build_contests_url(self) -> str:
        return "{BASE_URL}/lobby/getcontests".format(BASE_URL=self.base_path)

    def build_available_players_url(self) -> str:
        return "{BASE_URL}/lineup/getavailableplayers".format(BASE_URL=self.base_path)

    def build_draftables_url(self, draft_group_id: int) -> str:
        return "{API_BASE_URL}/draftgroups/v1/draftgroups/{draft_group_id}/draftables".format(
            API_BASE_URL=self.api_base_path,
            draft_group_id=draft_group_id
        )
