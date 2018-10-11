#!/usr/bin/env python
# coding=utf-8

import random
import itertools
import time

COLOURS = ['Red', 'Green', 'Purple']
FORMS = ['Elips', 'Amorf', 'Tiles']
FILLS = ['Full', 'Strip', 'Empty']
NUMBERS = ['One', 'Two', 'Three']

def generateAllCardsWithProperties():
	'''legenerálja a teljes kártyapaklit (81db (3*3*3*3) kártya)'''
	allCardData = {}
	num = 1

	for colour in COLOURS:
		for form in FORMS:
			for fill in FILLS:
				for number in NUMBERS:
					allCardData[num] = [colour, form, fill, number]
					num += 1

	return allCardData


def getRandomCards(allCardData = {}, redeal = False, cardsOfSet = (), lastCardNumbersOnTable = []):
	'''kiválaszt 12db random lapot a kezdéshez'''

	cardNum = 12
	variation = 3**4
	random_cards = {}

	if redeal == False:
		randomCardNumbersOnTable = random.sample(range(1, variation + 1), cardNum)

		print 'random cards: ', randomCardNumbersOnTable
	else:
		print '\tlast card numbers: ', lastCardNumbersOnTable

		reCalcPack()

		lastFreeCards = range(1, variation + 1)
		# freeCardsInPack = tuple(set(range(1, variation + 1)) - set(lastCardNumbersOnTable))
		freeCardsInPack = tuple(set(lastFreeCards) - set(lastCardNumbersOnTable))
		print len(freeCardsInPack), 'db különbség: ', freeCardsInPack

		for cc in cardsOfSet:
			lastCardNumbersOnTable.remove(cc)
		reducedCardNumbersOnTable = lastCardNumbersOnTable
		# print '\treduced card numbers: ', reducedCardNumbersOnTable

		newCards = random.sample(freeCardsInPack, 3)
		print '\tnew cards: ', newCards
		print '\treduced card numbers: ', reducedCardNumbersOnTable

		randomCardNumbersOnTable = reducedCardNumbersOnTable + newCards

		# print '\tset kártyái:', cardsOfSet
		print '\tnew random cards: ', randomCardNumbersOnTable

	i = 1
	for c in randomCardNumbersOnTable:
		random_cards[c] = allCardData[c]
		i += 1

	# print random_cards
	return random_cards, randomCardNumbersOnTable


def reCalcPack():
	pass


def search_intersections_of_2(set1, set2):
	'''összhasonlít 2db 3as szettet és veszi a közös tulajdonságokat'''
	return set(set1).intersection(set2)


def search_intersections_of_3(currCombi, set1, set2, set3):
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
		print 'SET FOUND!!!', currCombi	#, sum_12, sum_13, sum_23

	return bFoundSet, currCombi


def checkCards(cardsOnTable):
	'''generálja a létező összes 3as kombót a 12db lapból, és ezeket csekkolja'''

	for cardNum, values in cardsOnTable.items():
		# print cardNum, values
		# print str(cardNum) + '.számú kártya: ' + ', '.join(values)
		# time.sleep(0.1)
		pass

	allCombination = itertools.combinations(cardsOnTable.keys(), 3)
	for currCombination in allCombination:
		bFoundSet, setCombination = search_intersections_of_3(currCombination,
															  cardsOnTable[currCombination[0]],
															  cardsOnTable[currCombination[1]],
															  cardsOnTable[currCombination[2]])
		if bFoundSet == True:
			# break
			return setCombination
			# getRandomCards()

	return None

def main():
	allCardData = generateAllCardsWithProperties()

	reDeal = False
	noMoreCards = True
	setCombi = None
	cardsOfSet = ()
	lastCardNumbersOnTable = []

	for t in range(4):
		cardsData, randomCardNumbersOnTable = getRandomCards(allCardData = allCardData,
															 redeal = reDeal,
															 cardsOfSet = cardsOfSet,
															 lastCardNumbersOnTable = lastCardNumbersOnTable)

		setCombi = checkCards(cardsData)
		if setCombi != None:
			reDeal = True
			# print setCombi
			cardsOfSet = setCombi
			lastCardNumbersOnTable = randomCardNumbersOnTable

	# if setCombi:
	# 	print setCombi
	# else:
	# 	print 'Nincs SET!'

	# reDeal = False
	# noMoreCards = True
	# while 1:
	# 	getRandomCards(redeal = False)
	# 	setCombi = checkCards(getRandomCards(redeal = reDeal))
	# 	if setCombi:
	# 		reDeal = True
	#
	# 	if noMoreCards == True:
	# 		break
	#
	# if setCombi:
	# 	print setCombi
	# else:
	# 	print 'Nincs SET!'


if __name__ == '__main__':
	main()


