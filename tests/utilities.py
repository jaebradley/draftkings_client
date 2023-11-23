from pathlib import Path

from tests.config import ROOT_DIRECTORY


def read_fixture(file: str) -> str:
    with open(
        Path(ROOT_DIRECTORY).joinpath(ROOT_DIRECTORY, "tests", "files", file).with_suffix(".json"),
        encoding="utf-8",
    ) as data_file:
        return data_file.read()
