lwr=int(input("Enter the lower limit value:"))
upr=int(input("Enter the upper limit value:"))
rslt=[]
print("The Odd Numbers between",lwr,"and",upr,"is: ")
for i in range(lwr,upr+1):
    if(i%2!=0):
        rslt.append(i)
print(rslt)
