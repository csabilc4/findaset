#!/usr/bin/env python
# coding=utf-8

import random
import itertools

# shapes = ['1',
# 		  '2',
# 		  '3',
# 		  '4',
# 		  '5',
# 		  '6',
# 		  '7',
# 		  '8',
# 		  '9',
# 		  '10',
# 		  '11',
# 		  '12',
# 		  ]
# result = itertools.combinations(shapes, 3)
# for each in result:
#     print(each)
#
# exit()

COLOURS = [
	'Red',
	'Green',
	'Purple'
]

FORMS = [
	'Elips',
	'Amorf',
	'Tiles'
]

FILLS = [
	'Full',
	'Strip',
	'Empty'
]

NUMBERS = [
	'One',
	'Two',
	'Three'
]




class Cards(object):
	def __init__(self, colour, fill, form, number):
		self.colour = colour
		self.fill = fill
		self.form = form
		self.number = number

	def randomChoice(self):
		random.choice(COLOURS)



def setPackOfCards():
	packOfCards = {}
	num = 1

	for colour in COLOURS:
		for form in FORMS:
			for fill in FILLS:
				for number in NUMBERS:
					packOfCards[num] = [colour, form, fill, number]
					num += 1

	return packOfCards
	# print packOfCards

# setPackOfCards()
# exit()

def getRandomCards():
	packOfCards = setPackOfCards()
	# print packOfCards

	random_cards = {}
	randomNumbers = random.sample(range(1, 82), 12)
	# print randomNumbers

	i = 1
	for c in randomNumbers:
		random_cards[i] = packOfCards[c]
		i += 1

	# for c in range(1, 13):
	# 	randomCardPropertys = [random.choice(COLOURS), \
	# 						   random.choice(FORMS), \
	# 						   random.choice(FILLS), \
	# 						   random.choice(NUMBERS)]
	#
	# 	random_cards[c] = randomCardPropertys
	# print c, cards[c]


	return random_cards
	# print random_cards

# getRandomCards()
# exit()

def checkCards(cardsInTable):
	# print cardsInTable.keys()
	# print cardsInTable.values()

	for cardNum, values in cardsInTable.items():
		print cardNum, values
		pass

	result = itertools.combinations(cardsInTable.keys(), 3)
	for each in result:
		# print each[0], type(each)
		# sum = len(set(cardsInTable[each[0]] + cardsInTable[each[1]] + cardsInTable[each[2]]))
		# print each, cardsInTable[each[0]], cardsInTable[each[1]], cardsInTable[each[2]]
		# print search_intersections(cardsInTable[each[0]], cardsInTable[each[1]])

		search_intersections_of_3(each, cardsInTable[each[0]], cardsInTable[each[1]], cardsInTable[each[2]])
		if sum == 6 or sum == 8 or sum == 12:
			# print sum, 'SET!!!'
			pass

def search_intersections_of_2(set1, set2):

	return set(set1).intersection(set2)

def search_intersections_of_3(combo, set1, set2, set3):

	sum_12 = search_intersections_of_2(set1, set2)
	sum_13 = search_intersections_of_2(set1, set3)
	sum_23 = search_intersections_of_2(set2, set3)

	# print sum_12, sum_13, sum_23

	bFoundSet = False
	if sum_12 == sum_13 and sum_12 == sum_23 and sum_12 != 1:
		bFoundSet = True

	if bFoundSet == True:
		print 'SET!!!', combo, sum_12, sum_13, sum_23


checkCards(getRandomCards())


exit()







list1 = ['Green', 'Elips', 'Empty', 'Three']
list2 = ['Blue', 'Tiles', 'Strip', 'One']
list3 = ['Yellow', 'Amorf', 'Full', 'Two']

sum = set(list1 + list2 + list3)
# print len(sum)

list4 = ['Green', 'Elips', 'Full', 'Three']
list5 = ['Green', 'Elips', 'Full', 'One']
list6 = ['Green', 'Elips', 'Full', 'Two']

# sum2 = set(list4 + list5 + list6)
sum2 =set(list4).intersection(list5)
print sum2
# print len(sum2), sum2

# 12db random kártyát kell generálni a pakliból, egyedinek kell lenniük
# fel kell írni az összes 3-as kombinációt a 12 lapból pl. 123, 124, 125, 129, 267
# meg kell vizsgálnia a tulajdonságaikat:
# set:
# -ha 3 tulajd. megegyezik (ha set-be rakom őket és a len(set) = 6)
# -ha pontosan 2 tulajd. megegyezik (ha set-be rakom őket és a len(set) = 6)
# -ha nincs egyező tulajd. (ha set-be rakom őket és a len(set) = 12)


redFullElipsOne = Cards('red', 'full', 'elips', 'one')
greenFullElipsOne = Cards('green', 'full', 'elips', 'one')
purpleFullElipsOne = Cards('purple', 'full', 'elips', 'one')

redStripElipsOne = Cards('red', 'strip', 'elips', 'one')
greenStripElipsOne = Cards('green', 'strip', 'elips', 'one')
purpleStripElipsOne = Cards('purple', 'strip', 'elips', 'one')

redEmptyElipsOne = Cards('red', 'empty', 'elips', 'one')
greenEmptyElipsOne = Cards('green', 'empty', 'elips', 'one')
purpleEmptyElipsOne = Cards('purple', 'empty', 'elips', 'one')

redFullAmorfOne = Cards('red', 'full', 'Amorf', 'one')
greenFullAmorfOne = Cards('green', 'full', 'Amorf', 'one')
purpleFullAmorfOne = Cards('purple', 'full', 'Amorf', 'one')

redStripAmorfOne = Cards('red', 'strip', 'Amorf', 'one')
greenStripAmorfOne = Cards('green', 'strip', 'Amorf', 'one')
purpleStripAmorfOne = Cards('purple', 'strip', 'Amorf', 'one')

redEmptyAmorfOne = Cards('red', 'empty', 'Amorf', 'one')
greenEmptyAmorfOne = Cards('green', 'empty', 'Amorf', 'one')
purpleEmptyAmorfOne = Cards('purple', 'empty', 'Amorf', 'one')

redFullTilesOne = Cards('red', 'full', 'Tiles', 'one')
greenFullTilesOne = Cards('green', 'full', 'Tiles', 'one')
purpleFullTilesOne = Cards('purple', 'full', 'Tiles', 'one')

redStripTilesOne = Cards('red', 'strip', 'Tiles', 'one')
greenStripTilesOne = Cards('green', 'strip', 'Tiles', 'one')
purpleStripTilesOne = Cards('purple', 'strip', 'Tiles', 'one')

redEmptyTilesOne = Cards('red', 'empty', 'Tiles', 'one')
greenEmptyTilesOne = Cards('green', 'empty', 'Tiles', 'one')
purpleEmptyTilesOne = Cards('purple', 'empty', 'Tiles', 'one')


def mix():
	'''random kiválaszt kártáykat'''

	return random.choice(0, 1)

	pass
