"""
Bi-directional CSV-YAML Converter (CLI-based)

Author: Javed Ali
Email: javedali28@gmail.com
Website: https://javedali.net

Date: October 21, 2023
    
Description:
    This command-line utility offers the functionality to convert between CSV and YAML formats.
    The tool provides a user-friendly command-line interface to specify the conversion direction,
    input file, and output file paths.
    
Usage:
    python csv_yaml_converter_cli.py <conversion-direction> <input-file-path> <output-file-path>
        
Requirements:
    - Python 3.x
    - PyYAML library (install with 'pip install PyYAML')
    
Modules:
    - csv: Used for reading and writing CSV files.
    - yaml: Used for reading and writing YAML files.
    - argparse: Provides a way to specify and handle command-line arguments.
    
"""

# Import the required libraries
import argparse
import csv

import yaml


# Define the conversion function for CSV to YAML
def csv_to_yaml(csv_filename, yaml_filename):
    """
    Convert a CSV file to a YAML file.

    Parameters:
    - csv_filename (str): Path to the input CSV file.
    - yaml_filename (str): Path to the output YAML file.

    Returns:
    None
    """
    with open(csv_filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    with open(yaml_filename, "w") as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)


# Define the conversion function for YAML to CSV
def yaml_to_csv(yaml_filename, csv_filename):
    """
    Convert a YAML file to a CSV file.

    Parameters:
    - yaml_filename (str): Path to the input YAML file.
    - csv_filename (str): Path to the output CSV file.

    Returns:
    None
    """
    with open(yaml_filename, "r") as yaml_file:
        data = yaml.safe_load(yaml_file)

    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow(row)


# Define the main function to parse the command-line arguments
def main():
    """
    Main function to handle command-line arguments and control the conversion flow.
    """
    parser = argparse.ArgumentParser(description="Convert between CSV and YAML formats.")
    parser.add_argument("direction", choices=["csv-to-yaml", "yaml-to-csv"], help="Conversion direction")
    parser.add_argument("input_file", type=str, help="Path to the input file")
    parser.add_argument("output_file", type=str, help="Path to the output file")

    args = parser.parse_args()

    if args.direction == "csv-to-yaml":
        csv_to_yaml(args.input_file, args.output_file)
        print(f"Converted {args.input_file} to {args.output_file} successfully!")
    else:
        yaml_to_csv(args.input_file, args.output_file)
        print(f"Converted {args.input_file} to {args.output_file} successfully!")


if __name__ == "__main__":
    main()
