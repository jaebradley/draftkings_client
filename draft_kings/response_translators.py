from dateutil.parser import parse as parse_datetime

from draft_kings.utilities import dig, translate_formatted_datetime, from_unix_milliseconds_to_datetime
from draft_kings.data import SPORT_ID_TO_SPORT


def translate_player(response):
    return {
        "id": dig(response, "pid"),
        "draft": {
            "starts_at": dig(response, "dgst", transformer=from_unix_milliseconds_to_datetime),
            "draftable": dig(response, "IsDisabledFromDrafting", transformer=lambda value: value is False, fallback=False),
            "salary": dig(response, "s", transformer=float),
            "exceptional_messages": dig(response, "ExceptionalMessages"),
        },
        "first_name": dig(response, "fn"),
        "jersey_number": dig(response, "jn"),
        "last_name": dig(response, "ln"),
        "match_up": {
            "id": dig(response, "tsid"),
            "away_team_id": dig(response, "atid"),
            "home_team_id": dig(response, "htid"),
            "opposition_rank": dig(response, "or"),
        },
        "points_per_contest": dig(response, "ppg", transformer=float),
        "position": {
            "id": dig(response, "posid"),
            "name": dig(response, "pn"),
        },
        "team_id": dig(response, "tid"),
    }


def translate_players(response):
    return {
        "players": [translate_player(response=player) for player in response.get("playerList", [])],
        "team_series_list": [
            translate_player_team_series_details(team_series_id=team_series_id, details=details)
            for team_series_id, details in response.get("teamList", []).items()
        ]
    }


def translate_player_team_series_details(team_series_id, details):
    return {
        "id":  int(team_series_id),
        "away_team_id": dig(details, "atid"),
        "home_team_id": dig(details, "htid"),
        "starts_at": dig(details, "tz", transformer=translate_formatted_datetime),
        "status_id": dig(details, "status"),
        "weather": dig(details, "wthr"),
    }


def translate_contest(response):
    return {
        "id": dig(response, "id"),
        "double_up": "IsDoubleUp" in response.get("attr", {}),
        "draft_group_id": dig(response, "dg"),
        "entries": {
            "maximum": dig(response, "m"),
            "fee": dig(response, "a", transformer=float),
            "total": dig(response, "nt"),
        },
        "fantasy_player_points": dig(response, "fpp"),
        "fifty_fifty": "IsFiftyFifty" in response.get("attr", {}),
        "guaranteed": "IsGuaranteed" in response.get("attr", {}),
        "head_to_head": "IsH2h" in response.get("attr", {}),
        "name": dig(response, "n"),
        "payout": dig(response, "po", transformer=float),
        "sport": SPORT_ID_TO_SPORT.get(dig(response, "s")),
        "starred": "IsStarred" in response.get("attr", {}),
        "starts_at": dig(response, "sd", transformer=translate_formatted_datetime),
    }


def translate_contests(response):
    return {
        "contests": [translate_contest(contest) for contest in response.get("Contests", [])],
        "groups": [translate_draft_groups(response.get("DraftGroups", {}))],
    }


def translate_draft_groups(groups):
    return [
        {
            "id": dig(group, "DraftGroupId"),
            "series_id": dig(group, "DraftGroupSeriesId"),
            "contest_type_id": dig(group, "ContestTypeId"),
            "sport_id": dig(group, "Sport"),
            "starts_at": dig(group, "StartDate"),
            "games_count": dig(group, "GameCount"),
        }
        for group in groups
    ]


def translate_countries(response):
    return [
        {
            "id": dig(country, "countryId"),
            "code": dig(country, "countryCode"),
            "name": dig(country, "name"),
            "licensed": dig(country, "isLicensed"),
        }
        for country in response["countries"]
    ]


def translate_leagues(leagues):
    return [
        {
            "id": dig(league, "leagueId"),
            "name": dig(league, "leagueName"),
            "abbreviation": dig(league, "leagueAbbreviation"),
        }
        for league in leagues
    ]


def translate_games(games):
    return [
        {
            "id": dig(game, "gameId"),
            "away_team_id": dig(game, "awayTeamId"),
            "home_team_id": dig(game, "homeTeamId"),
            "starts_at": dig(game, "startDate"),
            "location": dig(game, "location"),
            "sport": dig(game, "sport"),
            "status": dig(game, "status"),
            "description": dig(game, "description"),
            "home_team_score": dig(game, "sportSpecificData", "homeTeamScore"),
            "away_team_score": dig(game, "sportSpecificData", "awayTeamScore"),
            "period": dig(game, "sportSpecificData", "period"),
            "time_remaining": dig(game, "sportSpecificData", "timeRemaining"),
            "league": dig(game, "league"),
        }
        for game in games
    ]


