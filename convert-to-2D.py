# import json

# # Read the model_string.txt file
# with open("run_result.json", "r") as file:
#     data = file.read()


# # Parse the JSON string into a dictionary
# json_data = json.loads(data)

# # Convert data to JSON format
# json_data = json.dumps(json_data, indent=4)

import json

# Function to determine the grid position of a product
def get_grid_position(x, y, w, h, scale_x, scale_y, shelf_width, shelf_height):
    # Calculate the center of the product
    center_x = x + w / 2
    center_y = y + h / 2
    
    # Scale the position to fit in the shelf grid
    grid_x = int(center_x * scale_x)
    grid_y = int(center_y * scale_y)
    
    # Ensure the positions are within the grid bounds
    grid_x = min(max(grid_x, 0), shelf_width - 1)
    grid_y = min(max(grid_y, 0), shelf_height - 1)
    
    return grid_x, grid_y

# Read JSON data from file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Main function to convert JSON data to 2D array
def json_to_2d_array(json_data):
    # Extract image dimensions and scale factors
    shelf_width = 10  # Define a fixed grid size for simplicity
    shelf_height = 10
    scale_x = shelf_width / json_data["imageMetadata"]["width"]
    scale_y = shelf_height / json_data["imageMetadata"]["height"]
    
    # Initialize the 2D array (shelf)
    shelf = [[None for _ in range(shelf_width)] for _ in range(shelf_height)]
    
    # Place products on the shelf based on their bounding box
    for product in json_data["products"]:
        x, y, w, h = product["boundingBox"].values()
        grid_x, grid_y = get_grid_position(x, y, w, h, scale_x, scale_y, shelf_width, shelf_height)
        # Use the most confident tag as the product representation
        most_confident_tag = max(product["tags"], key=lambda tag: tag["confidence"])["name"]
        shelf[grid_y][grid_x] = most_confident_tag
    
    return shelf

# Path to your JSON file
file_path = 'run_result_1.json'

# Read the JSON file
json_data = read_json_file(file_path)

# Convert the JSON data to a 2D array and print it
shelf_array = json_to_2d_array(json_data)

for row in shelf_array:
    print('\nwith none : \n',row)

def filter_and_print_shelf(shelf_array):
    # Filter out rows that consist entirely of None
    filtered_shelf = [row for row in shelf_array if any(item is not None for item in row)]
    
    # Print the filtered shelf, excluding None values in rows
    for row in filtered_shelf:
        print([item if item is not None else '' for item in row])

# Assuming `shelf_array` is the 2D array you've obtained
# Use the modified function to print the shelf
print('\nwithout none : \n')
filter_and_print_shelf(shelf_array)




