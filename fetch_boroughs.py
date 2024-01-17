import requests
import json
import os
import argparse
from dotenv import load_dotenv

def fetch_borough_info(zip_codes, api_key):
    updated_data = []
    for zip_code in zip_codes:
        full_address = f"{zip_code}, Germany"
        response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={full_address}&key={api_key}")
        
        if response.status_code == 200:
            results = response.json()['results']
            if results:
                borough = None
                for result in results:
                    for component in result['address_components']:
                        if 'sublocality' in component['types'] or 'political' in component['types']:
                            borough = component['long_name']
                            break
                    if borough:
                        break
                
                updated_data.append({'zip_code': zip_code, 'borough': borough or 'Unknown'})
                print(f"Zip Code: {zip_code}, Borough: {borough or 'Unknown'}")
            else:
                print(f"No results found for zip code {zip_code}")
        else:
            print(f"Failed to fetch data for zip code {zip_code}: {response.status_code}")
    return updated_data

def main():
    parser = argparse.ArgumentParser(description="Fetch borough information for a list of zip codes.")
    parser.add_argument("json_file", help="JSON file containing list of zip codes")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    if not api_key:
        raise Exception("GOOGLE_MAPS_API_KEY not found in environment variables")

    with open(args.json_file, 'r') as file:
        data = json.load(file)
        zip_codes = [item['code'] for item in data.get("results", [])]

    updated_data = fetch_borough_info(zip_codes, api_key)

    with open('./saved-results/zip_codes_with_boroughs.json', 'w') as json_file:
        json.dump(updated_data, json_file, indent=4)

if __name__ == "__main__":
    main()
