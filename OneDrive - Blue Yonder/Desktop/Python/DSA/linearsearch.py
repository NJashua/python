# def sorted_arr(arr, target_val):
#     for i in range(len(arr)):
#         if arr[i] == target_val:
#             return i 
#         return -1
    
# arr = [2, 7, 2, 9, 5, 33]
# target_val = 9
# res = sorted_arr(arr, target_val)
# print("Target val: ", res)

# if res != -1:
#     print("Value",  target_val, "Found at index", res)
# else:
#     print("Value", target_val, "not found")

def linearsearch(arr, target_val):
    for i in range(len(arr)):
        if arr[i] == target_val:
            return i
    return -1


arr = [3, 7, 2, 9, 5]
target_val = 5
res = linearsearch(arr, target_val)

if res != -1:
    print("Value", target_val, "Found at index", res)
else:
    print("Value",target_val, "Not found")