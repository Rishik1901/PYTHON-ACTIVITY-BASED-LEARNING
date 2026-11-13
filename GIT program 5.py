original_list = [15, 22, 15, 33, 44, 22, 55, 33]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("List after removing duplicates:", unique_list)

