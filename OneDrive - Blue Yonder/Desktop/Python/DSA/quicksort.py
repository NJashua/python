# Quick sort, its a proccess of sorting elements in an array like its holds an first element in the array and
#  moves the lowest element based on that element into first side...:)""

# def partition(my_array, low, high):
#     pivot = my_array[high]
#     i = low - 1
#     for j in range(low, high):
#         if my_array[j] <= pivot:
#             i+=1
#             my_array[i], my_array[j] = my_array[j], my_array[i]
#     my_array[i+1], my_array[high] = my_array[high], my_array[i+1]
#     return i + 1
# def quicksort(my_array, low = 0, high = None):
#     if high is None:
#         high = len(my_array)-1
#     if low < high:
#         pivot_index = partition(my_array, low, high)
#         quicksort(my_array, low, pivot_index-1)
#         quicksort(my_array, pivot_index+1, high)

# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# quicksort(my_array)
# print("Quick sort is: ", my_array) 

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low = 0, high = None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

array = [56, 6, 4, 33, 5, 5, 2, 55, 543, 5, 23, 4, 5]
quicksort(array)
print("Quick Sort is: ", array)
