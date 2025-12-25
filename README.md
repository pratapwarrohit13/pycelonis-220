# Pycelonis Project

This project uses Pycelonis 2.20.1 with Python 3.13.7.

## Setup

1. Ensure Python 3.13.7 is installed.
2. Create a virtual environment: `py -V:3.13 -m venv .venv`
3. Activate the virtual environment: `. .venv\Scripts\Activate.ps1` (on Windows)
4. Install dependencies: `pip install --extra-index-url=https://pypi.celonis.cloud/ -r requirements.txt`

## Requirements

See `requirements.txt` for the list of dependencies.

Note: Pycelonis requires the extra index URL for installation. Also, use Python 3.11.x as newer versions have compatibility issues with the required pydantic version.