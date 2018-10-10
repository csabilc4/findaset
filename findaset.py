#!/usr/bin/env python
# coding=utf-8

import random
import itertools

COLOURS = ['Red', 'Green', 'Purple']
FORMS = ['Elips', 'Amorf', 'Tiles']
FILLS = ['Full', 'Strip', 'Empty']
NUMBERS = ['One', 'Two', 'Three']

def setPackOfCards():
	'''legenerálja a teljes kártyapaklit (81db (3*3*3*3) kártya)'''
	packOfCards = {}
	num = 1

	for colour in COLOURS:
		for form in FORMS:
			for fill in FILLS:
				for number in NUMBERS:
					packOfCards[num] = [colour, form, fill, number]
					num += 1

	return packOfCards


def getRandomCards():
	'''kiválaszt 12db random lapot a kezdéshez'''
	packOfCards = setPackOfCards()

	random_cards = {}
	randomNumbers = random.sample(range(1, 82), 12)

	i = 1
	for c in randomNumbers:
		random_cards[i] = packOfCards[c]
		i += 1

	return random_cards


def search_intersections_of_2(set1, set2):
	'''összhasonlít 2db 3as szettet és veszi a közös tulajdonságokat'''
	return set(set1).intersection(set2)


def search_intersections_of_3(combo, set1, set2, set3):
	'''összhasonlítja a 3as szetteket hármasával:
	SET, ha:
	-3 tulajdonság megegyezik vagy,
	-2 tulajdonság megegyezik vagy,
	-nincs egyező tulajdonság
	'''

	sum_12 = search_intersections_of_2(set1, set2)
	sum_13 = search_intersections_of_2(set1, set3)
	sum_23 = search_intersections_of_2(set2, set3)

	bFoundSet = False
	if sum_12 == sum_13 and sum_12 == sum_23 and sum_12 != 1:
		bFoundSet = True

	if bFoundSet == True:
		print 'SET!!!', combo	#, sum_12, sum_13, sum_23


def checkCards(cardsInTable):
	'''generálja a létező összes 3as kombót a 12db lapból, és ezeket csekkolja'''

	for cardNum, values in cardsInTable.items():
		# print cardNum, values
		print str(cardNum) + '.számú kártya: ' + ', '.join(values)

	result = itertools.combinations(cardsInTable.keys(), 3)
	for combo in result:
		search_intersections_of_3(combo, cardsInTable[combo[0]], cardsInTable[combo[1]], cardsInTable[combo[2]])


def main():
	checkCards(getRandomCards())


if __name__ == '__main__':
	main()


