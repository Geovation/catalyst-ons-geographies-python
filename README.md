# ONS Geographies Python library

A python library for querying the CatalyST ONS Geographies database.

## Database dependency

This library depends on a `duckdb` database to be embedded as part of your solution. Versions of this database are available in the release artifacts of the [catalyst-ons-geographies-db](https://github.com/geovation/catalyst-ons-geographies-db) repository e.g. `https://github.com/geovation/catalyst-ons-geographies-db/releases/download/v1.3.0/ons_postcodes.duckdb`

This database file `ons_postcodes.duckdb` should be placed within a `data` directory in the root of the project. In future this will be changed so that any data path can be specified.

For each python library release the release notes will specify the database version it is compatible with, and include a link to that version.

## Install

The library can be installed using `pip`. It is not currently published to a repository such as PyPI but it can be installed by direct link to the latest version tag on GitHub.

```console
$ pip install git+https://github.com/Geovation/catalyst-ons-geographies-python.git@v0.1.0
```

Replace the version tag with the latest version. To upgrade reinstall with the latest tag (or whichever tag you choose).

## Usage

After installation in a python project, functions from the library can be included as so:

```python
from catalyst_ons_geography.postcodes import get_ons_from_postcodes
```

A list of modules and functions is provided below:

### postcodes.get_ons_from_postcodes

Gets a ONS postcode directory object from one or many postcodes. The function takes in an array of postcodes and returns an array of ONS postcode data objects.

## Licence

MIT Licence
