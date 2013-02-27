def truncatablePrimes():
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

   truncatables = []
   for i in range(len(primes)-1, 3, -1):
      if len(truncatables) == 11:
	 break
      curNum = str(primes[i])
      for j in range(1, len(curNum)):
	 if isPrime(curNum[j:], primes) == 0 or isPrime(curNum[:len(curNum)-j], primes) == 0:
	    break
	 if j == len(curNum)-1 and isPrime(curNum[0], primes) and isPrime(curNum[len(curNum)-1], primes):
	    truncatables.append(primes[i])
      
   print truncatables

   sum = 0
   for i in range(0, len(truncatables)):
      sum += truncatables[i]
   print sum

def isPrime(num, array):
   for i in range(0, len(array)):
      if num == array[i]:
	 return 1
   return 0


truncatablePrimes()
