# Flit Injection Example

This file explains the `new_flit_injection_example.py` script is used to create a Network-on-Chip (NoC) model with a custom flit injection pattern.

## Getting Started

First, we import the additional modules to help us define the NoC. `psn_results.simulate` is a function that allows us to run Modest's SMC engine from Python. `noc.PropertyType` defines what kind of NoC model we want to generate, the options are explained in [noc.py](./noc.py). We import `pathlib.Path` for ease of defining filepaths.

```python
from psn_results import simulate
from noc import PropertyType
from pathlib import Path
```

## How it Works

The `new_flit_injection_example.py` script works by defining a custom flit generation process as a string and then passing it to the `simulate` function. The `simulate` function is imported from the `psn_results.py` script, which in turn uses the `Noc` class from `noc.py` to generate a Modest model of the NoC. The `Noc` class takes a `generate_flits` parameter, which is a string containing the Modest code for the flit generation process. If this parameter is not provided, a default flit generation process is used.

The flit generation process needs to follow the specification given in Section 4.5 of the paper, and must be written in correct Modest syntax.

### Custom Flit Generation Process

The custom flit generation process is defined in the `custom_generate_flits` variable. This process sends flits in a bursty pattern, where the duty cycle varies between 5% and 25% for each router. The process uses two arrays, `burst_times` and `sleep_times`, to keep track of the burst and sleep times for each router. The `burst_times` array is initialized with random values between 10 and 100, and the `sleep_times` array is initialized with random values between 200 and 400.

When the process is executed, it first checks if the `burst_times` array for the current router is not zero. If it is not zero, it sends a flit and decrements the `burst_times` array. If the `burst_times` array is zero, it checks if the `sleep_times` array is not zero. If it is not zero, it decrements the `sleep_times` array. If both arrays are zero, it generates new random values for both arrays.

### Simulation

The `simulate` function is called with the following parameters:

- `size`: The size of the NoC (e.g., 2 for a 2x2 NoC).
- `result_path`: The path to the directory where the simulation results will be stored.
- `type`: The type of property to check (e.g., `PropertyType.RESISTIVE`).
- `threshold`: The noise threshold.
- `clk_upper`: The upper bound of the clock cycle to check.
- `stride`: The stride for the clock cycle.
- `generate_flits`: The custom flit generation process.

## How to Run

To run the script, simply execute the following command in your terminal:

```bash
python python/new_flit_injection_example.py
```

This will run a 2x2 resistive noise simulation with the custom flit generation process and save the results in the `results/2x2_custom_flit_gen` directory.
