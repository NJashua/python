array = [3, 5,6, 7,2, 68, -1]

min_val = array[0]
for i in array:
    if i < min_val:
        min_val = i

print("Lowest val is: ", min_val)