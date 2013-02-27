import math
def digitFactorials():
   sum = 0
   for i in range(0, 10):
      for j in range(0, 10):
	 for k in range(0, 10):
	    for l in range(0, 10):
	       for m in range(0, 10):
		  for n in range(0, 10):
		     for o in range(0, 10):
			digitSum = math.factorial(i) + math.factorial(j) + math.factorial(k) + math.factorial(l) + math.factorial(m) + math.factorial(n) + math.factorial(o)
			if i == 0:
			   digitSum -= 1
			if i == 0 and j == 0:
			   digitSum -= 1
			if i == 0 and j == 0 and k == 0:
			   digitSum -= 1
			if i == 0 and j == 0 and k == 0 and l == 0:
			   digitSum -= 1
			if i == 0 and j == 0 and k == 0 and l == 0 and m == 0:
			   digitSum -= 1
			if i == 0 and j == 0 and k == 0 and l == 0 and m == 0 and n == 0:
			   digitSum -= 1
			num = i*1000000 + j*100000 + k*10000 + l*1000 + m*100 + n*10 + o
			if num == digitSum and num != 1 and num != 2:
			   print num
			   sum += num

digitFactorials()
