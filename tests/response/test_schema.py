import os
from unittest import TestCase

from draft_kings.response.schema import ContestsSchema
from draft_kings.output.data.transformers import ContestsDetailsResponseTransformer, ContestsResponseTransformer, transform_contest, transform_draft_group, DraftGroupsTransformer
from tests.config import ROOT_DIRECTORY


class TestContestsSchemaDeserialization(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/nfl_contests.json')) as data_file:
            self.schema = ContestsSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)
        transformed_data = ContestsDetailsResponseTransformer(
            ContestsResponseTransformer(transform_contest),
            DraftGroupsTransformer(transform_draft_group)
        ).transform(self.data)
        self.assertIsNotNone(transformed_data)
