def pythagTriplet():
   sumAB = 0
   for c in range(335, 1000):
      sumAB = 1000 - c
      for b in range(1, sumAB):
	 a = sumAB - b
	 if a**2 + b**2 == c**2:
	    print a*b*c

pythagTriplet()
