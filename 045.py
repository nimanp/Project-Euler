def triPentHex():
   triangular = []
   pentagonal = []
   hexagonal = []
   for i in range(100000):
      triangular.append(i*(i+1)/2)
      pentagonal.append(i*(3*i-1)/2)
      hexagonal.append(i*(2*i-1))
   firstTwo = list(set(triangular).intersection(set(pentagonal)))
   allThree = list(set(firstTwo).intersection(set(hexagonal)))
   print allThree

triPentHex()
