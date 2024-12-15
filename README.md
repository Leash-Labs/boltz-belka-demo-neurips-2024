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
This tutorial uses [skypilot](https://docs.skypilot.co/en/latest/docs/index.html) to run inference with Boltz-1 in the cloud. SkyPilot relies on being authenticated with a supported cloud provider. [inference_runner.py](./inference_runner.py) requests resources which may only accessible with AWS. If you aren't using AWS, see which GPUs are accessible to you with `sky show-gpus`. Check the general availability of cloud providers and your authenitcation statis with `sky check`.

## BELKA
[BELKA](https://www.kaggle.com/c/leash-BELKA) is a Kaggle competition and public dataset containing over 100M observations of protein-ligand interactions.

### Downloading the full dataset
This repo comes with a small sample of the BELKA dataset to make it easier to access for the in-person presentation of this tutorial. The full dataset can be downloaded from [kaggle](https://www.kaggle.com/c/leash-BELKA) or [polaris](https://polarishub.io/datasets/leash-bio/belka-v1). The Polaris dataset contains the dataset in a more raw form.

```python
import polaris as po

# Load the dataset from the Hub
dataset = po.load_dataset("leash-bio/BELKA-v1")

# Get information on the dataset size
dataset.size()

# Load a datapoint in memory
dataset.get_data(
    row=dataset.rows[0],
    col=dataset.columns[0],
)

# Or, similarly:
dataset[dataset.rows[0], dataset.columns[0]]

# Get an entire data point
dataset[0]
```

## Boltz-1 
[Boltz-1](https://github.com/jwohlwend/boltz) is an open-source clone of AlphaFold 3 developed at MIT CSAIL. Boltz predicts the structure of biological complexes, including protein-ligand complexes. Boltz also has a module for estimating the confidence of predicted structures. 

## Using this repository
1. Start in [experiment.ipynb](./experiment.ipynb) to prepare the dataset for a Boltz-1 inference run in the cloud.
2. Use [inference_runner.py](./inference_runner.py) to kick off the inference run with skypilot. This will likely need some editing to accomodate the cloud resources you have access to.
3. After the inference run is complete, pull the inference results down to your local machine with a command specific to your cloud provider. For AWS, this looks something like `scp -r ubuntu@{ your instance's public IPv4 DNS }:~/sky_workdir/boltz-outputs ./` 
5. Return to [experiment.ipynb](./experiment.ipynb) to parse and analyze the inference results.
