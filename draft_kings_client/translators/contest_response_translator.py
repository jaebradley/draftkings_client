from draft_kings_client.translators.date_time_translator import translate as translate_datetime


def translate(response):
    return {
        "id": response["id"],
        "name": response["n"],
        "starts_at": translate_datetime(formatted_datetime=response["sd"]),
        "fantasy_player_points": response["fpp"],
        "sport_id": response["s"],
        "entries": {
            "maximum": response["m"],
            "fee": float(response["a"]),
            "total": response["nt"],
        },
        "payout": float(response["po"]),
        "draft_group_id": response["dg"],
        "guaranteed": True if "IsGuaranteed" in response["attr"] else False,
        "starred": True if "IsStarred" in response["attr"] else False,
        "head_to_head": True if "IsH2h" in response["attr"] else False,
        "double_up": True if "IsDoubleUp" in response["attr"] else False,
        "fifty_fifty": True if "IsFiftyfifty" in response["attr"] else False,
    }
