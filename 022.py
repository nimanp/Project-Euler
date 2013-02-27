def nameScores(file):
   f = open(file, "r")
   list = f.read()
   newList = list.split(",")
   newList.sort()
   f.close()
   #Calculate scores and add them together
   totalScore = 0
   for i in range(0, len(newList)):
      score = 0
      if i < 100:
	 print newList[i]
      for j in range(1, len(newList[i])-1):
	 score += (ord(newList[i][j]))
	 score -= 64
      totalScore += (score * (i+1))
   print totalScore

nameScores("prob22.txt")
