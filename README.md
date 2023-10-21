
<p align="center"><img alt="Logo" src="https://github.com/javedali99/csv-to-yaml-converter/assets/15319503/1b707dad-d76d-4b7c-939b-c4b1a03f9ae4" width=150px></a></p>

<h1 align="center">Bi-directional CSV-YAML Converter</h1>

<p align="center">
Effortlessly convert between CSV and YAML formats using either a Python script or a command-line interface (CLI).

</p>

<br>

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

This repository provides two utilities for bi-directional conversions between CSV and YAML formats:

1. **Script-based Conversion**: An interactive Python script that prompts the user to choose a conversion direction and then to provide the appropriate input and output file paths.
2. **CLI-based Conversion**: A command-line utility that allows users to specify the conversion direction and file paths as arguments, offering a streamlined conversion process suitable for automation and batch processing.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/javedali99/bi-directional-csv-yaml-converter.git
   cd csv-yaml-converter
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
   conda create --name csv_yaml_converter_env python=3.9
   ```

2. Activate the conda environment:
   ```bash
   conda activate csv_yaml_converter_env
   ```

3. Install the required packages:
   ```bash
   conda install -c anaconda pyyaml
   ```

## Usage

### Script-based Conversion

1. Run the script:
   ```bash
   python bi_directional_csv_yaml_script.py
   ```
2. Follow the on-screen prompts to choose the conversion mode and provide file paths.

### CLI-based Conversion

For CSV to YAML:
```bash
python bi_directional_csv_yaml_cli.py csv-to-yaml path_to_input.csv path_to_output.yaml
```

For YAML to CSV:
```bash
python bi_directional_csv_yaml_cli.py yaml-to-csv path_to_input.yaml path_to_output.csv
```

## Requirements

- Python 3.8 or newer
- PyYAML package

## Contributing

1. Fork the repository on GitHub.
2. Clone the forked repository and make the necessary changes.
3. Push your changes to your GitHub repository.
4. Submit a pull request, providing a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

