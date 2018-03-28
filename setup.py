
from setuptools import setup, find_packages
setup(
  name='draft_kings',
  packages=find_packages(exclude=['tests*']),
  install_requires=['requests', 'enum34'],
  version='0.9',
  description='A DraftKings client',
  author='Jae Bradley',
  author_email='jae.b.bradley@gmail.com',
  url='https://github.com/jaebradley/draftkings_client',
  download_url='https://github.com/jaebradley/draftkings_client/tarball/0.2',
  keywords=['sports', 'dfs', 'draftkings'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2.7',
  ],
)