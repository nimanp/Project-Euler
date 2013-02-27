def fibonacci(n):
   if n == 1:
      return 1
   if n == 2:
      return 2

   return fibonacci(n-1) + fibonacci(n-2)

def sumEvens():
   sum = 0
   i = 1
   while fibonacci(i) <= 4000000:
      i += 1
      if fibonacci(i) % 2 == 0:
	 sum += fibonacci(i)
	
   print sum

sumEvens()
