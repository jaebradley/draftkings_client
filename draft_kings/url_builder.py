class URLBuilder:
    BASE_URL = 'https://www.draftkings.com'
    API_BASE_URL = 'https://api.draftkings.com'

    @staticmethod
    def draft_groups(draft_group_id: int) -> str:
        return f"{URLBuilder.API_BASE_URL}/draftgroups/v1/{draft_group_id}"

    @staticmethod
    def countries() -> str:
        return f"{URLBuilder.API_BASE_URL}/addresses/v1/countries"

    @staticmethod
    def regions(country_code: str) -> str:
        return f"{URLBuilder.API_BASE_URL}/addresses/v1/countries/{country_code}/regions"

    @staticmethod
    def contests() -> str:
        return f"{URLBuilder.BASE_URL}/lobby/getcontests"

    @staticmethod
    def available_players() -> str:
        return f"{URLBuilder.BASE_URL}/lineup/getavailableplayers"

    @staticmethod
    def draftables(draft_group_id: int) -> str:
        return f"{URLBuilder.API_BASE_URL}/draftgroups/v1/draftgroups/{draft_group_id}/draftables"

    @staticmethod
    def game_type_rules(game_type_id: int) -> str:
        return f"{URLBuilder.API_BASE_URL}/lineups/v1/gametypes/{game_type_id}/rules"
