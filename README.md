# DraftKings Python Client

[![Build Status](https://travis-ci.org/jaebradley/draftkings_client.svg?branch=master)](https://travis-ci.org/jaebradley/draftkings_client)
[![codecov](https://codecov.io/gh/jaebradley/draftkings_client/branch/master/graph/badge.svg)](https://codecov.io/gh/jaebradley/draftkings_client)
![PyPI](https://img.shields.io/pypi/v/draft_kings.svg)

## Introduction
DraftKings does not have a public API with documentation.

However, one can identify network API calls to fetch data from 
DraftKings - data like NFL contests, or players available for a 
"Draft Group" (e.g. all NBA games starting at 7 PM EST tonight), along
with relevant metadata.

As DraftKings makes no guarantees about it's public API, this client makes no guarantees that existing API methods
will work consistently.

## Install using PyPi

```bash
pip install draft_kings
```

## API

### Get Contests for a Sport

```python
from draft_kings.data import Sport
from draft_kings.client import contests

contests(sport=Sport.NBA)
```

### Get Available Players for a Draft Group

```python
from draft_kings.client import available_players

available_players(draft_group_id=1)
```

### Get Draft Group Details

```python
from draft_kings.client import draft_group_details

draft_group_details(draft_group_id=1)
```

### Get Countries

Get all country information that DraftKings uses to make country-specific requests

```python
from draft_kings.client import countries

countries()
```

### Get Regions

Get all region information for the specified country code that DraftKings uses to make region-specific requests

```python
from draft_kings.client import regions

regions(country_code='US')
```


### Get Draftables

Get all draftable players

```python
from draft_kings.client import draftables

draftables(draft_group_id=1)
```
