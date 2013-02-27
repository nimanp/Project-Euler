def powerfulDigitSum():
   max = 0
   for i in range(1, 100):
      for j in range(1, 100):
	 digitSum = 0
	 product = str(i**j)
	 for k in range(len(product)):
	    digitSum += int(product[k])
	 if digitSum > max:
	    max = digitSum
   print max

powerfulDigitSum()
