from draftkings_client.data.models.available_player_match_up import AvailablePlayerMatchUp


class AvailablePlayersTeamSeries:
    def __init__(self, team_series_id, match_up, start_timestamp, weather):
        if type(team_series_id) is not int:
            raise TypeError('team series id is not an int')

        if not isinstance(match_up, AvailablePlayerMatchUp):
            raise TypeError('match up is not valid')

        if type(start_timestamp) is not long:
            raise TypeError('start timestamp is not a long')

        if type(weather) is not str:
            raise TypeError('weather is not a string')

        self.team_series_id = team_series_id
        self.match_up = match_up
        self.start_timestamp = start_timestamp
        self.weather = weather

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))