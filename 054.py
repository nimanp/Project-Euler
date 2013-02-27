def pokerHands():
   winCount = 0
   hands = []
   file = open('prob54.txt', 'r')
   for line in file:
      hands.append(line[:len(line)-1])

   for i in range(len(hands)):
      hand1 = winningHand(hands[i][:len(hands[i])/2])
      hand2 = winningHand(hands[i][len(hands[i])/2+1:])
      if hand1 > hand2:
	 winCount += 1
	 print hands[i][:len(hands[i])/2]
	 print hands[i][len(hands[i])/2+1:]
   print winCount

def winningHand(hands):
   cards = hands.split()
   values = []
   suits = []
   for i in range(len(cards)):
      if cards[i][0] == 'T':
	 values.append(10)
      elif cards[i][0] == 'J':
	 values.append(11)
      elif cards[i][0] == 'Q':
	 values.append(12)
      elif cards[i][0] == 'K':
	 values.append(13)
      elif cards[i][0] == 'A':
	 values.append(14)
      else:
	 values.append(int(cards[i][0]))
      suits.append(cards[i][1])

   values.sort()
   suits.sort()
   
   #straight flush
   if values[4] == values[3]+1 and values[3] == values[2]+1 and values[2] == values[1]+1 and values[1] == values[0]+1 and suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]:
      return 5000+values[4]
   if values[4] == 14 and values[3] == 5 and values[2] == 4 and values[1] == 3 and values[0] == 2 and suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]:
      return 5000+values[3]

   #four of a kind
   if values[0] == values[3] or values[1] == values[4]:
      return 4500+values[4]

   #full house
   if values[0] == values[1] and values[2] == values[4]:
      return 4000+values[4]
   if values[0] == values[2] and values[3] == values[4]:
      return 4000+values[4]

   #flush
   if suits[0] == suits[1] and suits[0] == suits[2] and suits[0] == suits[3] and suits[0] == suits[4]:
      return 3500+values[4]

   #straight
   if values[4] == values[3]+1 and values[3] == values[2]+1 and values[2] == values[1]+1 and values[1] == values[0]+1:
      return 3000+values[4]
   if values[4] == 14 and values[3] == 5 and values[2] == 4 and values[1] == 3 and values[0] == 2:
      return 3000+values[3]

   #three of a kind
   if values[0] == values[2]:
      return 2900+values[2]
   if values[1] == values[3]:
      return 2900+values[3]
   if values[2] == values[4]:
      return 2900+values[4]

   #twopair
   if values[0] == values[1] and values[2] == values[3]:
      return 200+169*values[3]+13*values[1]+values[4]
   if values[0] == values[1] and values[3] == values[4]:
      return 200+169*values[4]+13*values[1]+values[2]
   if values[1] == values[2] and values[3] == values[4]:
      return 200+169*values[4]+13*values[2]+values[0]

   #pair
   for i in range(len(values)-1):
      if values[i] == values[i+1]:
	 return 15+13*values[i]+values[4]

   #high card
   return values[4]
   
pokerHands()

