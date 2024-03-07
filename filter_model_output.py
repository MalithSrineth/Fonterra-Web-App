import json

def filter_products_by_bounding_box(input_file_path, output_file_path):
    # Load the JSON data from the file
    with open(input_file_path, "r") as file:
        data = json.load(file)

    # Filter function based on the rule
    def follows_rule(product):
        confidence = product['tags'][0]['confidence']
        w = product['boundingBox']['w']
        h = product['boundingBox']['h']
        im_w = data['imageMetadata']['width']
        return (w < 2 * h) and (h < 2 * w) and confidence > 0.3 and (w > im_w/20)
        # return True
        
    # Apply the filter function to the products in the JSON data
    filtered_products = [product for product in data['products'] if follows_rule(product)]

    # Update the data with filtered products
    data['products'] = filtered_products


    # Save the filtered data back to a new JSON file
    with open(output_file_path, "w") as filtered_file:
        json.dump(data, filtered_file, indent=4)

# Specify the path to your input and output JSON files
input_file_path = 'run_result_1.json'  # Change this to your input file path
output_file_path = './filtered_recognition_result1.json'  # Change this to your desired output file path

# Call the function with the file paths
filter_products_by_bounding_box(input_file_path, output_file_path)

print("Filtered JSON data has been saved to the output file.")