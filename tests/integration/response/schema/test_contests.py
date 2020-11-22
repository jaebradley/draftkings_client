import os
from unittest import TestCase

from draft_kings.response.schema.contests import ContestsSchema
from draft_kings.output.transformers.contests import ContestsDetailsResponseTransformer, ContestsResponseTransformer, transform_contest, transform_draft_group, DraftGroupsTransformer
from draft_kings.output.schema.contests import ContestsDetailsSchema
from tests.config import ROOT_DIRECTORY


class TestContestsSchemaDeserialization(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/contests/nfl/2020_10_22.json')) as data_file:
            self.schema = ContestsSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)
        transformed_data = ContestsDetailsResponseTransformer(
            ContestsResponseTransformer(transform_contest),
            DraftGroupsTransformer(transform_draft_group)
        ).transform(self.data)
        self.assertIsNotNone(transformed_data)
        schema = ContestsDetailsSchema()
        schema_output = schema.dump(transformed_data)
        self.assertIsNotNone(schema_output)
