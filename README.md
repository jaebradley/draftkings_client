# DraftKings Python Client

## Install using PyPi
`pip install draft-kings`

## Usage

### Get Contest for a League
```python
from draftkings_client import DraftKingsClient, League

// Gets current NBA contests
return DraftKingsClient.get_contests(league=League.nba)
```

### Get Available Players for a Draft Group
```python
from draftkings_client import DraftKingsClient

// Gets player salary information for a draft group
return DraftKingsClient.get_available_players(draft_group_id=1)
```