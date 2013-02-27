def digitFifthPowers():
   sum = 0
   for i in range(2, 1000000):
      stringNum = 0
      digitSum = 0
      for j in range(0, len(str(i))):
	 digitSum += int(str(i)[j])**5
      
      if digitSum == i:
	 sum += i
   print sum

digitFifthPowers()
