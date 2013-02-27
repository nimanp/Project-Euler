def champernowneConstant():
   leng = counter = 0
   constant = "."
   while leng <= 1000000:
      counter += 1
      constant += str(counter)
      leng += len(str(counter))
   total = 1
   total *= int(constant[1])
   total *= int(constant[10])
   total *= int(constant[100])
   total *= int(constant[1000])
   total *= int(constant[10000])
   total *= int(constant[100000])
   total *= int(constant[1000000])
   print total

champernowneConstant()
