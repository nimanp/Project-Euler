def concealedSquare():
   for i in range(1010101010, 1389026623):
      square = str(i**2)
      compare = square[0]+square[2]+square[4]+square[6]+square[8]+square[10]+square[12]+square[14]+square[16]+square[18]
      if int(compare) == 1234567890:
	 print square
	 print i

concealedSquare()

