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

	def __init__(self):
		self.cardNum = 12
		self.onTableCardsData = {}

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

		if redeal == False:		# kiválaszt 12db random lapot a kezdéshez
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

		print '\tnumber of free cards in pack: ', len(freeCardsInPack)
		return onTableCardsData, cardsOnTable, freeCardsInPack

def main():

	allCards = Cards()
	allCardWithData = allCards.generateAllCardsWithData()




	# print allCardWithData

	pass


if __name__ == '__main__':
	before = time.time()
	main()
	after = time.time()

	print after - before