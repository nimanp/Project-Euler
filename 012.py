import math
def divisibleTriNum():
   done = 0
   curTriNum = 0
   index = 1

   while done == 0:
      curTriNum += index
      index += 1
      if numDivisors(curTriNum) > 500:
	 done = 1
   print curTriNum

def numDivisors(n):
   divisors = 0
   for i in range(1, math.sqrt(n)):
      if n % i == 0:
	 divisors += 2
   return divisors
   
divisibleTriNum()
