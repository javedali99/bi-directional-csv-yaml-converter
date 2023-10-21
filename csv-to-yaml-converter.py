"""
Bi-directional CSV-YAML Converter (Script-based)

Author: Javed Ali
Email: javedali28@gmail.com
Website: https://javedali.net

Date: October 21, 2023

Description:
    This Python script offers the functionality to convert between CSV and YAML formats.
    It provides two main functionalities:
    1. Convert CSV files to YAML format.
    2. Convert YAML files to CSV format.
    
    The user can choose the desired conversion mode and provide file paths when prompted.
    
Usage:
    python csv_yaml_converter.py <conversion-mode> <input-file-path> <output-file-path> 
    
Requirements:
    - Python 3.x
    - PyYAML library (install with 'pip install PyYAML')
    
Modules:
    - csv: Used for reading and writing CSV files.
    - yaml: Used for reading and writing YAML files.    

"""

# Import the required libraries
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

    Description:
    The function reads the specified CSV file, converts its content into a list of dictionaries,
    and then writes this list to the specified YAML file.
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

    Description:
    The function reads the specified YAML file, converts its content into a list of dictionaries,
    and then writes this list to the specified CSV file, preserving the original structure.
    """
    with open(yaml_filename, "r") as yaml_file:
        data = yaml.safe_load(yaml_file)

    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow(row)


if __name__ == "__main__":
    print("Bi-directional CSV-YAML Converter")
    mode = input("Choose conversion mode: (1) CSV to YAML, (2) YAML to CSV: ")

    if mode == "1":
        csv_path = input("Enter path to input CSV: ")
        yaml_path = input("Enter path to output YAML: ")
        csv_to_yaml(csv_path, yaml_path)
        print(f"Converted {csv_path} to {yaml_path} successfully!")

    elif mode == "2":
        yaml_path = input("Enter path to input YAML: ")
        csv_path = input("Enter path to output CSV: ")
        yaml_to_csv(yaml_path, csv_path)
        print(f"Converted {yaml_path} to {csv_path} successfully!")
