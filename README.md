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
from draft_kings.client import contests, Sport

contests(sport=Sport.nba)
```

### Get Available Players for a Draft Group

```python
from draft_kings.client import available_players

return available_players(draft_group_id=1)
```

### Get Draft Group Details

```python
from draft_kings.client import draft_group_details

return draft_group_details(draft_group_id=1)
```

### Get Countries

Get all country information that DraftKings uses to make country-specific requests

```python
from draft_kings.client import countries

return countries()
```

### Get Regions

Get all region information for the specified country code that DraftKings uses to make region-specific requests

```python
from draft_kings.client import regions

return regions(country_code='US')
```


### Get Draftables

Get all draftable players

```python
from draft_kings.client import draftables

return draftables(draft_group_id=1)
```
