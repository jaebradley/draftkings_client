from datetime import datetime

from draft_kings_client.data.models.available_player import MatchUp


class AvailablePlayersTeamSeries:
    def __init__(self, match_up, start_timestamp, weather, status):
        if not isinstance(match_up, MatchUp):
            raise TypeError('match up is not valid')

        if type(start_timestamp) is not datetime:
            raise TypeError('start timestamp is not a datetime')

        if type(weather) is not str:
            raise TypeError('weather is not a string')

        if type(status) is not int:
            raise TypeError('status is not an int')

        self.match_up = match_up
        self.start_timestamp = start_timestamp
        self.weather = weather
        self.status = status

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