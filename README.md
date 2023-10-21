# CSV to YAML Converter

Convert CSV files to YAML format seamlessly using either a Python script or a command-line interface (CLI).

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
  - [Using pip and venv](#using-pip-and-venv)
  - [Using conda](#using-conda)
- [Usage](#usage)
  - [Script-based Conversion](#script-based-conversion)
  - [CLI-based Conversion](#cli-based-conversion)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Description

This repository contains two utilities for converting CSV files to YAML format:

1. **Script-based Conversion**: A Python script that, when executed, converts a specified CSV file to a corresponding YAML file.
2. **CLI-based Conversion**: A command-line tool that allows users to specify the input CSV file and the output YAML file through command-line arguments.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/javedali99/csv-to-yaml-converter.git
   cd csv-to-yaml-converter
   ```

## Environment Setup

### Using pip and venv

1. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

2. Install the required packages:
   ```bash
   pip install PyYAML
   ```

### Using conda

1. Create a conda environment:
   ```bash
   conda create --name csv_to_yaml_env python=3.9
   ```

2. Activate the conda environment:
   ```bash
   conda activate csv_to_yaml_env
   ```

3. Install the required packages:
   ```bash
   conda install -c anaconda pyyaml
   ```

## Usage

### Script-based Conversion

1. Edit the `csv_to_yaml_script.py` file and provide the path to your input CSV and desired output YAML file.
2. Run the script:
   ```bash
   python csv_to_yaml_script.py
   ```

### CLI-based Conversion

Execute the CLI script with the paths to the input CSV and output YAML files as arguments:

```bash
python csv_to_yaml_cli.py path_to_input.csv path_to_output.yaml
```

## Requirements

- Python 3.8 or newer
- PyYAML package

## Contributing

1. Fork the repository on GitHub.
2. Clone the forked repo and make the necessary changes.
3. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

