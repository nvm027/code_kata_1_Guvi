n = int(input("Enter a number: "))  
sum = 0  
tmp = n  
  
while tmp > 0:  
   dgt = tmp % 10  
   sum += dgt ** 3  
   tmp //= 10  
  
if n == sum:  
   print("YES!")  
else:  
   print("NO!")  
