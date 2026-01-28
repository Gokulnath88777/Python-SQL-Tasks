arr=[10,20,30,40,50,60]
d=2
for i in range(d):
    for j in range(len(arr)-1):
        arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)