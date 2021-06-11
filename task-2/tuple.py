tup = (10,20,30,"dhruti")
print(tup)
print(tup[2])
print(tup[0:3])
print(tup[5:])
print(tup[-3:-1])


lis = []
n=int(input("enter the number of element:"))
for i in range(0,n):
        element = input("enter value")
        lis.append(element)

print(lis)
tupl = tuple(lis)
print(tupl)