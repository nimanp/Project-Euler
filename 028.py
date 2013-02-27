def spiralDiagonals():
   sum = 1
   incrementer = 3
   for i in range(2, 1001, 2):
      for j in range(0, 3):
	 sum += incrementer
	 incrementer += i
      sum += incrementer
      incrementer += (i+2)

   print sum

spiralDiagonals()
      
