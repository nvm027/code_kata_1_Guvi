n = int(input("Enter N value:"))
a = int(input("Enter A Value:"))
d = int(input("Enter D Value:"))
def sumAP( a, d,n) :
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
print (sumAP(a, d, n))
