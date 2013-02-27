def coinSums(amount):
   if amount == 0:
      global possibilities
      possibilities += 1
   if amount >= 200:
      coinSums(amount-200)
   if amount >= 100:
      coinSums(amount-100)
   if amount >= 50:
      coinSums(amount-50)
   if amount >= 20:
      coinSums(amount-20)
   if amount >= 10:
      coinSums(amount-10)
   if amount >= 5:
      coinSums(amount-5)
   if amount >= 2:
      coinSums(amount-2)
   if amount >= 1:
      coinSums(amount-1)

possibilities = 0
coinSums(10)
print possibilities
