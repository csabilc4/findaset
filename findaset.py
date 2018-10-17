#!/usr/bin/env python
# coding=utf-8

import random
import itertools
import time
import cards


def getRandomCards(allCardData = {},
				   redeal = False,
				   cardsInSet = (),
				   lastCardNumbersOnTable = [],
				   freeCardsInPack = [],
				   addCards = False):

	'''kiválaszt 12db random lapot a kezdéshez'''

	cardNum = 12
	onTableCardsData = {}

	print '\n'
	print '------------------------------------------------'
	print '--------------------NEW ROUND-------------------'
	print '------------------------------------------------'

	if redeal == False:
		cardsOnTable = random.sample(freeCardsInPack, cardNum)
		# print '\tStart random cards: ', cardsOnTable

		freeCardsInPack = tuple(set(freeCardsInPack) - set(cardsOnTable))
	else:
		# print '\tlast card numbers: ', lastCardNumbersOnTable

		if addCards == False:
			for cc in cardsInSet:
				lastCardNumbersOnTable.remove(cc)

		reducedCardNumbersOnTable = lastCardNumbersOnTable
		# print '\treduced card numbers: ', reducedCardNumbersOnTable

		# print len(freeCardsInPack)
		if len(freeCardsInPack) > 2:
			newCards = random.sample(freeCardsInPack, 3)

		cardsOnTable = reducedCardNumbersOnTable + newCards

		# print '\tnew cards: ', newCards
		# print '\treduced card numbers: ', reducedCardNumbersOnTable
		# print '\tnew cards on table: ', cardsOnTable
		# print '\tset cards: ', cardsInSet

		freeCardsInPack = tuple(set(freeCardsInPack) - set(newCards))

	# get card data
	i = 1
	for c in cardsOnTable:
		onTableCardsData[c] = allCardData[c]
		i += 1

	print 'A pakliban még ' + '{:d}'.format(len(freeCardsInPack)) + ' kártya van,' + \
		' az asztalon lévő kártyák:'

	return onTableCardsData, cardsOnTable, freeCardsInPack


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

	return bFoundSet, currCombi


def checkCards(cardsOnTable):
	'''legenerálja a létező összes 3as kombót az asztalon lévő lapokból, és ezeken csekkolja a SET-eket'''

	for cardNum, values in cardsOnTable.items():
		print '{:2d}'.format(cardNum) + '. számú kártya (' + '{}'.format(', '.join(values)) + ')'
		# time.sleep(0.2)

	print '------------------------------------------------'
	# time.sleep(2)

	allCombination = itertools.combinations(cardsOnTable.keys(), 3)
	for currCombination in allCombination:
		bFoundSet, setCombination = search_intersections_of_3(currCombination,
															  cardsOnTable[currCombination[0]],
															  cardsOnTable[currCombination[1]],
															  cardsOnTable[currCombination[2]])

		if bFoundSet == True:
			print '***SET FOUND***' +  ', kártyák száma: ' + str(setCombination)
			return setCombination

	print 'NO SET FOUND!!! (add 3 more cards to table)'

	return None


def main():
	allCardData = cards.generateAllCardsWithProperties()

	reDeal = False
	addCards = False
	cardsInSet = ()
	lastCardNumbersOnTable = []
	freeCardsInPack = range(1, 81 + 1)

	while len(freeCardsInPack) > 60:
		cardsData, cardsOnTable, freeCardsInPack = getRandomCards(allCardData = allCardData,
																			  redeal = reDeal,
																			  cardsInSet = cardsInSet,
																			  lastCardNumbersOnTable = lastCardNumbersOnTable,
																			  freeCardsInPack = freeCardsInPack,
																			  addCards = addCards)

		# if len(freeCardsInPack) == 0: break

		cardsInSet = checkCards(cardsData)
		reDeal = True
		lastCardNumbersOnTable = cardsOnTable

		if cardsInSet == None:
			addCards = True
		else:
			addCards = False


	#TODO le kell kezelni azt az esetet, ha nincs SET az asztalon, ekkor fel kell rakni még 3 kártyát stb....
	#TODO az utolsó 12 kártyát végig kell járni, az összes SET-et meg kell keresni

if __name__ == '__main__':
	before = time.time()
	main()
	after = time.time()

	print after - before