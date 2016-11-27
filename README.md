# DraftKings Python Client

## Introduction
DraftKings does not have a public API with documentation.

However, one can identify network API calls to fetch data from 
DraftKings - data like NFL contests, or players available for a 
"Draft Group" (e.g. all NBA games starting at 7 PM EST tonight), along
with relevant metadata.

Unfortunately, because these APIs are not designed for public consumption, 
the responses can be difficult to interpret. 

For example, here's example contest json:

```json
{
  "uc": 0,
  "ec": 0,
  "mec": 150,
  "fpp": 33,
  "s": 4,
  "n": "NBA $350K Bird [$350,000 Guaranteed]",
  "attr": {
    "IsGuaranteed": "true",
    "IsStarred": "true"
  },
  "nt": 864,
  "m": 12261,
  "a": 33,
  "po": 350000,
  "pd": {
    "Cash": "350000"
  },
  "tix": false,
  "sdstring": "Fri 7:00PM",
  "sd": "/Date(1478908800000)/",
  "id": 32099545,
  "tmpl": 280331,
  "pt": 1,
  "so": -99994999,
  "fwt": false,
  "isOwner": false,
  "startTimeType": 0,
  "dg": 11435,
  "ulc": 0,
  "cs": 1,
  "ssd": null,
  "dgpo": 2611098.4000,
  "cso": 4,
  "rl": false,
  "rlc": 0,
  "rll": 99999,
  "sa": true
}
```

Thus, I do some light translation for the fields that __can__ be interpreted
and return these translated objects to the user. I could not identify
the meaning of all fields, so some fields are left out.

If you see missing fields that can interpreted, please open an issue and
I will do my best to add it to the returned objects.

## Install using PyPi
`pip install draft-kings`

## API

### Get Contest for a League


## Usage

### Get Contests for a League
```python
from draftkings_client import DraftKingsClient, Sport

// Gets current NBA contests
return DraftKingsClient.get_contests(league=League.nba)
```

### Get Available Players for a Draft Group
```python
from draftkings_client import DraftKingsClient

// Gets player salary information for a draft group
// Draft group ids are returned when fetching contests
return DraftKingsClient.get_available_players(draft_group_id=1)
```

## Example Response From DraftKings

### Contests
```json
{
  "SelectedSport": 4,
  "Contests": [
    {
      "uc": 0,
      "ec": 0,
      "mec": 150,
      "fpp": 33,
      "s": 4,
      "n": "NBA $350K Bird [$350,000 Guaranteed]",
      "attr": {
        "IsGuaranteed": "true",
        "IsStarred": "true"
      },
      "nt": 864,
      "m": 12261,
      "a": 33,
      "po": 350000,
      "pd": {
        "Cash": "350000"
      },
      "tix": false,
      "sdstring": "Fri 7:00PM",
      "sd": "/Date(1478908800000)/",
      "id": 32099545,
      "tmpl": 280331,
      "pt": 1,
      "so": -99994999,
      "fwt": false,
      "isOwner": false,
      "startTimeType": 0,
      "dg": 11435,
      "ulc": 0,
      "cs": 1,
      "ssd": null,
      "dgpo": 2611098.4000,
      "cso": 4,
      "rl": false,
      "rlc": 0,
      "rll": 99999,
      "sa": true
    },
    ...
  ],
  "DraftGroups": [
    {
      "DraftGroupId": 11435,
      "ContestTypeId": 5,
      "StartDate": "2016-11-12T00:00:00.0000000Z",
      "StartDateEst": "2016-11-11T19:00:00.0000000",
      "SortOrder": 0,
      "SportSortOrder": 2,
      "Sport": "NBA",
      "GameCount": 8,
      "ContestStartTimeSuffix": null,
      "ContestStartTimeType": 0,
      "Games": null,
      "DraftGroupSeriesId": 0
    }
  ],
  "MarketingOffers": [
    "\n\n<a href=\"/offer/acceptoffer?h=3702%257c2578548996%257c1468758%257cQUp2mRIHR7u1E%252bQmiEr2gAOk0m9aVkIfodb6RMiGre8%253d\" >\n    <div class=\"marquee\">\n        <div class=\"rollover\">\n            <div class=\"rollover-inner\" >\n                <div>Introducing Leagues</div><br /><span>A new way to play with your friends!</span>\n                <span class=\"cta-link\">Learn More <span class=\"icon-chevron\"></span></span>\n            </div>\n        </div>\n        <img src=\"https://dkstatic.s3.amazonaws.com/cms-zones/335x28challenge.win.repeat.png\" />\n    </div>\n</a>\n\n",
    "\n\n<a href=\"/offer/acceptoffer?h=3820%257c2578548996%257c1468758%257c5ZdhMeizHz8QZGttM28B%252bpAF6TwE68VUO1u%252bs9AQt8E%253d\" >\n    <div class=\"marquee\">\n        <div class=\"rollover\">\n            <div class=\"rollover-inner\" >\n                <div>Missions</div><br /><span>Earn rewards and rack up frequent player points</span>\n                <span class=\"cta-link\">See your Mission now <span class=\"icon-chevron\"></span></span>\n            </div>\n        </div>\n        <img src=\"https://dkstatic.s3.amazonaws.com/cms-zones/5.25missionsrevampassets336x28marquee.png\" />\n    </div>\n</a>\n\n",
    "\n\n<a href=\"/offer/acceptoffer?h=3903%257c2578548996%257c1468758%257cHJXu0rp%252f5gIJpw5W8Z4cA5Vp2nKk0zB%252fezXJrApZXeI%253d\" >\n    <div class=\"marquee\">\n        <div class=\"rollover\">\n            <div class=\"rollover-inner\" >\n                <div>It's time to elevate</div><br /><span>Learn how to play 1-day fantasy basketball</span>\n                <span class=\"cta-link\">Learn More <span class=\"icon-chevron\"></span></span>\n            </div>\n        </div>\n        <img src=\"https://dkstatic.s3.amazonaws.com/cms-zones/howtoplaynba-marquee.png\" />\n    </div>\n</a>\n\n"
  ],
  "DirectChallengeModal": null,
  "DepositTransaction": null,
  "ShowRafLink": false,
  "ShowRafModal": false,
  "PrizeRedemptionModel": null,
  "PrizeRedemptionPop": false,
  "UseRaptorHeadToHead": false,
  "SportMenuItems": null,
  "UserGeoLocation": null,
  "ShowAds": true,
  "IsVip": null,
  "ShowAdsIgnoreLocale": true
}
```

