#!/bin/bash

# Create a Conda environment with Python 3.9
conda create -n mta_env python=3.9 -y

# Initialize Conda for the current shell
source $(conda info --base)/etc/profile.d/conda.sh

echo "Run conda activate mta_env to activate the conda environment."
