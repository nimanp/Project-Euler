def palindromeProduct():
   max = 0
   for i in range(999, 100, -1):
      for j in range(999, 100, -1):
	 product = i*j
	 if product == reverseNum(product) and product > max:
	    max = product

   print max

def reverseNum(n):
   return int(str(n)[::-1])

palindromeProduct()
