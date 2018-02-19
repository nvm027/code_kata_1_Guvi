n1=[]
n2=int(input("Enter no of inputs:"))
for i in range(1,n2+1):
    n3=int(input("Enter input:"))
    n1.append(n3)
n1.sort()
print("Largest number is:",n1[n2-1])
