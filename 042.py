def triangleNums(file):
   f = open(file, "r")
   words = f.read()
   newWords = words.split(",")
   f.close()
   #Find which numbers are triangle numbers
   numTriangles = 0
   for i in range(len(newWords)):
      score = 0
      for j in range(1, len(newWords[i])-1):
	 score = score + (ord(newWords[i][j]) - 64)
      #Determine whether it's a triangle word
      for k in range(25):
	 if score == ((k)*(k + 1) / 2):
	    numTriangles = numTriangles + 1
	    break
   print numTriangles

triangleNums("prob40.txt")
