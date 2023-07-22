import os

# Read the requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Uninstall each package
for package in requirements:
    os.system(f"pip uninstall -y {package}")