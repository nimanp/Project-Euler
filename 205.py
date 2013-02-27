def diceGame():
   peter = []
   colin = []
   for i in range(1, 5):
      for j in range(1, 5):
	 for k in range(1, 5):
	    for l in range(1, 5):
	       for m in range(1, 5):
		  for n in range(1, 5):
		     for o in range(1, 5):
			for p in range(1, 5):
			   for q in range(1, 5):
			      peter.append(i+j+k+l+m+n+o+p+q)
   for i in range(1, 7):
      for j in range(1, 7):
	 for k in range(1, 7):
	    for l in range(1, 7):
	       for m in range(1, 7):
		  for n in range(1, 7):
		     colin.append(i+j+k+l+m+n)
   peter.sort()
   colin.sort()
   total = wins = 0

   for i in range(0, len(peter)):
      for j in range(0, len(colin)):
	 total += 1
	 if peter[i] > colin[j]:
	    wins += 1

   print wins
   print total
   

diceGame()

