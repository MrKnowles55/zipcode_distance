import csv
import map_tool
from functools import lru_cache
import pickle


class DistanceCache:
    def __init__(self):
        self.cache = {}

    @lru_cache(maxsize=1000)
    def get_distance(self, zip1, zip2):
        # check that zips are not identical
        if zip1 == zip2:
            return float(0)

        # check if already cached calculation
        if (zip1, zip2) in self.cache:
            return self.cache[(zip1, zip2)]

        # else calculates distance
        distance = map_tool.extract_distances(zip1, zip2)
        self.cache[(zip1, zip2)] = distance
        self.cache[(zip2, zip1)] = distance

        return distance

    def save_cache(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self.cache, f)

    def load_cache(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                self.cache = pickle.load(f)
        except FileNotFoundError:
            print(f"No cache file found at {file_path}. Starting with an empty cache.")


def extract_csv_data(file_path):
    data = []
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return headers, data


cache = DistanceCache()
cache_save_path = "cache.pkl"

cache.load_cache(cache_save_path)

# Example usage
file_path = "indiana_locations.csv"
headers, data = extract_csv_data(file_path)

# Get user input for a zip code
user_zip_code = input("Enter a zip code: ")

# Dict to store the distances
distances = {}

# Extract distances for each zip code in the CSV
for row in data:
    zip_code2 = row[1]
    distances[zip_code2] = cache.get_distance(user_zip_code, zip_code2)
    cache.save_cache(cache_save_path)


# Sort distances by value in ascending order
distances = dict(sorted(distances.items(), key=lambda x: x[1]))

# Print the sorted distances
for zip, distance in distances.items():
    print(f"{zip},{distance}")
