# Can Boltz-1 confidence scores predict binding on BELKA?
This code is a part of the BELKA workshop given by Leash Bio at NeurIPS 2024.

The goal of this tutorial is to:
1. Get some hands-on experience working with BELKA data.
2. Learn to use a very cool new open source model.

## Installation / environment setup
### Poetry
This tutorial is set up as a [poetry](https://python-poetry.org/) environment for dependency management. I recommend [installing poetry](https://python-poetry.org/docs/#installation) if you haven't because it's great. If not see pyproject.toml to set up your environment your own way.

Install dependencies with
```bash
poetry install
```

And activate the environment in your command line with
```bash
poetry shell
```

### Cloud compute
This tutorial uses [skypilot](https://docs.skypilot.co/en/latest/docs/index.html) to run inference with Boltz-1 in the cloud. SkyPilot relies on being authenticated with a supported cloud provider. [inference_runner.py](./inference_runner.py) requests resources which may only accessible with AWS. If you aren't using AWS, see which GPUs are accessible to you with `sky show-gpus`.

## Boltz-1 




