# DraftKings Python Client

## Introduction
DraftKings does not have a public API with documentation.

However, one can identify network API calls to fetch data from 
DraftKings - data like NFL contests, or players available for a 
"Draft Group" (e.g. all NBA games starting at 7 PM EST tonight), along
with relevant metadata.

## Install using PyPi
`pip install draft_kings`

## API

### Get Contests for a Sport

```python
from draftkings_client import DraftKingsClient, Sport

DraftKingsClient.get_contests(sport=Sport.nba)
```

### Get Available Players for a Draft Group

```python
from draftkings_client import DraftKingsClient

return DraftKingsClient.get_available_players(draft_group_id=1)
```

### Get Draft Group Details

```python
from draftkings_client import DraftKingsClient

return DraftKingsClient.get_draft_group_details(draft_group_id=1)
```

### Get Countries

Get all country information that DraftKings uses to make country-specific requests

```python
from draftkings_client import DraftKingsClient

return DraftKingsClient.get_countries(include_unlicensed=True)
```

### Get Regions

Get all region information for the specified country code that DraftKings uses to make region-specific requests

```python
from draftkings_client import DraftKingsClient

return DraftKingsClient.get_regions(country_code='US')
```

### Get Contest Details

```python
from draftkings_client import DraftKingsClient

return DraftKingsClient.get_contest_details(contest_id=1)
```

### Get Draftables

Get all draftable competitors

```python
from draftkings_client import DraftKingsClient

return DraftKingsClient.get_draftables(draft_group_id=1)
```
