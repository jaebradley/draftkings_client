# Development

## Branches

There are two branches, `v2` and `v3`, which map to the `2.0.0+` and `3.0.0+` versions, respectively. These are the defacto 
branches to branch from when developing features.

The `v2` branch (as well as the `2.0.0+` version) will be deprecated in the near-future.

`master` will reflect the latest major version branch.

## Local

There is a build script written in Bash named `build.sh` that checks if `Python 3` is installed, installs a specific version of [`Poetry`](https://python-poetry.org/).

After the `build.sh` script finishes executing, there will be instructions printed to standard output that give context
around the location of `Poetry`'s `bin` directory and how to add this directory to the `PATH` environment variable.

!!! note
    The `pyproject.toml` file is used to describe the project's requirements and relevant metadata including both the
    project's dependencies and it's development dependencies (like for generating code coverage, and this documentation 
    site)

## Testing

Unit tests are organized in the `unit` directory under the `tests` directory while integration tests are organized 
under the `integration` directory.

In the cases where tests are extensive (like integration tests for an API method), each of these tests are grouped in a 
separate file, even if they are implemented in the same file.

This is why API methods have their own integration test file under the `client` directory even though they are all 
implemented in the `client.py` file.

Currently, this project uses [**Codecov**](https://codecov.io/gh/jaebradley/draftkings_client) for code 
coverage statistics.

## Continuous Integration

[**GitHub Actions**](https://github.com/jaebradley/draftkings_client/actions) is used for continuous 
integration to run tests on a variety of operating systems.

## Documentation Application 

This project uses [the `MkDocs` library](https://www.mkdocs.org) to generate the assets associated with the 
documentation application.

To run the documentation application locally, ensure dependencies are installed and then execute

```bash
mkdocs serve
```
