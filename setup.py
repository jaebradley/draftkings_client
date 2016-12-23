
from setuptools import setup, find_packages
setup(
  name = 'draft_kings',
  packages = find_packages(exclude=['tests*']),
  install_requires=['requests', 'enum34'],
  version = '0.1',
  description = 'A DraftKings client',
  author = 'Jae Bradley',
  author_email = 'jae.b.bradley@gmail.com',
  url = 'https://github.com/jaebradley/draftkings_client', # use the URL to the github repo
  download_url = 'https://github.com/jaebradley/draftkings_client/tarball/0.1', # I'll explain this in a second
  keywords = ['sports', 'dfs', 'draftkings'], # arbitrary keywords
  classifiers = [],
)