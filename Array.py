# import array as arr
# from collections import Counter as ctr
# a=arr.array('i')
# for i in range(0,5):
#     a.append(int(input()))
# a.insert(1,100)
# a.remove(100)
# a.pop(3)

# print (a[1:])
# if(10 in a):
#     print("10 is present in a")
# else :
#     print("Not present in a")
# print(ctr(a))
# print(list(ctr(a).elements()))

# import array as arr
# a=arr.array('i',[10,20,30,40,50])
# for i in range(0,5):
#    a[i]=int(input())
# a.insert(1,100)
# a.remove(100)
# a.pop(3)
# print (a)

# using List
lst=[1,2,3,4,5,6,7]
# search
for i in range(len(lst)):
    if(lst[i]==1):
        print(1)
# insert
lst.append(8)
lst.insert(8,1000)
print(lst)

# update
lst[0]=0
print(lst)

#delete
lst.remove(5)
lst.pop(0)
print(lst)

#Traverse
for i in lst:
    print(i)
# Sorting
lst.sort()
print("Ascending Order",lst)
lst.sort(reverse=True)
print("Descending Order",lst)