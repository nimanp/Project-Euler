import math
def factorialSum(num):
   sum = 0
   result = str(math.factorial(num))
   for i in range(0, len(result)):
      sum += int(result[i])
   print sum

factorialSum(100)
