class URLBuilder:
    BASE_URL = 'https://www.draftkings.com'
    API_BASE_URL = 'https://api.draftkings.com'

    @staticmethod
    def build_draft_group_url(draft_group_id: int) -> str:
        return f"{URLBuilder.API_BASE_URL}/draftgroups/v1/{draft_group_id}"

    @staticmethod
    def build_countries_url() -> str:
        return f"{URLBuilder.API_BASE_URL}/addresses/v1/countries"

    @staticmethod
    def build_regions_url(country_code: str) -> str:
        return f"{URLBuilder.API_BASE_URL}/addresses/v1/countries/{country_code}/regions"

    @staticmethod
    def build_contests_url() -> str:
        return f"{URLBuilder.BASE_URL}/lobby/getcontests"

    @staticmethod
    def build_available_players_url() -> str:
        return f"{URLBuilder.BASE_URL}/lineup/getavailableplayers"

    @staticmethod
    def build_draftables_url(draft_group_id: int) -> str:
        return f"{URLBuilder.API_BASE_URL}/draftgroups/v1/draftgroups/{draft_group_id}/draftables"

    @staticmethod
    def build_game_type_rules_url(game_type_id: int) -> str:
        return f"{URLBuilder.API_BASE_URL}/lineups/v1/gametypes/{game_type_id}/rules"
