lwr = int(input("Enter lower range: "))
upr = int(input("Enter upper range: "))
 
for n in range(lwr,upr + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
