def sum3and5():
   sum = 0
   for i in range(0, 1000):
      if i%3 == 0 or i%5 == 0:
	 print i
	 sum += i
	 
   print sum

sum3and5()
