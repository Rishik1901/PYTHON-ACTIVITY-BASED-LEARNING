elements = [10, 20, 10, 30, 20, 10, 40, 50, 30]
freq = {}

for item in elements:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("Element Frequencies:", freq)
