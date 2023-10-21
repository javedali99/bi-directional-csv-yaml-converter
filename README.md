# CSV to YAML Converter

Convert CSV files to YAML format seamlessly using either a Python script or a command-line interface (CLI).

## Table of Contents

- [Description](#description)
- [Installation](#installation)
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
   git clone https://github.com/YourUsername/csv-to-yaml-converter.git
   cd csv-to-yaml-converter
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
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

- Python 3.x
- `PyYAML` library (already listed in `requirements.txt`)

## Contributing

1. Fork the repository on GitHub.
2. Clone the forked repo and make your necessary changes.
3. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
