import json

# GLOBAL: Dictionary
# Used to cities by population rank
newData = {}
newData['cities'] = []

# Writes data to json file
def write_json(fileName, jsonData):
    with open(fileName, 'w+') as f:
        json.dump(jsonData, f)

# Loads json data from file and returns it
def read_json(jsonFile):
    with open(jsonFile) as file:
        data = json.load(file)

    return data

# Sort_Dictionary: Takes in ranks 1 to 1000
# Searches the dictionary for the current iterable and places it
# in the sorted dictionary
def sort_dictionary(rankOrder, jsonData, dataLength):
    # Loops through unordered dataset, extracts the rank and checks to see if it's next in order
    for n in range(0, dataLength, 1):
        elementRank = jsonData[n]["fields"]["rank"]

        # If the element rank is next in order, places it in new dataset
        if elementRank == rankOrder:
            print(f"Rank: {elementRank}")
            newData['cities'].append(jsonData[n]["fields"])
            # return used to end loop and start on next iteration
            return

# Main: used to read unordered list of cities (city_cords.json)
# and sort them by rank from 1 to 1000
def main():

    # Read the json data set and place into a variable
    jsonFile = "city_cords.json"
    jsonData = read_json(jsonFile)

    # Get the length of the dataset
    dataLength = len(jsonData)

    # Loops through 1 to 1000 (Top 1000 US cities)
    # Calls sort dictionary and allows us to find and append cities in order 1 to 1000
    for rankOrder in range(1, dataLength + 1, 1):
        sort_dictionary(rankOrder, jsonData, dataLength)

    # Write global dictionary to json file
    write_json('top_1000_us_cities.json', newData)


# Call main
main()

print("Sort has Finished")
