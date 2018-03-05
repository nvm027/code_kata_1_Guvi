lwr = int(input("Enter lower range: "))
upr = int(input("Enter upper range: "))

for n in range(lwr,upr + 1):
   sum = 0
   tmp = n
   while tmp > 0:
       dgt = tmp % 10
       sum += dgt ** 3
       tmp //= 10

   if n == sum:
       print(n)
