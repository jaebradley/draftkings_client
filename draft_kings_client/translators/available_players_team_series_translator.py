from draft_kings_client.translators.date_time_translator import translate as translate_datetime


def translate(team_series_id, details):
    return {
        "id":  team_series_id,
        "home_team": details["htid"],
        "away_team": details["atid"],
        "starts_at": translate_datetime(formatted_datetime=details['tz']),
        "weather": details["wthr"],
        "status": details["status"],
    }