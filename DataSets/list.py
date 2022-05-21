#%%
# Printing lists
list_1=[34, 12, 89, 1]
for i, element in enumerate(list_1):
    print("list_1[{}]=>{}".format(i, element))

#   34, 12, 89,  1
#    0   1   2   3
#   -4  -3  -2  -1

print(list_1[-3:-1])

#Reversing list
print(list_1[-1::-1])

#Append elements
list_2=[x for x in range(0, 10) if x%2==0]
print(list_2)

print(25 in list_1)
