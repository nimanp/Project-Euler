def collatzSeq(n):
   maxMoves = maxIndex = 0
   for i in range(n, 1, -1):
      curNum = i
      count = 0
      while curNum > 1:
	 count += 1
	 if curNum%2 == 0:
	    curNum = curNum/2
	 else:
	    curNum = 3*curNum + 1
      if count > maxMoves:
	 maxMoves = count
	 maxIndex = i
   print maxMoves
   print maxIndex

collatzSeq(1000000)
