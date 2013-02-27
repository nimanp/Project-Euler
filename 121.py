from __future__ import division
def prizeFund():
   probWin = []
   numTurns = 4
   for i in range(2, 2+numTurns):
      probWin.append(1/i)

   winningChance = 0
   for i in range(0, len(probWin)-2):
      for j in range(i+1, len(probWin)-1):
	 for k in range(j+1, len(probWin)):
	    winningChance += probWin[i]*probWin[j]*probWin[k]
   winningChance += probWin[0]*probWin[1]*probWin[2]*probWin[3]

   print probWin
   print winningChance

prizeFund()

