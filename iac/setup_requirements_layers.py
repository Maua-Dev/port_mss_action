import os
import shutil
import subprocess
import sys
from pathlib import Path

IAC_DIRECTORY_NAME = "iac"

def install_package(package: str, destination: str):
    print(f"Installing {package} to {destination}")
    root_directory = Path(__file__).parent.parent
    iac_directory = os.path.join(root_directory, IAC_DIRECTORY_NAME)

    requirement_name = package.split("==")[0]

    layer_destination = os.path.join(iac_directory, destination, requirement_name, "python")

    if os.path.exists(layer_destination):
        print(f"Removing {layer_destination} because it already exists")
        shutil.rmtree(layer_destination)

    subprocess.check_call(["pip", "install", package, "-t", layer_destination, "--no-cache-dir"])

def setup_requirements_layers(destination: str):
    with open("requirements-layers.txt", "r") as f:
        requirements = f.read().splitlines()

    for requirement in requirements:
        print(requirement)

    for requirement in requirements:
        install_package(requirement, destination)
    
    if __name__ == '__main__':
        setup_requirements_layers(destination="lambda_requirements_layer_temp")