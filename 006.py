def sumSquareDif(num):
   sumOfSquares = squareOfSums = 0
   for i in range(1, num+1):
      sumOfSquares += i**2

   squareOfSums = (num*(num+1)/2)**2

   dif = squareOfSums-sumOfSquares
   print dif

sumSquareDif(100)
