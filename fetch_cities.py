import json
import argparse

def extract_unique_cities(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    unique_cities = set()
    for item in data.get("results", []):
        city = item.get("city")
        if city:
            unique_cities.add(city)

    return list(unique_cities)

def write_cities_to_file(cities, output_file):
    with open(output_file, 'w') as file:
        for city in sorted(cities): 
            file.write(city + '\n')

def main():
    parser = argparse.ArgumentParser(
        description="Fetch all of the unique names associated with a zip code radius based on an input file"
    )
    parser.add_argument("json_file", help="JSON file containing list of cities")
    parser.add_argument("zip_code", help="Starting zip code from search")
    parser.add_argument("radius", help="Radius")
    args=parser.parse_args()

    json_file = args.json_file
    output_file = f'./saved-results/all_cities_{args.zip_code}_{args.radius}'
    cities = extract_unique_cities(json_file)
    write_cities_to_file(cities, output_file)

if __name__ == "__main__":
    main()
