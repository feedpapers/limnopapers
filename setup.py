"""A package to monitor limnology RSS feeds and tweet new articles."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="limnopapers",
    version="0.0.1",
    author="Jemma Stachelek",
    author_email="stachel2@msu.edu",
    description="A package to monitor limnology RSS feeds and tweet new \
                articles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jsta/limnopapers",
    scripts=["bin/limnopapers"],
    include_package_data=True,
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
