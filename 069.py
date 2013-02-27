from __future__ import division
def totientMax():
   max = 0
   maxIndex = 0
   i = 30030
   while i < 1000000:
      ratio = i/totient(i)
      if ratio > max:
	 max = ratio
	 maxIndex = i
      i += 30030
   print max
   print maxIndex

def totient(num):
   factors = []
   for i in range(2, num/2+1):
      if num % i == 0:
	 factors.append(i)
	 for j in range(2, num/i):
	    factors.append(j*i)

   factors.sort()
   factors = list(set(factors))
   return (num-1)-len(factors)
      
totientMax()
