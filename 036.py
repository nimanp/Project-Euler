def doublePalindromes():
   palindromes10 = []
   sum = 0
   for i in range(1, 1000000):
      if i == reverseNum(i):
	 palindromes10.append(i)
   print palindromes10

   for i in range(0, len(palindromes10)):
      binary = bin(palindromes10[i])[2:]
      reversed = int(binary[::-1])
      if int(binary) == reversed:
	 sum += palindromes10[i]
	 print palindromes10[i]
	 print binary
	 print reversed
	 print "----"
   print sum


def reverseNum(n):
   return int(str(n)[::-1])

doublePalindromes()
