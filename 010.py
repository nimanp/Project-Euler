import math
def sumOfPrimes(num):
   array = [1]*num
   array[0] = 0
   array[1] = 0
   for i in range(2, math.sqrt(num)):
      for j in range(2*i, len(array), i):
	 array[j] = 0

   sum = 0
   for i in range(2, len(array)):
      if array[i] == 1:
	 sum += i

   print sum

sumOfPrimes(2000000)
