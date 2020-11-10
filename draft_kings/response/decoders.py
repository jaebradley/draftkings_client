from json import JSONDecoder

from draft_kings.data import CountryData


class CountriesDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if "countries" in dct:
            return [
                CountryData(
                    data["countryId"],
                    data["countryCode"],
                    data["name"],
                    data["isLicensed"]
                ) for data in dct["countries"]
            ]

        return dct
