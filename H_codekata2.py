def printMax(inum):

    cont = [0 for x in range(10)]

    strng = str(num)

    for i in range(len(strng)):
        cont[int(strng[i])] = cont[int(strng[i])] +  1
 
    rslt = 0
    mux = 1

 
    for i in range(10):
        while cont[i] > 0:
            rslt = rslt + ( i * mux )
            cont[i] = cont[i] - 1
            mux = mux * 10
            
    return rslt
num = int(input("Enter the Value:"))
print (printMax(num))
