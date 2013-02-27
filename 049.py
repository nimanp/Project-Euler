def primePermutations():
   array = [1]*10000
   array[0] = 0
   array[1] = 0
   for i in range(2, 100):
      for j in range(2*i, len(array), i):
	 array[j] = 0

   primes = []
   for i in range(0, len(array)):
      if array[i] == 1:
	 primes.append(i)

   while primes[0] < 1000:
      primes.pop(0)
   
   for i in range(len(primes), 0

primePermutations()
