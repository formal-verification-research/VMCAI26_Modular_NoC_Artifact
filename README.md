# Probabilistic Verification for Modular Network-on-Chip Systems Artifact

This repository contains the artifact for the paper "Probabilistic Verification for Modular Network-on-Chip Systems".

This artifact provides the models and tools used to generate the results in the paper. The models are written in the Modest language and the tools are written in Python.

## Directory Structure

- `models/`: Contains the Modest models for the Network-on-Chip (NoC) of various sizes.
- `tools/`: Contains the Python scripts for generating the results and models.
- `results/`: Contains the raw CSV data and timing information from the experiments.
- `plot/`: Contains the plots generated from the results, and the script to generate them.

## Reproducing the Results

To reproduce the results, you will need to have the Modest toolset installed and on your system's PATH. You can find installation instructions here: [modestchecker.net](https://www.modestchecker.net/).

Once Modest is installed, you can run the experiments using the `generate_results.py` script in the `tools/` directory:

```bash
python3 tools/generate_results.py
```

This will run all the simulations and generate the results in the `results/` directory.

To generate the plots, you will need to have Python with the `matplotlib` and `numpy` libraries installed. The original paper used MATLAB, but this has been converted to Python for portability. You can run the script `generate_plots.py` in the `plot/` directory:

```bash
python3 plot/generate_plots.py
```

This will generate the plots in the `plot/` directory.

## Customizing the Experiments

The `tools/noc.py` file contains the `Noc` class, which is used to generate the Modest models. You can the class in this file to generate NoC models with unique topological size, buffer size, injection rate, and other parameters.

The `tools/generate_results.py` file contains the main script for running the experiments. You can modify this file to change the simulation parameters, such as the clock upper bound, threshold, and stride.

The `tools/new_flit_injection_example.py` file shows how to create a custom flit injection pattern and run a simulation with it.
