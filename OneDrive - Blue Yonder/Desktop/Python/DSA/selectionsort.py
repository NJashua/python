# my_array = [2, 54, 4,21, 5, 54, 2,1]
# n = len(my_array)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1, n):
#         if my_array[j] < my_array[min_index]:
#             min_index = j 
#     min_val = my_array.pop(min_index)
#     my_array.insert(i, min_val)

# print("Sorted array is: ", my_array)

# array = [9, 4, 6, 2]
# n = len(array)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1, n):
#         if array[j] < array[min_index]:
#             min_index = j 
#     min_val = array.pop(min_index)
#     array.insert(i,min_val)
# print("Selection sorted array is: ", array) 

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j

    my_array[i], my_array[min_index] = my_array[min_index],my_array[i]

print("Sorted array: ", my_array)