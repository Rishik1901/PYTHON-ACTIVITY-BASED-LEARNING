numbers = [45, 12, 89, 78, 34, 89, 56]
unique_nums = list(set(numbers))
unique_nums.sort()

if len(unique_nums) >= 2:
    print("Second Largest Number:", unique_nums[-2])
else:
    print("Not enough unique elements.")

