# Hey
my_array =  [64, 34, 25, 12, 22, 11, 90, 5]
print("Without boble sort: ", my_array)
n = len(my_array)
for i in range(n-1):
    # print(i)
    for j in range(n-i-1):
        if my_array[j]>my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Boble sort array is: ", my_array)