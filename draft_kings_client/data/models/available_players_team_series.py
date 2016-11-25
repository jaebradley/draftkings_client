from draft_kings_client.data.models.available_player import AvailablePlayerMatchUp
from draft_kings_client.data.models.sport import Sport


class AvailablePlayersTeamSeries:
    def __init__(self, team_series_id, match_up, start_timestamp, weather, sport, status):
        if type(team_series_id) is not int:
            raise TypeError('team series id is not an int')

        if not isinstance(match_up, AvailablePlayerMatchUp):
            raise TypeError('match up is not valid')

        if type(start_timestamp) is not long:
            raise TypeError('start timestamp is not a long')

        if type(weather) is not unicode:
            raise TypeError('weather is not a string')

        if not isinstance(sport, Sport):
            raise TypeError('sport is not valid')

        if type(status) is not int:
            raise TypeError('status is not an int')

        self.team_series_id = team_series_id
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