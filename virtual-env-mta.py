#!/bin/bash

echo "Creating Anaconda environment for Multi-Touch Attribution..."
conda create -n mta_env python=3.9 -y

echo "Activating the environment..."
source activate mta_env  # Use 'conda activate mta_env' if this doesn't work

echo "Setup completed! Run 'conda activate mta_env' to use the environment."
