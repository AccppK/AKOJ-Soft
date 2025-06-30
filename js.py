import os
import json

def generate_software_list(directory, json_file):
    software_list = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            extension = filename.split('.')[-1].lower()
            name = os.path.splitext(filename)[0]
            software_list.append({'name': name, 'type': extension})
    with open(json_file, 'w') as outfile:
        json.dump(software_list, outfile, indent=4)

# Set the path to your 'soft' directory here
soft_directory = './soft'
json_output = './software.json'

generate_software_list(soft_directory, json_output)
