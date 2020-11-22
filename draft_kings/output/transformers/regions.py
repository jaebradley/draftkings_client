from typing import Callable

from draft_kings.output.objects.regions import Region, Regions
from draft_kings.response.objects.regions import Region as ResponseRegion, Regions as ResponseRegions


def transform_region(response_region: ResponseRegion) -> Region:
    return Region(
        code=response_region.region_code,
        country_code=response_region.country_code,
        iso_code=response_region.iso_region_code,
        name=response_region.name
    )


class RegionsTransformer:
    def __init__(self, region_transformer: Callable[[ResponseRegion], Region]) -> None:
        self.region_transformer = region_transformer

    def transform(self, response_regions: ResponseRegions) -> Regions:
        return Regions(
            regions=list(map(lambda region: self.region_transformer(region), response_regions.regions))
        )
