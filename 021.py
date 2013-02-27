import math
def amicableNumbers():
   amicableSum = 0 
   for i in range(1, 10000):
      divSum1 = divSum2 = 1
      for j in range(2, math.sqrt(i)):
	 if i % j == 0:
	    divSum1 += j
	    divSum1 += (i/j)
      for k in range(2, math.sqrt(divSum1)):
	 if divSum1 % k == 0:
	    divSum2 += k
	    divSum2 += (divSum1/k)
      if i == divSum2 and divSum1 != i:
	 amicableSum += (i)
	 print i
   print amicableSum

amicableNumbers()

