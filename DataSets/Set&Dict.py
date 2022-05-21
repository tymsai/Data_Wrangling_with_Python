#  sets & Dictionary

set_1={1, 2, 3, "hi"}
set_2={1, 2, 3, "hi", 4}
print(set_1 & set_2)

dict_1={1:'apple', 2:['ball', 24], 3:'cake', 4:'dog', 5:'egg'}
print(dict_1)
print(dict_1[2])

for k, v in dict_1.items():
    print("{} : {}".format(k, v))

del dict_1[2]
print(dict_1)
