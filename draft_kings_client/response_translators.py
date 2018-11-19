from datetime import datetime

import pytz

from draft_kings_client.translators.date_time_translator import translate as translate_datetime


def translate_player(response):
    return {
        "id": response["pid"],
        "draft": {
            "starts_at": datetime.fromtimestamp(response["dgst"] / 1e3, tz=pytz.utc),
            "draftable": bool(response["IsDisabledFromDrafting"]) is False,
            "salary": float(response["s"]),
            "exceptional_messages": response["ExceptionalMessages"],
        },
        "first_name": response["fn"],
        "jersey_number": response["jn"],
        "last_name": response["ln"],
        "match_up": {
            "id": response["tsid"],
            "away_team_id": response["atid"],
            "home_team_id": response["htid"],
            "opposition_rank": response["or"],
        },
        "points_per_contest": float(response["ppg"]),
        "position": {
            "id": response["posid"],
            "name": response["pn"],
        },
        "team_id": response["tid"],
    }


def translate_players(response):
    return {
        "players": [translate_player(response=player) for player in response["playerList"]],
        "team_series_list": [
            translate_player_team_series_details(team_series_id=team_series_id, details=details)
            for team_series_id, details in response["teamList"].items()
        ]
    }


def translate_player_team_series_details(team_series_id, details):
    return {
        "id":  team_series_id,
        "away_team_id": details["atid"],
        "home_team_id": details["htid"],
        "starts_at": translate_datetime(formatted_datetime=details["tz"]),
        "status": details["status"],
        "weather": details["wthr"],
    }


def translate_contest(response):
    return {
        "id": response["id"],
        "double_up": True if "IsDoubleUp" in response["attr"] else False,
        "draft_group_id": response["dg"],
        "entries": {
            "maximum": response["m"],
            "fee": float(response["a"]),
            "total": response["nt"],
        },
        "fantasy_player_points": response["fpp"],
        "fifty_fifty": True if "IsFiftyfifty" in response["attr"] else False,
        "guaranteed": True if "IsGuaranteed" in response["attr"] else False,
        "head_to_head": True if "IsH2h" in response["attr"] else False,
        "name": response["n"],
        "payout": float(response["po"]),
        "sport_id": response["s"],
        "starred": True if "IsStarred" in response["attr"] else False,
        "starts_at": translate_datetime(formatted_datetime=response["sd"]),
    }


def translate_contests(response):
    return {
        "contests": [translate_contest(contest) for contest in response["Contests"]],
        "groups": [translate_draft_groups(response["DraftGroups"])],
    }


def translate_draft_groups(groups):
    return [
        {
            "id": group["DraftGroupId"],
            "series_id": group["DraftGroupSeriesId"],
            "contest_type_id": group["ContestTypeId"],
            "sport_id": group["Sport"],
            "starts_at": group["StartDate"],
            "games_count": group["GameCount"]
        }
        for group in groups
    ]


def translate_countries(response):
    return [
        {
            "id": country["countryId"],
            "code": country["countryCode"],
            "name": country["name"],
            "licensed": country["isLicensed"],
        }
        for country in response["countries"]
    ]
