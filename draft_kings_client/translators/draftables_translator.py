from draft_kings_client.utilities import remap_keys


TEAM_KEY_MAPPING = {
    "teamId": "id",
    "teamName": "name",
    "abbreviation": "abbreviation",
    "city": "city",
}

DRAFTABLE_KEY_MAPPING = {
    "id": "draftableId",
    "player_id": "playerId",
    "position": "position",
    "roster_slot_id": "rosterSlotId",
    "salary": "salary",
    "swappable": "isSwappable",
    "disabled": "isDiabled",
    "news_status": "newsStatus",
    "team_id": "teamId",
    "team_abbreviation": "teamAbbreviation",
    "draft_alerts": "draftAlerts",
}

COMPETITION_KEY_MAPPING = {
    "id": "competitionId",
    "name": "name",
    "starts_at": "startTime",
    "sport": "sport",
    "venue": "venue",
    "starting_lineups_available": "startingLineupsAvailable",
    "depth_charts_available": "depthChartsAvailable",
    "state": "competitionState",
}


def translate_draftable(draftable):
    translated_data = remap_keys(draftable, DRAFTABLE_KEY_MAPPING)
    translated_data["name"] = remap_keys(
        draftable,
        {
            "first": "firstName",
            "last": "lastName",
            "display": "displayName",
            "short": "shortName",
        }
    )
    translated_data["image"] = remap_keys(
        draftable,
        {
            "full": "playerImageFull",
            "50": "playerImage50",
            "65": "playerImage65",
            "160": "playerImage160",
        }
    )
    translated_data["competition"] = remap_keys(
        draftable.get("competition", {}),
        {
            "id": "competitionId",
            "name": "name",
            "starts_at": "startTime",
        }
    )
    return translated_data


def translate_competition(competition):
    translated_data = remap_keys(competition, COMPETITION_KEY_MAPPING)
    translated_data["home_team"] = remap_keys(
        competition.get("home_team", {}),
        TEAM_KEY_MAPPING,
    )
    translated_data["away_team"] = remap_keys(
        competition.get("away_team", {}),
        TEAM_KEY_MAPPING,
    )
    translated_data["weather"] = remap_keys(
        competition.get("weather", {}),
        {
            "type": "icon",
            "dome": "isDome",
        }
    )
    return translated_data


def translate_draftables(response):
    return {
        "draftables": [
            translate_draftable(draftable)
            for draftable in response["draftables"]
        ],
        "competitions": [
            translate_competition(competition)
            for competition in response["competitions"]
        ]
    }