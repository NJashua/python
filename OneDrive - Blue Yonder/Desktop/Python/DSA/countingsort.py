# Arranges the elements in an array by counting each value, like first it 
# counts the array and forms a count array and sorts based on no.of elements 
# def countingsort(array):
#     max_val = max(array)
#     # print(max_val)
#     count = [0] * (max_val + 1)
#     # print(count)
#     while len(array)>0:
#         num = array.pop(0)
#         print(num)
#         count[num] += 1
    
#     for i in range(len(count)):
#         while count[i] >0:
#             array.append(i)
#             count[i] -= 1
#     return array

# array = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3, 4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# rest = countingsort(array)
# print("Counting sort is: ", rest)

def countingsort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1
    
    for i in range(len(count)):
        while count[i]>0:
            arr.append(i)
            count[i] -= 1
    return arr
unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
result = countingsort(unsortedArr)
print("Counting sort is: ", result)