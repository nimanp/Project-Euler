def letterCounter():
   numLetters = 0
   #ones - nines
   numLetters += 9*10*3
   numLetters += 9*10*3
   numLetters += 9*10*5
   numLetters += 9*10*4
   numLetters += 9*10*4
   numLetters += 9*10*3
   numLetters += 9*10*5
   numLetters += 9*10*5
   numLetters += 9*10*4
   #teens
   numLetters += 30
   numLetters += 60
   numLetters += 60
   numLetters += 80
   numLetters += 80
   numLetters += 70
   numLetters += 70
   numLetters += 90
   numLetters += 80
   numLetters += 80
   #twenties-nineties
   numLetters += 100*6
   numLetters += 100*6
   numLetters += 100*5
   numLetters += 100*5
   numLetters += 100*5
   numLetters += 100*7
   numLetters += 100*6
   numLetters += 100*6
   #hundreds
   numLetters += (7*900)
   numLetters += (300)
   numLetters += 300
   numLetters += 500
   numLetters += 400
   numLetters += 400
   numLetters += 300
   numLetters += 500
   numLetters += 500
   numLetters += 400

   numLetters += 11
   numLetters += 3*(99*9)
   print numLetters

letterCounter()

