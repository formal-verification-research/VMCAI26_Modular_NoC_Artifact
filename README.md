# Artifact for Probabilistic Verification for Modular Network-on-Chip Systems

Authors: Nick Waddoups, Jonah Boe, Arnd Hartmanns, Prabal Basu, Sanghamitra Roy,
Koushik Chakraborty, Zhen Zhang

This is the artifact for "Probabilistic Verification for Modular Network-on-Chip
Systems". Access the artifact by downloading the zipped artifact from the releases
section of this GitHub repository, and then follow the instructions below for loading
the docker image on your machine. Steps for replicating the work presented in the paper
are located at the bottom of this document.

This artifact aims to meet the requirements for the _Available_, _Functional_, and
_Resuseable_ badges.

## Prerequisites for Using the Modular NoC model

The following software must be installed to run the modular NoC model or generate
new model templates using the Python library.

- [Modest Toolset](https://www.modestchecker.net/) Version 3.1.290 or greater.
- Python 3.10 or greater.
- 16 GB RAM or greater.

A Docker image is provided with this artifact containing the Modest Toolset and
Python. Using this Docker image is the recommended way to review this artifact.
If required, steps are provided below to install Modest and Python on a local
machine as well.

## Setting up the Docker Container

This artifact has a Docker image that contains the build of the Modest Toolset used in
the paper.

### Installing Docker Desktop

Next, you need to ensure Docker is installed. Follow the instructions located at
[docs.docker.com](https://docs.docker.com/desktop/) to install the desktop version of
Docker for you specific operating system. Once enstalled, make sure to start Docker
Desktop in order for the following commands to work correctly.

### Obtaining the Docker Image

Go to the releases tab of artifact's GitHub repository and download the latest release.

Move your shell into this directory containing the downloaded release and then
run the following command to load the Docker image.

```sh
# load the docker image -- this will take several minutes
docker load -i modular_noc.tar
```

Then start the docker image using the following command.

```sh
docker run -it modular_noc:vmcai26
```

You should now be in the docker environment. You can check that Modest and Python are
correctly installed by running the following commands.

```sh
modest --version  # v3.1.290
python3 --version # 3.13.5
```

## Installing Modest on a Local Machine

Go to [modestchecker.net](https://www.modestchecker.net/Downloads/) and read and
agree to the license terms. Then, download the zipped executable for your specific
operating system. Options are available for Linux, Mac, and Windows.

Unzip the Modest executable and add it to your path. You can test that you have
correctly added the tool to the path by going to a shell of your choice and
running the following command.

```sh
modest --version
```

The output should match the following:

```text
The Modest Toolset (www.modestchecker.net), version <v3.1.290 or greater>.
Command: modest --version
Usage:    modest <tool> <parameters>
Tools: benchmark         (mobench)
       check             (mcsta)
       check-symblicit   (mcsta-symblicit)
       convert           (moconv)
       export-to-dot     (mosta)
       export-to-python  (mopy)
       initialize        (init)
       plan              (modysh)
       plot              (moplot)
       prohver           (prohver)
       simulate          (modes)
```

## Files in this Artifact

This artifact contains the modular 2x2 model used to verify functional correctness of the
modular NoC design and the results from the verification in the [models/](./models/)
directory.

Additionally, two python scripts are provided for generating arbitrarily-sized NoC models
and for running the `modest` tool from Python in the [python/](./python/) directory.

## Replicating Modular Results From the Paper

Results can either be replicated using the provided Docker image or with a local
installation of Modest and Python.

### Modular 2x2 Correctness

To verify 2x2 correctness run the following command from this directory to produce the
correctness guarantees from Modest. This should take approximately 10 minutes and use
10 GB of memory.

```sh
modest check models/2x2_ctl_example.modest --unsafe --chainopt
```

### Modular PSN Characterization

To generate the PSN characterization results for basic 2x2, 3x3, 4x4, and 8x8 setups (Figures 3,
5, 7-9 in paper) run the following from this directory. This should take approximately 2 hrs,
and should use only a small amount of memory as it is simulating the model, not exploring the
statespace.

```sh
python3 python/psn_results.py
```

### Interpreting the Results

The output of running modest on the 2x2 correctness model demonstrate that all properties hold
for the model. Each property listed in the output represents a CTL property in the model, and
is either marked `True` if the property held or `False` if it did not hold. You can see the CTL
properties in Section V. of our paper or on lines 227-361 of
[functional_2x2.modest](models/functional_2x2.modest).

The output of the PSN characterization is stored in the result/ directory. This directory has
subdirectories for 2x2, 3x3, 4x4, and 8x8. Inside of each of these directories is a list of .csv
and .txt files containing the results of each simulation run. The files are of the following
naming convention:

```text
noc_<size>_<type>_<threshold>_<clk cycle stride>_<cycles per analysis>
```

For example, simulation results (e.g. CDF of PSN probability vs. clk cycles) for inductive noise
with a `INDUCTIVE_THRESHOLD` of 1, a clock cycle stride of 6, and 300 cycles per analysis would
be named as follows:

```text
noc_2x2_inductive_noise_threshold_1_stride_6_block_size_300
```

The files ending in .csv are the raw data from `modest simulate` formatted in a csv file, and the
files ending in .time.txt contain the simulation specification and time that it took to complete
the simulation.

To replicate the plots from the submission we provide a plotting script using Matplotlib in Python.
If you are using the docker image, simply run `python3 python/plot.py` to generate the plots.
Otherwise, first ensure that you have Matplotlib and Pandas installed before running the script.

Plots can be viewed in Docker desktop by going to "Containers" (in the leftside menu bar), then clicking
on "modular_noc", then selecting "files", then navigating to the /home/plots/ directory.

## Using Python Scripts to Generate New Models

This artifact also provides two python scripts that are useful for automating result generation of
other NoC work: [noc.py](./python/noc.py) and [modest.py](./python/modest.py). These two scripts
provide functions for generating new NoC models and running Modest models from python. The
[psn_results](./python/psn_results.py) results script makes heavy use of both these libraries.
See [NoC and Modest Library README](./python/README.md) for more information.
