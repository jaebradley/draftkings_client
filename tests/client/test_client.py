import pytest

from draft_kings.client import Client


class TestClient:
    @pytest.fixture(autouse=True)
    def under_test(self) -> Client:
        return Client()

    def test_get_available_players(self, under_test: Client) -> None:
        assert under_test.available_players(draft_group_id=11513) is not None

    def test_get_draft_group_details(self, under_test: Client) -> None:
        assert under_test.draft_group_details(draft_group_id=11513) is not None

    def test_get_draftables(self, under_test: Client) -> None:
        assert under_test.draftables(draft_group_id=18186) is not None

    def test_regions(self, under_test: Client) -> None:
        assert under_test.regions("UX") is not None
