def primeFactor(num):
   array = []
   for i in range(1, 776000):
      if num % i == 0: #if the current number is a factor
	 array.append(i)

   print array

primeFactor(600851475143)
