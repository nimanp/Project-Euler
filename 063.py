def powerfulDigitCounts():
   total = 0
   for i in range(1, 100):
      for j in range(1, 100):
	 power = i**j
	 if len(str(power)) == j:
	    total += 1
   print total

powerfulDigitCounts()
