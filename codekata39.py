arr=[]
for i in range(1,10+1):
    ipt=int(input("Enter element:"))
    arr.append(ipt)
arr.sort()
print("Largest element is:",arr[10-1])
