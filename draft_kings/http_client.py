import requests


class HTTPClient:
    def __init__(self, url_builder):
        self.url_builder = url_builder

    def countries(self):
        response = requests.get(url=self.url_builder.build_countries_url(),
                                params={'format': 'json'})

        response.raise_for_status()

        return response

    def regions(self, country_code):
        response = requests.get(url=self.url_builder.build_regions_url(country_code=country_code),
                                params={'format': 'json'})

        response.raise_for_status()

        return response

