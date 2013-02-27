def primeFinder():
   array = [1]*200000
   array[0] = 0
   array[1] = 0
   for i in range(2, 448):
      for j in range(2*i, len(array), i):
	 array[j] = 0

   count = 0
   for i in range(2, len(array)):
      if array[i] == 1:
	 count += 1
	 if count == 10001:
	    print i

primeFinder()
