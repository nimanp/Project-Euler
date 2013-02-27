def gridProduct():
   file = open("prob11.txt", "r")
   grid = []
   for line in file:
      grid.append(line)
   for i in range(0, len(grid)):
      grid[i] = int(grid[i])

   max = 0
   for i in range(0, 20): # horizontals
      for j in range(0, 16):
	 prod = grid[20*i+j]*grid[20*i+j+1]*grid[20*i+j+2]*grid[20*i+j+3]
	 if prod > max:
	    max = prod

   for i in range(0, 16): # verticals
      for j in range(0, 20):
	 prod = grid[20*i+j]*grid[20*(i+1)+j]*grid[20*(i+2)+j]*grid[20*(i+3)+j]
	 if prod > max:
	    max = prod

   for i in range(0, 16): # diagonals
      for j in range(0, 16):
	 prod = grid[20*i+j]*grid[20*(i+1)+j+1]*grid[20*(i+2)+j+2]*grid[20*(i+3)+j+3]
	 if prod > max:
	    max = prod

   for i in range(0, 16): # backward diagonals
      for j in range(4, 20):
	 prod = grid[20*i+j]*grid[20*(i+1)+j-1]*grid[20*(i+2)+j-2]*grid[20*(i+3)+j-3]
	 if prod > max:
	    max = prod

   print max

gridProduct()
