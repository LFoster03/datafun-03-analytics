import json

# Reading a JSON file
with open('example_data/rows.json', 'r') as file:
    data = json.load(file)

print(data)

# Saving the JSON data to a .txt file
with open('json_data.txt', 'w') as txt_file:
    # Optionally, convert the data to a string if it's not already
    json_string = json.dumps(data, indent=4)
    txt_file.write(json_string)

print("Data has been saved to json_data.txt")
