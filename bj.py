"""
This is BlackJack!
"""
# good luck

import random
# to generate random numbers

currentDeck = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
 "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
 "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
 "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"]
# deck of new cards

currentValue = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
""" 
deck of card's value
have flag for every subtraction, maxing out at the number of aces
"""

useDeck = []
useValue = []
# pile of used cards

def dealing(currentDeck, currentValue, useDeck, useValue):
	randomnumber = random.randrange(0, len(currentDeck)-1)
	# ramdom number between 0 to number of cards
	global card
	card = currentDeck[randomnumber]
	# card from random position
	global value
	value = currentValue[randomnumber]
	# value from random position
	currentDeck.pop(randomnumber)
	# takes out one card from picked position
	currentValue.pop(randomnumber)
	# takes out one value from picked position
	useDeck.append(card)
	# adds card into used pile
	useValue.append(value)
	# adds value into used pile


def acehole(deck, value):
	if value > 21:
	# if total is over 21
		if 11 in deck:
		# searches all in deck
			deck.remove(11)
			deck.append(1)
			# take out 11 and enter 1
			return value - 10
		# if there is an ace, it becomes 1
		else:
			return value
	else:
		return value


def wol(value):
	if value == 21:
		print("Winner Winner Chicken Dinner")
		return 1
		# blackjack!
	elif value > 21:
		print("Loser Loser Doggy Lover")
		return 1
		# bust!
	else:
		return 0
# compares my value if win or lost and returns flag

def wold(value):
	if value == 21:
		print("Loser Loser Doggy Lover")
		return 1
		# blackjack
	elif value > 21:
		print("Winner Winner Chicken Dinner")
		return 1
		# bust
	else:
		return 0
# compares dealer's value if win or lost and returns flag


play = 0
while play == 0 and len(currentDeck) > 17:

	dealerDeck = []
	dDeckValue = []
	dealerValue = 0
	# dealer
	myDeck = []
	mDeckValue = []
	myValue = 0
	# me

	for x in range(2):
		dealing(currentDeck, currentValue, useDeck, useValue)
		dealerDeck.append(card)
		dDeckValue.append(value)
		dealerValue = dealerValue + value
		
		dc = "Dealer's cards: {}"
		print(dc.format(dealerDeck))
		dv = "Dealer's value: {}"
		print(dv.format(dealerValue))
		# displays dealers cards and value
		
		dealerValue = acehole(dDeckValue, dealerValue)
	# deals two random cards to dealer's lists and calculates value

	for x in range(2):
		dealing(currentDeck, currentValue, useDeck, useValue)
		myDeck.append(card)
		mDeckValue.append(value)
		myValue = myValue + value
		
		mc = "Your cards: {}"
		print(mc.format(myDeck))
		mv = "My value: {}"
		print(mv.format(myValue))
		# displays my cards and value
		
		myValue = acehole(mDeckValue, myValue)
	# deals two random cards to my list and adds value

	"""
	dc = "Dealer's cards: {}"
	print(dc.format(dealerDeck[0]))
	dv = "Dealer's value: {}"
	print(dv.format(dealerValue))
	# displays dealers cards and value
	mc = "Your cards: {}"
	print(mc.format(myDeck))
	mv = "My value: {}"
	print(mv.format(myValue))
	# displays my cards and value
	"""

	flag = wol(myValue)
	# checks value for win or loss
	if flag == 0:
	# continues when no blackjack or bust
		hitstand = input("Hit(h) or Stand(s): ")
		# user acts to hit or stand 
		while hitstand == "h":
			dealing(currentDeck, currentValue, useDeck, useValue)
			myDeck.append(card)
			mDeckValue.append(value)
			myValue = myValue + value
			myValue = acehole(mDeckValue, myValue)
			# deals another card and calculates value
			mc = "Your cards: {}"
			print(mc.format(myDeck))
			mv = "My value: {}"
			print(mv.format(myValue))
			# shows current cards and value
			flag = wol(myValue)
			# compares current value
			if flag == 1:
				break
			hitstand = input("Hit(h) or Stand(s): ")
			# waits for input

	if myValue <= 21:
		dflag = wold(dealerValue)
		# checks value for win or loss
		dc = "Dealer's cards: {}"
		print(dc.format(dealerDeck))
		dv = "Dealer's value: {}"
		print(dv.format(dealerValue))
		# displays dealers cards and value
		if dflag == 0:
		# continues when no blackjack or bust
			while dealerValue < 17:
				dealing(currentDeck, currentValue, useDeck, useValue)
				dealerDeck.append(card)
				dDeckValue.append(value)
				dealerValue = dealerValue + value
				dealerValue = acehole(dDeckValue, dealerValue)
				# deals another card and adds value
				dc = "Dealer's cards: {}"
				print(dc.format(dealerDeck))
				dv = "Dealer's value: {}"
				print(dv.format(dealerValue))
				# displays dealers cards and value
				dflag = wold(dealerValue)
				# compares current value


	if myValue < 21 and dealerValue <21:
		if myValue == dealerValue:
			print("No Dinner, No Lover")
		# if same value, no win and no loss
		elif myValue > dealerValue:
			print("Winner Winner Chicken Dinner")
		# if i am closer to 21
		elif myValue < dealerValue:
			print("Loser Loser Doggy Lover")
		# if dealer is closer to 21
		else:
			print("weird")
			
	game = input("Another game? (y or n) ")
	if game == "y":
		play = 0
	else:
		play = 1