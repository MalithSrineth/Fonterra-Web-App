# Updated example 2D arrays based on the new requirement
array1 = [
    ['Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g'],
    ['Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Ratthi/Normal/400g']
]

array2 = [
    ["A", "B"],
    ["C", "D"]
]

array3 = [
    [1, 2, 1, 2],
    [8, "E", "B", 5],
    [7, "C", "D", 2],
    [3, 3, 4, 5, 5],
    [8, "A", "B", 5],
    [7, "C", "D", 2]
]

array4 = [
    ['Anlene/400g', '', 'Anlene/400g', 'Anlene/400g', 'Anchor/Non Fat/400g', 'Anchor/Non Fat/400g', 'Pediapro/3-5/350g', '', 'Pediapro/3-5/350g', ''],
    ['', 'Anchor/Plus 1-5/400g', 'Anchor/Plus 1-5/400g', 'Ratthi/3 in 1/Kiri Tea', 'Ratthi/3 in 1/Kiri Tea', 'Anchor', '', 'Anchor', 'Ratthi/3 in 1/Milk n Malt', 'Ratthi/3 in 1/Milk n Malt'],
    ['', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', ''],
    ['', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', '', 'Anchor/Normal/400g', 'Anchor/Normal/400g'],
    ['Other', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', '', 'Anchor/Normal/400g'],
    ['Other', '', '', '', '', '', '', '', '', ''],
    ['', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Anchor/Normal/400g', 'Ratthi/Normal/400g', 'Ratthi/Normal/400g', 'Ratthi/Normal/400g'],
    ['Other', 'Anchor/Normal/1kg', '', 'Anchor/Normal/1kg', 'Anchor/Normal/1kg', 'Anchor/Normal/1kg', '', 'Ratthi/Normal/400g', '', 'Ratthi/Normal/400g'],
    ['', '', '', '', '', '', 'Ratthi/Normal/400g', '', '', '']
]

# Function to find and print the starting coordinates of array1 within array2
def find_subarray_coordinates(subarray, mainarray):
    rows_sub, cols_sub = len(subarray), len(subarray[0])
    rows_main, cols_main = len(mainarray), len(mainarray[0])
    
    # Iterate through mainarray to find potential starting points
    for i in range(rows_main - rows_sub + 1):
        for j in range(cols_main - cols_sub + 1):
            match_found = True
            for x in range(rows_sub):
                if mainarray[i + x][j:j + cols_sub] != subarray[x]:
                    match_found = False
                    break
            if match_found:
                return (i, j)
    return None

# coordinates = find_subarray_coordinates(array1, array2)

# if coordinates:
#     print(f"The subarray is found within the main array starting at coordinates: {coordinates}")
# else:
#     print("The subarray is not found within the main array.")


"**************************************************************************************************"  


# Updated function to find and print the starting coordinates of all matches of array1 within array2
def find_all_subarray_coordinates(subarray, mainarray):
    rows_sub, cols_sub = len(subarray), len(subarray[0])
    rows_main, cols_main = len(mainarray), len(mainarray[0])
    matches = []  # List to store the starting coordinates of all matches
    
    # Iterate through mainarray to find all potential starting points
    for i in range(rows_main - rows_sub + 1):
        for j in range(cols_main - cols_sub + 1):
            match_found = True
            for x in range(rows_sub):
                if mainarray[i + x][j:j + cols_sub] != subarray[x]:
                    match_found = False
                    break
            if match_found:
                matches.append((i, j))
    
    return matches

# Find all matches
all_matches_coordinates = find_all_subarray_coordinates(array1, array2)

# Print the starting coordinates of all matches
if all_matches_coordinates:
    print("All possible matches are found at the following coordinates:")
    for coordinates in all_matches_coordinates:
        # print(f'coordinates = ')
        print(coordinates)

else:
    print("No matches found in the main array.")


"**************************************************************************************************"  


# Function to find and print the starting coordinates of matches with matching percentage
def find_matches_with_percentage(subarray, mainarray):
    rows_sub, cols_sub = len(subarray), len(subarray[0])
    rows_main, cols_main = len(mainarray), len(mainarray[0])
    matches = []  # List to store the starting coordinates of matches and their matching percentage
    
    # Function to calculate the match percentage
    def calculate_match_percentage(sub, main):
        total_elements = len(sub) * len(sub[0])
        match_count = 0
        for x in range(len(sub)):
            for y in range(len(sub[0])):
                if sub[x][y] == main[x][y]:
                    match_count += 1
        return (match_count / total_elements) * 100
    
    # Iterate through mainarray to find all potential starting points
    for i in range(rows_main - rows_sub + 1):
        for j in range(cols_main - cols_sub + 1):
            sub_main = [row[j:j+cols_sub] for row in mainarray[i:i+rows_sub]]
            match_percentage = calculate_match_percentage(subarray, sub_main)
            # If match percentage is 75% or higher, record the match
            if match_percentage >= 50:
                matches.append(((i, j), match_percentage))
    
    return matches

# Find all matches with their matching percentage
# all_matches_with_percentage = find_matches_with_percentage(array1, array4)

# # Print the starting coordinates of all matches with their matching percentage
# if all_matches_with_percentage:
#     print("Matches found with the following details:")
#     for match in all_matches_with_percentage:
#         print(f"Coordinates: {match[0]}, Match Percentage: {match[1]:.2f}%")
# else:
#     print("No matches found in the main array.")


"**************************************************************************************************"

def find_matches_with_percentage_v2(subarray, mainarray):
    rows_sub, cols_sub = len(subarray), len(subarray[0])
    rows_main, cols_main = len(mainarray), len(mainarray[0])
    matches = []  # List to store the starting coordinates of matches and their matching percentage
    
    # Function to calculate the match percentage with bounds checking
    def calculate_match_percentage_v2(sub, main):
        total_elements = len(sub) * len(sub[0])
        match_count = 0
        for x in range(len(sub)):
            for y in range(len(sub[0])):
                # Check if we're within the bounds of the main array
                if x < len(main) and y < len(main[x]) and sub[x][y] == main[x][y]:
                    match_count += 1
        return (match_count / total_elements) * 100
    
    # Iterate through mainarray to find all potential starting points
    for i in range(rows_main - rows_sub + 1):
        for j in range(cols_main - cols_sub + 1):
            sub_main = [row[j:j+cols_sub] for row in mainarray[i:i+rows_sub] if j+cols_sub <= len(row)]
            if len(sub_main) == rows_sub and all(len(row) == cols_sub for row in sub_main):
                match_percentage = calculate_match_percentage_v2(subarray, sub_main)
                # If match percentage is 75% or higher, record the match
                if match_percentage >= 75:
                    matches.append(((i, j), match_percentage))
    
    return matches

# Find all matches with their matching percentage for the updated arrays
all_matches_with_percentage_v2 = find_matches_with_percentage_v2(array2, array3)

# Print the starting coordinates of all matches with their matching percentage
if all_matches_with_percentage_v2:
    print("Matches found with the following details:")
    for match in all_matches_with_percentage_v2:
        print(f"Coordinates: {match[0]}, Match Percentage: {match[1]:.2f}%\n")
        print(f'{match[1]:.2f = }')
else:
    print("No matches found in the main array.")