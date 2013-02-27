def fibThousand():
   next = 0
   cur = 1
   prev = 1
   for i in range(0, 20000):
      next = cur + prev
      prev = cur
      cur = next
      if len(str(next)) >= 1000:
	 return i+3

answer = fibThousand()
print answer
