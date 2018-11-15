from datetime import datetime

import pytz


def translate(response):
    return {
        "id": response["pid"],
        "team_id": response["tid"],
        "first_name": response["fn"],
        "last_name": response["ln"],
        "points_per_contest": float(response["ppg"]),
        "jersey_number": response["jn"],
        "draft": {
            "starts_at": datetime.fromtimestamp(response["dgst"] / 1e3, tz=pytz.utc),
            "draftable": bool(response["IsDisabledFromDrafting"]) is False,
            "salary": float(response["s"]),
            "exceptional_messages": response["ExceptionalMessages"],
        },
        "position": {
            "id": response["posid"],
            "name": response["pn"],
        },
        "match_up": {
            "id": response["tsid"],
            "home_team_id": response["htid"],
            "away_team_id": response["atid"],
            "opposition_rank": response["or"],
        },
    }

