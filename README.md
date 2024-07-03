# BK-AUTO READER TOOL

## Hardware

- **Version:** BK-AUTO READER TOOL Hardware V1.0
- **Based on:** MKS Canable V2.0 Pro with 5 channels

## Software Features

- **Log CAN data to CSV file:** Utilize the CAN Sniffer function to log data.

## Change Logs

### SV1.1

- **CSV Info Table:** Added a CSV info table to check the time and size of the CSV file.
- **Python-can Library:** Fixed the issue of the missing python-can library in the package.
- **Stop Save CSV:** Fixed the issue where stopping the save CSV process did not delete the dataframe, preventing old data from being saved to new CSV files.
- **Threading Optimization:** Improved the threading mechanism for better performance.

## Usage

1. **Setup:** Ensure you have the BK-AUTO READER TOOL Hardware V1.0 connected.
2. **Log CAN Data:** Use the CAN Sniffer function to log data to a CSV file.
3. **Check CSV Info:** Use the CSV info table to check the time and size of your CSV files.
