n=int(input("Enter the number to check:"))
tem=n
rv=0
while(n>0):
    dig=n%10
    rv=rv*10+dig
    n=n//10
if(tem==rv):
    print("Yes!")
else:
    print("No!")
