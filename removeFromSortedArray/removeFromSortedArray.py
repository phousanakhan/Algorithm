list = [1,1,1,2,2,2,3,4,5,5]
for i in list:
    while list.count(i) > 1:
        list.remove(i)
print(list)