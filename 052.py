def permutedMultiples():
   flag = 0
   num = 1
   while flag == 0:
      i = int("".join(sorted(str(num))))
      a = int("".join(sorted(str(num*2))))
      b = int("".join(sorted(str(num*3))))
      c = int("".join(sorted(str(num*4))))
      d = int("".join(sorted(str(num*5))))
      e = int("".join(sorted(str(num*6))))
      if i == a and i == b and i == c and i == d and i == e:
	 flag = 1
      num += 1
   print num


permutedMultiples()      
