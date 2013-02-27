import math
def nonAbundants(num):
   abundants = []
   for i in range(1, num):
      curSum = 0
      for j in range(1, (i/2)+1):
	 if i % j == 0:
	    curSum += j
      if curSum > i:
	 for k in range(1, num/i+1):
	    abundants.append(i*k)
   abundants = list(set(abundants))
   abundants.sort()
   print "Abundant numbers: " + str(abundants)

   sums = []
   for i in range(0, len(abundants)):
      for j in range(i, len(abundants)):
	 if abundants[i]+abundants[j] <= num:
	    sums.append(abundants[i]+abundants[j])

   sums = list(set(sums))
   sums.sort
   print "Possible sums of abundants:" + str(sums)

   total = 0
   for i in range(1, num+1):
      total += i
   for j in range(0, len(sums)):
      total -= sums[j]

   print total


nonAbundants(28123)