def translate_draft_group_league(league):
    return {
        "id": dig(league, "leagueId"),
        "name": dig(league, "leagueName"),
        "abbreviation": dig(league, "leagueAbbreviation"),
    }


def translate_draft_group_game(game):
    return {
        "id": dig(game, "gameId"),
        "away_team_id": dig(game, "awayTeamId"),
        "home_team_id": dig(game, "homeTeamId"),
        "start_time": dig(game, "startDate", transformer=parse_datetime),
        "status": dig(game, "status"),
        "location": dig(game, "location"),
        "description": dig(game, "description"),
        "name": dig(game, "name")
    }


def translate_draft_group(response):
    return {
        "id": dig(response, "draftGroup", "draftGroupId"),
        "contest": {
            "type_id": dig(response, "draftGroup", "contestType", "contestTypeId"),
            "game_type": dig(response, "draftGroup", "contestType", "gameType"),
        },
        "sport": SPORT_ID_TO_SPORT.get(dig(response, "draftGroup", "sportId")),
        "start_time": {
            "type": dig(response, "draftGroup", "startTimeType"),
            "minimum": dig(response, "draftGroup", "minStartTime", transformer=parse_datetime),
            "maximum": dig(response, "draftGroup", "maxStartTime", transformer=parse_datetime),
        },
        "state": dig(response, "draftGroup", "draftGroupState"),
        "leagues": [
            translate_draft_group_league(league)
            for league in dig(response, "draftGroup", "leagues", fallback=[])
        ],
        "games": [
            translate_draft_group_game(game)
            for game in dig(response, "draftGroup", "games", fallback=[])
        ],
    }


def translate_regions(response):
    return [
        {
            "country_code": dig(region, "countryCode"),
            "code": dig(region, "regionCode"),
            "iso_code": dig(region, "isoRegionCode"),
            "name": dig(region, "name"),
        }
        for region in response["regions"]
    ]


def translate_draftable_players(draftable):
    return {
        "id": dig(draftable, "draftableId"),
        "player_id": dig(draftable, "playerId"),
        "position": dig(draftable, "position"),
        "roster_slot_id": dig(draftable, "rosterSlotId"),
        "salary": dig(draftable, "salary"),
        "swappable": dig(draftable, "isSwappable"),
        "disabled": dig(draftable, "isDisabled"),
        "news_status": dig(draftable, "newsStatus"),
        "team_id": dig(draftable, "teamId"),
        "team_abbreviation": dig(draftable, "teamAbbreviation"),
        "draft_alerts": dig(draftable, "draftAlerts"),
        "names": {
            "first": dig(draftable, "firstName"),
            "last": dig(draftable, "lastName"),
            "display": dig(draftable, "displayName"),
            "short": dig(draftable, "shortName"),
        },
        "images": {
            "full": dig(draftable, "playerImageFull"),
            "50": dig(draftable, "playerImage50"),
            "65": dig(draftable, "playerImage65"),
            "160": dig(draftable, "playerImage160"),
        },
        "competition": {
            "id": dig(draftable, "competition", "competitionId"),
            "name": dig(draftable, "competition", "name"),
            "starts_at": dig(draftable, "competition", "startTime"),
        },
    }


def translate_draftable_competition(competition):
    return {
        "id": dig(competition, "competitionId"),
        "name": dig(competition, "name"),
        "starts_at": dig(competition, "startTime"),
        "sport": SPORT_ID_TO_SPORT.get(dig(competition, "sport")),
        "venue": dig(competition, "venue"),
        "starting_lineups_available": dig(competition, "startingLineupsAvailable"),
        "depth_charts_available": dig(competition, "depthChartsAvailable"),
        "state": dig(competition, "competitionState"),
        "home_team": {
            "id": dig(competition, "homeTeam", "teamId"),
            "name": dig(competition, "homeTeam", "teamName"),
            "abbreviation": dig(competition, "homeTeam", "abbreviation"),
            "city": dig(competition, "homeTeam", "city"),
        },
        "away_team": {
            "id": dig(competition, "awayTeam", "teamId"),
            "name": dig(competition, "awayTeam", "teamName"),
            "abbreviation": dig(competition, "awayTeam", "abbreviation"),
            "city": dig(competition, "awayTeam", "city"),
        },
        "weather": {
            "type": dig(competition, "weather", "icon"),
            "dome": dig(competition, "weather", "isDome"),
        }
    }


def translate_draftables(response):
    return {
        "draftables": [
            translate_draftable_players(draftable)
            for draftable in response.get("draftables", [])
        ],
        "competitions": [
            translate_draftable_competition(competition)
            for competition in response.get("competitions", [])
        ]
    }