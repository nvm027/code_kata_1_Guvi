def pwr(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base number: "))
exp=int(input("Enter power value: "))
print("The result is:",power(base,exp))
