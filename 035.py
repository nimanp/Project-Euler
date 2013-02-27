def circularPrimes():
   total = 1
   array = [1]*1000000
   array[0] = 0
   array[1] = 0
   for i in range(2, 1000):
      for j in range(2*i, len(array), i):
	 array[j] = 0

   primes = []
   for i in range(0, len(array)):
      if array[i] == 1:
	 primes.append(str(i))
	 
   for i in range(0, len(primes)):
      circular = 0
      temp = primes[i]
      for j in range(0, len(primes[i])):
	 if len(primes[i]) == 1:
	    total += 1
	 else:
	    primes[i] = primes[i][1:] + primes[i][0]
	    for k in range(0, len(primes)):
	       if primes[i] == primes[k] and i != k:
		  circular += 1
		  print circular

      if circular == len(primes[i])-1 and len(primes[i]) != 1:
	 total += 1
      primes[i] = temp

   print total

circularPrimes()
