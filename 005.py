import fractions
def smallestMultiple():
   product = 1
   for i in range(1, 20):
      product = product*i / fractions.gcd(product, i)
      print product
   
smallestMultiple()