### Available Players
```json
{
  "playerList": [
    {
      "pid": 214152,
      "pcode": 3704,
      "tsid": 5479720,
      "fn": "LeBron",
      "ln": "James",
      "fnu": "LeBron",
      "lnu": "James",
      "jn": 23,
      "pn": "SF/PF",
      "dgst": 1479254400000,
      "tid": 5,
      "htid": 5,
      "atid": 28,
      "htabbr": "Cle",
      "atabbr": "Tor",
      "posid": 27,
      "slo": null,
      "IsDisabledFromDrafting": false,
      "ExceptionalMessages": [

      ],
      "s": 10300,
      "ppg": "51.2",
      "or": 20,
      "swp": true,
      "ipc": true,
      "pp": 0,
      "i": "",
      "news": 2
    },
    ...
    ],
  "teamList": {
    "5479280": {
      "ht": "Min",
      "htid": 16,
      "at": "Cha",
      "atid": 5312,
      "tz": "/Date(1479258000000)/",
      "wthr": "",
      "dh": 0,
      "s": 4,
      "status": 1,
      "lrdy": false
    },
    "5479637": {
      "ht": "Mia",
      "htid": 14,
      "at": "Atl",
      "atid": 1,
      "tz": "/Date(1479256200000)/",
      "wthr": "",
      "dh": 0,
      "s": 4,
      "status": 1,
      "lrdy": false
    },
    "5479720": {
      "ht": "Cle",
      "htid": 5,
      "at": "Tor",
      "atid": 28,
      "tz": "/Date(1479254400000)/",
      "wthr": "dome partly-cloudy-night",
      "dh": 0,
      "s": 4,
      "status": 1,
      "lrdy": false
    },
    "5479968": {
      "ht": "Por",
      "htid": 22,
      "at": "Chi",
      "atid": 4,
      "tz": "/Date(1479265200000)/",
      "wthr": "",
      "dh": 0,
      "s": 4,
      "status": 1,
      "lrdy": false
    },
    "5480294": {
      "ht": "LAL",
      "htid": 13,
      "at": "Bkn",
      "atid": 17,
      "tz": "/Date(1479267000000)/",
      "wthr": "",
      "dh": 0,
      "s": 4,
      "status": 1,
      "lrdy": false
    }
  }
}
```