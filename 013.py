def largeSum():
   array = []
   numbers = open("prob13.txt", "r")
   for line in numbers:
      array.append(line)
   for i in range(0, len(array)):
      array[i] = int(array[i])

   sum = 0
   for i in range(0, len(array)):
      sum += array[i]

   print sum

largeSum()
