# Insertion sort holds one part of the sorted array later,
#  it checks the unsorted array to sort and place the elements in correct order in sorted array... 

# for ex


# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# n = len(my_array)
# for i in range(1, n):
#     insert_index = i
#     current_val = my_array.pop(i)
#     for j in range(i-1, -1, -1):
#         if my_array[j] > current_val:
#             insert_index = j
#     my_array.insert(insert_index, current_val)

# print("Insertion array is: ", my_array)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)
for i in range(1, n):
    insert_index = i 
    current_val = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_val:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_val

print("Insertion sort is: ", my_array)