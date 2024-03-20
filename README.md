# `tap-gohighlevel`

GoHighLevel tap class.

Built with the [Meltano Singer SDK](https://sdk.meltano.com).

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

## Settings

| Setting | Required | Default | Description |
|:--------|:--------:|:-------:|:------------|
| client_id | True     | None    | Client ID for the API service |
| client_secret | True     | None    | Client Secret for the API service |
| refresh_token | True     | None    | Refresh token for the API service |
| location_id | True     | None    | The Location Id to request data |
| stream_maps | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config | False    | None    | User-defined config values to be used within map expressions. |
| faker_config | False    | None    | Config for the [`Faker`](https://faker.readthedocs.io/en/master/) instance variable `fake` used within map expressions. Only applicable if the plugin specifies `faker` as an addtional dependency (through the `singer-sdk` `faker` extra or directly). |
| faker_config.seed | False    | None    | Value to seed the Faker generator for deterministic output: https://faker.readthedocs.io/en/master/#seeding-the-generator |
| faker_config.locale | False    | None    | One or more LCID locale strings to produce localized output for: https://faker.readthedocs.io/en/master/#localization |
| flattening_enabled | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth | False    | None    | The max depth to flatten schemas. |
| batch_config | False    | None    |             |
| batch_config.encoding | False    | None    | Specifies the format and compression of the batch files. |
| batch_config.encoding.format | False    | None    | Format to use for batch files. |
| batch_config.encoding.compression | False    | None    | Compression format to use for batch files. |
| batch_config.storage | False    | None    | Defines the storage layer to use when writing batch files |
| batch_config.storage.root | False    | None    | Root path to use when writing batch files. |
| batch_config.storage.prefix | False    | None    | Prefix to use when writing batch files. |

A full list of supported settings and capabilities is available by running: `tap-gohighlevel --about`

## Supported Python Versions

* 3.8
* 3.9
* 3.10
* 3.11
* 3.12

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-gohighlevel --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

See the docs for more details https://highlevel.stoplight.io/docs/integrations/0443d7d1a4bd0-overview.

## Write Back Feature

The GoHighlevel API uses OAuth credentials but each time the refresh token is used to get a new access token, the refresh token is invalidated.
This means that we need to store the new refresh token provided in the access token response, otherwise we need to go through the authorization flow again to get a new valid refresh token.
This is a pain and isn't directly solved by the SDK or Meltano, see https://github.com/meltano/sdk/issues/106 and https://github.com/meltano/meltano/issues/2660.

To solve this, the tap implements a writeback feature where the new refresh token is set in the input config.json file every time it changes.
As a result an exception will be thrown unless exactly one config file is provided.
Also the config file will need have write access so the tap can edit it.

## Usage

You can easily run `tap-gohighlevel` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-gohighlevel --version
tap-gohighlevel --help
tap-gohighlevel --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-gohighlevel` CLI interface directly using `poetry run`:

```bash
poetry run tap-gohighlevel --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-gohighlevel
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-gohighlevel --version
# OR run a test `run` pipeline:
meltano run tap-gohighlevel target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
