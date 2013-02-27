from __future__ import division
def digitCancels():
   product = 1
   for i in range(10, 100):
      for j in range(i, 100):
	 canceledFrac = 0
	 if int(str(j)[1]) != 0 and int(str(i)[1]) == int(str(j)[0]):
	    canceledFrac = int(str(i)[0])/int(str(j)[1])
	 if i/j == canceledFrac and i/j != 1:
	    print str(i) + "/" + str(j)
	    product *= i/j
   print product

digitCancels()
