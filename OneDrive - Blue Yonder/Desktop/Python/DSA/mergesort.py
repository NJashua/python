# def merge(left, right):
#     merged = []
#     i=0
#     j=0
#     while i <len(left) and j<len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i+=1
#         else:
#             merged.append(right[j])
#             j += 1
#     merged += left[i:] + right[j:]
#     return merged
# def mergesort(arr):
#     if len(arr)==1:
#         return arr
#     mid = len(arr) // 2
#     left = mergesort(arr[:mid])
#     right = mergesort(arr[mid:])
#     return merge(left, right)

# arr=[38,27,43,3,9,82,10]
# sorted_arr = mergesort(arr)
# print("Merge sort is: ", sorted_arr)

# def merge(left, right):
#     merged = []
#     i = 0
#     j = 0
#     while i <len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#     merged += left[i:] + right[j:]
#     return merged

# def mergesort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = mergesort(arr[:mid])
#     right = mergesort(arr[mid:])
#     return merge(left, right)

# arr = [38, 27, 43, 2, 4, 5]
# sorted_arr = mergesort(arr)
# print("Merge sort is: ", sorted_arr)

def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= left[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:] + right[j:]
    return merged

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


arr = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_arr = mergesort(arr)
print("Merge sort is: ", sorted_arr)