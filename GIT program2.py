num = int(input("Enter a 3-digit number: "))
temp = num
sum_cubes = 0

while temp > 0:
    digit = temp % 10
    sum_cubes += digit ** 3
    temp //= 10

if sum_cubes == num:
    print(num, "is an Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")

