#!/usr/bin/env python
# coding=utf-8

import random
import itertools
import time


class Cards:

	def __init__(self):
		self.COLOURS = ['Red', 'Green', 'Purple']
		self.FORMS = ['Elips', 'Amorf', 'Tiles']
		self.FILLS = ['Full', 'Strip', 'Empty']
		self.NUMBERS = ['One', 'Two', 'Three']

	def generateAllCardsWithData(self):
		'''legenerálja a teljes kártyapaklit (81db (3*3*3*3) kártya)'''
		allCardWithData = {}
		num = 1

		for colour in self.COLOURS:
			for form in self.FORMS:
				for fill in self.FILLS:
					for number in self.NUMBERS:
						allCardWithData[num] = [colour, form, fill, number]
						num += 1

		return allCardWithData


class RandomCards:

	def __init__(self, allCardWithData):
		self.cardNum = 12
		self.allCardWithData = allCardWithData
		self.onTableCardsData = {}
		self.cardsInSet = ()
		self.lastCardNumbersOnTable = []
		self.freeCardsInPack = range(1, 81 + 1)
		self.addCards = False
		self.redeal = False


	def cardDealer(self):

		cardsOnTable = random.sample(self.freeCardsInPack, self.cardNum)
		print '\tStart random cards: ', cardsOnTable

		freeCardsInPack = tuple(set(self.freeCardsInPack) - set(cardsOnTable))
		# return self.freeCardsInPack, cardsOnTable
		return freeCardsInPack, cardsOnTable


	def cardRemover(self, addCards, cardsInSet, lastCardNumbersOnTable):
		# print '\tlast card numbers: ', lastCardNumbersOnTable

		if addCards == False:  # ha volt SET, akkor leveszi az asztalról a megtalált SET kártyáit
			for cc in cardsInSet:
				lastCardNumbersOnTable.remove(cc)

		reducedCardNumbersOnTable = lastCardNumbersOnTable
		# print '\treduced card numbers: ', reducedCardNumbersOnTable

		return reducedCardNumbersOnTable


	def cardAdder(self, freeCardsInPack, reducedCardNumbersOnTable):
		# print len(freeCardsInPack)

		if len(freeCardsInPack) > 2:  # ha van még a pakliban kártya, akkor leoszt 3 kártyát az asztalra
			newCards = random.sample(freeCardsInPack, 3)

		cardsOnTable = reducedCardNumbersOnTable + newCards

		# print '\tnew cards: ', newCards
		# print '\treduced card numbers: ', reducedCardNumbersOnTable
		# print '\tnew cards on table: ', cardsOnTable
		# print '\tset cards: ', cardsInSet

		freeCardsInPack = tuple(set(freeCardsInPack) - set(newCards))
		return freeCardsInPack, cardsOnTable


	def getOnTableCardsData(self, cardsOnTable):

		# print cardsOnTable
		# get card data
		i = 1
		for c in cardsOnTable:
			self.onTableCardsData[c] = self.allCardWithData[c]
			i += 1

		# print '\tnumber of free cards in pack: ', len(freeCardsInPack)
		return self.onTableCardsData, cardsOnTable
		# print self.onTableCardsData


def checkCards(cardsOnTable):
	'''legenerálja a létező összes 3as kombót az asztalon lévő lapokból, és ezeken csekkolja a SET-eket'''

	bFoundSet = False

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
		pass

	print 'NO SET FOUND!!! (add 3 more cards to table)'


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


def main():

	allCards = Cards()
	allCardWithData = allCards.generateAllCardsWithData()

	randomCards = RandomCards(allCardWithData)
	# randomCards.cardDealer()

	freeCardsInPack = range(1, 81 + 1)

	while len(freeCardsInPack) > 60:
		# onTableCardsData, cardsData, freeCardsInPack = randomCards.getOnTableCardsData(randomCards.cardDealer())
		onTableCardsData, cardsData = randomCards.getOnTableCardsData(randomCards.cardDealer())

		cardsInSet = checkCards(onTableCardsData)
		lastCardNumbersOnTable = cardsOnTable

		if cardsInSet == None:
			addCards = True
		else:
			addCards = False






if __name__ == '__main__':
	before = time.time()
	main()
	after = time.time()

	print after - before








class val:

	def getRandomCards(self,
					   allCardData = {},
					   redeal = False,
					   cardsInSet = (),
					   lastCardNumbersOnTable = [],
					   freeCardsInPack = [],
					   addCards = False):



		print '------------------------------------------------'
		print '--------------------NEW ROUND-------------------'
		print '------------------------------------------------'

		if redeal == False:		#kiválaszt 12db random lapot a kezdéshez
			cardsOnTable = random.sample(freeCardsInPack, cardNum)
			# print '\tStart random cards: ', cardsOnTable

			freeCardsInPack = tuple(set(freeCardsInPack) - set(cardsOnTable))
		else:
			# print '\tlast card numbers: ', lastCardNumbersOnTable

			if addCards == False:	#ha volt SET, akkor leveszi az asztalról a megtalált SET kártyáit
				for cc in cardsInSet:
					lastCardNumbersOnTable.remove(cc)

			reducedCardNumbersOnTable = lastCardNumbersOnTable
			# print '\treduced card numbers: ', reducedCardNumbersOnTable

			# print len(freeCardsInPack)
			if len(freeCardsInPack) > 2:	#ha van még a pakliban kártya, akkor leoszt 3 kártyát az asztalra
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

		print '\tnumber of free cards in pack: ', len(freeCardsInPack)
		return onTableCardsData, cardsOnTable, freeCardsInPack
