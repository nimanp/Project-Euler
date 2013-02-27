import math
choices = 0
for i in range(0, 21):
   choices += ((math.factorial(20))/(math.factorial(i)*math.factorial(20-i)))**2
print choices
