def get_square(num):
    list_a = []
    for i in num:
        list_a.append(i*i)
    return list_a


num = [2,4,5]
res = get_square(num)
print(res.insert(3,5))
print(res.remove(1))