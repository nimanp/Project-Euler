from __future__ import division
def bouncyNumbers():
   bouncies = 0
   total = 0
   ratio = 0
   for num in range(1, 2000000):
      if isIncreasing(num) == 0 and isDecreasing(num) == 0:
	 print num
	 bouncies += 1
      total += 1
      ratio = bouncies/total
      if ratio >= 0.99 and num > 1000:
	 print num
	 break
      num += 1
   print ratio

def isIncreasing(num):
   num = str(num)
   flag = 1
   for i in range(0, len(num)-1):
      if int(num[i]) <= int(num[i+1]):
	 continue
      else:
	 flag = 0
	 break
   return flag

def isDecreasing(num):
   num = str(num)
   flag = 1
   for i in range(0, len(num)-1):
      if int(num[i]) >= int(num[i+1]):
	 continue
      else:
	 flag = 0
	 break
   return flag

bouncyNumbers()
