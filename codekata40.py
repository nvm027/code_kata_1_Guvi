nts = int(input("Enter N Value:"))
n1 = 0
n2 = 1
cnt = 0
if nts <= 0:
   print("Please enter a positive number")
elif nts == 1:
   print("Fibonacci sequence upto",nts,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nts,":")
   while cnt < nts:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       cnt += 1
