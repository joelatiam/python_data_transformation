# Python Data Transformation with Pandas

# Table of Contents
1. [Python Data Transformation with Pandas](#python-data-transformation-with-pandas)
2. [Overview](#overview)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
   - [Output Screenshot](#output-screenshot)
6. [Development](#development)

## Overview
This project provides tools for loading, cleaning, and transforming CPI (Consumer Price Index) data from Excel files. It specifically caters to the reported consumer price index, encompassing data from urban, rural, and national levels.

## Project Structure

    python_data_transformation/
    │
    ├── .gitignore              # Specifies intentionally untracked files to ignore
    ├── .pre-commit-config.yaml # Configuration for pre-commit hooks
    ├── .pylintrc               # Configuration for pylint
    ├── requirements.txt        # List of dependencies to install
    │
    ├── data/                   # Directory for storing data files
    │ ├── CPI_data.xlsx         # Source Excel file with CPI data  
    │ └── CPI_time_series.csv   # Output file after transformations       
    │
    ├── src/                    # Source files for the project
    │ ├── main.py               # Main script for executing data transformations
    │ └── pandas_helpers.py     # Helper functions for working with pandas DataFrames
    │
    └── venv/                   # Virtual environment directory


## Installation

To set up the project environment, follow these steps:

```bash
# Clone the repository
git clone git@github.com:joelatiam/python_data_transformation.git

# Navigate to the project directory
cd python_data_transformation

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Unix: Linux or macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt
```

## Usage

To run the data transformation process, execute the `main.py` script in the `src` directory. This script utilizes functions from `pandas_helpers.py` to load data from Excel files, perform transformations, and concatenate the results into a single DataFrame.

```bash
# Run the main script
python src/main.py
```
### Output Screenshot
![Screenshot of combined CPI data CSV](/img/Screen%20Shot%202024-04-28%20at%2015.56.29.png)


## Development

This project utilizes pre-commit hooks for maintaining code quality standards:

```bash
# Install pre-commit hooks
pre-commit install

# Run pre-commit on all files (manually)
pre-commit run --all-files
```
