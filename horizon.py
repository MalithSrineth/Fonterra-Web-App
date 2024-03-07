# # Sample JSON data provided by the user
# data = {
#     "imageMetadata": {
#         "width": 2448,
#         "height": 3264
#     },
#     "products": [
#         {
#             "id": "12",
#             "boundingBox": {
#                 "x": 1554,
#                 "y": 520,
#                 "w": 415,
#                 "h": 553
#             },
#             "tags": [
#                 {"name": "pediapro", "confidence": 0.915},
#                 {"name": "nan", "confidence": 0.0015}
#             ]
#         },
#         {
#             "id": "11",
#             "boundingBox": {
#                 "x": 1580,
#                 "y": 2393,
#                 "w": 369,
#                 "h": 315
#             },
#             "tags": [
#                 {"name": "cereal", "confidence": 0.351},
#                 {"name": "rusk", "confidence": 0.212}
#             ]
#         }
#     ],
#     "gaps": []
# }

import json

# Path to your JSON file
file_path = './filtered_recognition_result.json'

# Read JSON data from file
with open(file_path, 'r') as file:
    data = json.load(file)

# Function to find the products that cuts a given line
def find_products_cutting_line(products, mid_y):
    cutting_products = []
    for product in products:
        y1 = product["boundingBox"]["y"]
        y2 = y1 + product["boundingBox"]["h"]
        if y1 <= mid_y <= y2:
            cutting_products.append(product)
    return cutting_products

# Sorting the products based on their 'x' and then 'y' values
sorted_products = sorted(data["products"], key=lambda x: (x["boundingBox"]["x"], x["boundingBox"]["y"]))

# Initializing the 2D array for shelf rows
shelf_rows = []

while sorted_products:
    # Finding the product with least x and least (or second least for subsequent iterations) y value
    base_product = sorted_products.pop(0)
    mid_y = base_product["boundingBox"]["y"] + base_product["boundingBox"]["h"] // 2

    # Finding all products that cut the mid_y line
    row_products = find_products_cutting_line(sorted_products, mid_y)

    # Adding the base product to the row
    row_products_names = [base_product["tags"][0]["name"]]  # Assuming the first tag's name as the product name

    # Adding other products that cut the line to the row, and removing them from the sorted_products list
    for product in row_products:
        row_products_names.append(product["tags"][0]["name"])
        sorted_products.remove(product)

    # Adding the row to the shelf_rows
    shelf_rows.append(row_products_names)

shelf_rows

print(shelf_rows)