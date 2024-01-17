import argparse
import requests
import os
from dotenv import load_dotenv
import json

def fetch_zip_codes(starting_zip, radius, country_code, api_key):
    url = f"https://app.zipcodebase.com/api/v1/radius?code={starting_zip}&radius={radius}&country={country_code}&unit=km"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: Received status code {response.status_code}\n{response.text}")

def save_to_files(data, starting_zip, radius):
    with open(f'./saved-results/zip_codes_{starting_zip}_{radius}.json', 'w') as json_file:        json.dump(data, json_file, indent=4)

    with open(f'./saved-results/zip_codes_{starting_zip}_{radius}.txt', 'w') as text_file:
        for zip_code_info in data.get("results", []):
            city = zip_code_info.get('city', 'Unknown')
            distance = zip_code_info.get('distance', 'Unknown')
            text_file.write(f"Zip Code: {zip_code_info['code']}, City: {city}, Distance: {distance} km\n")

def main():
    parser = argparse.ArgumentParser(description="Fetch and save zip codes within a radius of a given starting zip code.")
    parser.add_argument("starting_zip", help="Starting zip code")
    parser.add_argument("radius", help="Radius in kilometers")
    parser.add_argument("country_code", help="Country code")

    args = parser.parse_args()

    load_dotenv()
    api_key = os.getenv('ZIPCODE_API_KEY')

    if api_key is None:
        raise Exception("ZIPCODE_API_KEY not found in environment variables")

    data = fetch_zip_codes(args.starting_zip, args.radius, args.country_code, api_key)
    save_to_files(data, args.starting_zip, args.radius)

if __name__ == "__main__":
    main()
