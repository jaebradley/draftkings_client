# DraftKings Python Client

[![Build Status](https://travis-ci.org/jaebradley/draftkings_client.svg?branch=v3)](https://travis-ci.org/jaebradley/draftkings_client)
[![codecov](https://codecov.io/gh/jaebradley/draftkings_client/branch/v3/graph/badge.svg)](https://codecov.io/gh/jaebradley/draftkings_client)
![PyPI](https://img.shields.io/pypi/v/draft_kings.svg)

## Introduction

To the best of my knowledge, **DraftKings** does not have an "official", well-documented public-facing API.

Instead, they have various **HTTP** endpoints that do not require authentication (so are "public" in this manner).

These "public" endpoints allow one to fetch data for various resources including contests for a specific sport, or
players that are draftable for a given contest (as well as relevant metadata).

As **DraftKings** makes no guarantees about it's "public" API, this client makes no guarantees that the existing API 
methods will work consistently.

## Documentation

For documentation about package installation as well as the client's API, please see 
[the documentation site](https://jaebradley.github.io/draftkings_client).
