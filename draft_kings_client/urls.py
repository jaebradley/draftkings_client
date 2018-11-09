BASE_URL = 'https://www.draftkings.com'
API_BASE_URL = 'https://api.draftkings.com'
GETCONTESTS_PATH = '/lobby/getcontests'
AVAILABLE_PLAYERS_PATH= '/lineup/getavailableplayers'
DRAFTGROUPS_PATH = '/draftgroups/v1/'
COUNTRIES_PATH = '/addresses/v1/countries/'
CONTESTS_PATH = '/contests/v1/contests/'

CONTESTS_URL = BASE_URL + GETCONTESTS_PATH
AVAILABLE_PLAYERS_URL = BASE_URL + AVAILABLE_PLAYERS_PATH
COUNTRIES_URL = API_BASE_URL + COUNTRIES_PATH


def draft_group_url(draft_group_id):
    return "{API_BASE_URL}{DRAFTGROUPS_PATH}{draft_group_id}".format(
        API_BASE_URL=API_BASE_URL,
        DRAFTGROUPS_PATH=DRAFTGROUPS_PATH,
        draft_group_id=draft_group_id
    )


def regions_url(country_code):
    return "{API_BASE_URL}{COUNTRIES_PATH}{country_code}/regions".format(
        API_BASE_URL=API_BASE_URL,
        COUNTRIES_PATH=COUNTRIES_PATH,
        country_code=country_code,
    )


def contest_url(contest_id):
    return "{API_BASE_URL}{CONTESTS_PATH}{contest_id}".format(
        API_BASE_URL=API_BASE_URL,
        CONTESTS_PATH=CONTESTS_PATH,
        contest_id=contest_id,
    )


def draftables_url(draft_group_id):
    return "{API_BASE_URL}{DRAFTGROUPS_PATH}draftgroups/{draft_group_id}/draftables".format(
        API_BASE_URL=API_BASE_URL,
        DRAFTGROUPS_PATH=DRAFTGROUPS_PATH,
        draft_group_id=draft_group_id
    )
