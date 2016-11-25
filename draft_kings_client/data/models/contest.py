from draft_kings_client.data.models.sport import Sport


class Contest:
    def __init__(self, contest_id, start_timestamp, fantasy_player_points, sport, name, is_guaranteed, is_starred,
                 is_head_to_head, is_double_up, is_fifty_fifty, total_entries, maximum_entries, entry_fee,
                 total_payout, draft_group_id):

        if type(contest_id) is not int:
            raise TypeError('contest id is not an int')

        if type(start_timestamp) is not long:
            raise TypeError('start timestamp is not an int')

        if type(fantasy_player_points) is not int:
            raise TypeError('fantasy player points is not an int')

        if not isinstance(sport, Sport):
            raise TypeError('sport is not valid')

        if type(name) is not unicode:
            raise TypeError('name is not a string')

        if type(is_guaranteed) is not bool:
            raise TypeError('is guaranteed is not a boolean')

        self.contest_id = contest_id
        self.start_timestamp = start_timestamp
        self.fantasy_player_points = fantasy_player_points
        self.sport = sport
        self.name = name
        self.is_guaranteed = is_guaranteed
        self.is_starred = is_starred
        self.is_head_to_head = is_head_to_head
        self.is_double_up = is_double_up
        self.is_fifty_fifty = is_fifty_fifty
        self.total_entries = total_entries
        self.maximum_entries = maximum_entries
        self.entry_fee = entry_fee
        self.total_payout = total_payout
        self.draft_group_id = draft_group_id
