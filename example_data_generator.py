import csv
import random

# List of locations and zip codes in Indiana
locations = [
    ("Indianapolis", "46201"),
    ("Fort Wayne", "46802"),
    ("Evansville", "47708"),
    ("South Bend", "46601"),
    ("Carmel", "46032"),
    ("Fishers", "46038"),
    ("Bloomington", "47401"),
    ("Hammond", "46320"),
    ("Gary", "46402"),
    ("Lafayette", "47901"),
    ("Muncie", "47302"),
    ("Noblesville", "46060"),
    ("Terre Haute", "47802"),
    ("Greenwood", "46142"),
    ("Kokomo", "46901"),
    ("Anderson", "46011"),
    ("Elkhart", "46514"),
    ("Mishawaka", "46544"),
    ("Lawrence", "46226"),
    ("Jeffersonville", "47130")
]

# Random category for each location
categories = ["Restaurant", "Park", "Museum", "Shopping Mall", "Library"]

# Randomly select 20 locations from Indiana
indiana_locations = random.sample(locations, k=20)

# Generate the CSV file
with open("indiana_locations.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Location", "Zip Code", "Category"])  # Write header row
    writer.writerows([(location[0], location[1], random.choice(categories)) for location in indiana_locations])

print("CSV file generated successfully.")
