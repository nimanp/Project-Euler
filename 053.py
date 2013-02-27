import math
def combinatorics():
   count = 0
   for i in range(1, 101):
      for j in range(1, i):
	 combination = math.factorial(i)/(math.factorial(j)*math.factorial(i-j))
	 if combination > 1000000:
	    count += 1
   print count

combinatorics()
