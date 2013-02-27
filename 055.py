def lychrelNumbers():
   lychrels = 0
   for i in range(1, 10001):
      product = i
      for j in range(0, 50):
	 reverse = int(str(product)[::-1])
	 product += reverse
	 if isPalindrome(product) == 1:
	    break
	 if j == 49:
	    lychrels += 1
   print lychrels

def isPalindrome(num):
   reverse = int(str(num)[::-1])
   if reverse == num:
      return 1
   return 0

lychrelNumbers()
