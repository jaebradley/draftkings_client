import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="draft_kings",
    version="2.0.0",
    author="Jae Bradley",
    author_email="jae.b.bradley@gmail.com",
    license="MIT",
    description="An unofficial DraftKings Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaebradley/draftkings_client",
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires=">=3.4",
    install_requires=[
        "requests==2.20.0",
        "pytz==2018.7",
        "python-dateutil==2.8.0",
        "urllib3==1.24.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "Daily Fantasy Sports",
        "DraftKings",
    ],
)