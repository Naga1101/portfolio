import os
import json

# Path to the root folder where all building folders are stored
root_folder = '/imagens/edificios/'

# Function to extract house details from the folder name
def get_house_info_from_folder(folder_name):
    parts = folder_name.split('_')
    
    if len(parts) != 4:
        raise ValueError(f"Invalid folder name format: {folder_name}")
    
    house_id = int(parts[0])  # id of the house
    house_type = int(parts[1])  # house type
    bedrooms = int(parts[2])  # number of bedrooms
    bathrooms = int(parts[3])  # number of bathrooms

    return {
        'id': house_id,
        'type': house_type,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms
    }

# Function to get image and blueprint files from the folder
def get_files_from_folder(folder_path):
    fotos = []
    blueprints = []

    for file_name in sorted(os.listdir(folder_path)):
        if file_name.startswith('img'):
            fotos.append(file_name)
        elif file_name.startswith('planta'):
            blueprints.append(file_name)

    return fotos, blueprints

# List to store all projects
projects = []

# Iterate over each folder in the root folder
for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)

    if os.path.isdir(folder_path):
        try:
            house_info = get_house_info_from_folder(folder_name)
        except ValueError as e:
            print(e)
            continue

        # Get the image and blueprint files
        fotos, blueprints = get_files_from_folder(folder_path)

        # Store the house info with paths to fotos and blueprints
        house_info.update({
            'fotos': [os.path.join(folder_path, foto) for foto in fotos],
            'blueprints': [os.path.join(folder_path, blueprint) for blueprint in blueprints]
        })

        projects.append(house_info)

# Save the projects info to a JSON file
output_file = 'projects.json'
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump({'projects': projects}, json_file, ensure_ascii=False, indent=4)

print(f'JSON file saved: {output_file}')
