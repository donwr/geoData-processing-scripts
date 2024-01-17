# Location Research Tool

## Overview
This repository contains three Python scripts designed to fetch and process geographical data, specifically related to zip codes, cities, and boroughs. The scripts interact with external APIs and handle JSON data to extract and save relevant information.

## Scripts

1. fetch_zipcodes.py

- Description: Fetches zip codes within a specified radius of a given starting zip code.
- Usage: python fetch_zipcodes.py [starting_zip] [radius] [country_code]
- Output: Saves the fetched zip code data in both JSON and text formats to the ./saved-results/ directory.

2. fetch_cities.py

- Description: Extracts unique city names from a JSON file containing zip code data.
- Usage: python fetch_cities.py [json_file] [zip_code] [radius]
- Output: Writes the unique city names to a file in the ./saved-results/ directory.

3. fetch_boroughs.py

- Description: Fetches borough information for a list of zip codes using the Google Maps Geocoding API.
- Usage: python fetch_boroughs.py [json_file]
- Output: Saves the zip code and borough data to a JSON file in the ./saved-results/ directory.

## Requirements
- Python 3.x
- External libraries: requests, argparse, os, json
- A .env file containing API keys for the respective services (ZIPCODE_API_KEY for fetch_zipcodes.py and GOOGLE_MAPS_API_KEY for fetch_boroughs.py).

## Installation
1. Clone the repository or download the scripts.
2. Install required Python packages: pip install requests python-dotenv
3. Create a .env file in the root directory with your API keys:

- ZIPCODE_API_KEY=your_zipcode_api_key
- GOOGLE_MAPS_API_KEY=your_google_maps_api_key
4. Run the scripts as needed with the appropriate arguments.


## Notes
- Ensure you have the necessary API keys and permissions for the external services used by these scripts.
- The scripts are designed to be run independently based on the specific task required.

## EXTRA - Command to read borough json file and export alphabetical list of boroughs 
`jq -r '.[].borough' ./saved-results/berlin/zip_codes_with_boroughs.json | sort -u > unique_boroughs.txt``
