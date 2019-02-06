#!/usr/bin/env python
# coding=utf-8

import random
import itertools
import time
import cards
import cProfile, pstats, io
import PIL.Image
import PIL.ImageFilter
# from PIL import Image
import sys
import os

print PIL.Image.BOX

#pylint: disable=mixed-indentation
#pylint: disable=bad-continuation
#pylint: disable=invalid-name
#pylint: disable=dangerous-default-value
#pylint: disable=missing-docstring
#pylint: disable=bad-whitespace
#pylint: disable=wrong-import-order

PICTS_DIR_PATH = os.path.join(os.getcwd(), 'cards')

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

    if redeal is False:
        cardsOnTable = random.sample(freeCardsInPack, cardNum)
        # print '\tStart random cards: ', cardsOnTable

        freeCardsInPack = tuple(set(freeCardsInPack) - set(cardsOnTable))
    else:
        # print '\tlast card numbers: ', lastCardNumbersOnTable

        if addCards is False:
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

    print 'A pakliban meg ' + '{:d}'.format(len(freeCardsInPack)) + ' kartya van,' + \
          ' az asztalon levo kartyak:'

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

    cardsOnTablePictName = []
    for cardNum, values in cardsOnTable.items():
        # print '{:2d}'.format(cardNum) + '. szamu kartya (' + '{}'.format(', '.join(values)) + ')'
        cardsOnTablePictName.append(values[0] + '_' + values[1] + '_'  + values[2] + '_' + values[3])
        # print cardPictName
        # TODO ki kell rakni az asztalra a kártyák képeit
        # TODO meg kell valahogy jelölni a SET kártyáit (szines körvonal???)


    print '------------------------------------------------'
    # time.sleep(2)

    allCombination = itertools.combinations(cardsOnTable.keys(), 3)

    cardsOnTablePictName = []
    for cardNum, values in cardsOnTable.items():
        cardsOnTablePictName.append(values[0] + '_' + values[1] + '_'  + values[2] + '_' + values[3])

    cardPictsNamesWithSet = []
    for currCombination in allCombination:
        # print currCombination

        bFoundSet, setCombination = search_intersections_of_3(currCombination,
                                                              cardsOnTable[currCombination[0]],
                                                              cardsOnTable[currCombination[1]],
                                                              cardsOnTable[currCombination[2]])

        if bFoundSet:
            print '***SET FOUND***' +  ', kartyak szama: ' + str(setCombination)
            print setCombination[0], cardsOnTable[setCombination[0]]
            print setCombination[1], cardsOnTable[setCombination[1]]
            print setCombination[2], cardsOnTable[setCombination[2]]

            for i in range(3):
                cardPictsNamesWithSet.append(cardsOnTable[setCombination[i]][0] + '_' +
                                             cardsOnTable[setCombination[i]][1] + '_' +
                                             cardsOnTable[setCombination[i]][2] + '_' +
                                             cardsOnTable[setCombination[i]][3])

            drawCardsWithSet(cardsOnTablePictName, cardPictsNamesWithSet)

            return setCombination

    print 'NO SET FOUND!!! (add 3 more cards to table)'
    return None


def drawCardsWithSet(cardsOnTablePictName, cardPictsNamesWithSet):

    pict_width = 194
    pict_height = 108
    new_pict = PIL.Image.new(mode = 'RGB', size=(pict_width * 4, pict_height * 3))

    # print cardPictsNamesWithSet

    for i, table_pict in enumerate(cardsOnTablePictName):
        pictName = table_pict + '.png'
        pictPath = os.path.join(PICTS_DIR_PATH, pictName)
        orig_pict = PIL.Image.open(pictPath)
        copy_pict = orig_pict.copy()

        # highlight set cards
        bResizePict = False
        if table_pict in cardPictsNamesWithSet:
            # mod_pict = copy_pict.filter(PIL.ImageFilter.CONTOUR)
            mod_pict = copy_pict
        else:
            # mod_pict = copy_pict.convert(mode = '1')
            bResizePict = True
            mod_pict = copy_pict.resize((pict_width / 2 , pict_height / 2))

        pictPosX = (i % 4) * pict_width + pict_width / 4 * bResizePict
        pictPosY = ((i - (i % 4)) / 4) * pict_height + pict_height / 4 * bResizePict
        # print table_pict
        new_pict.paste(mod_pict, box = (pictPosX, pictPosY))

    new_pict.show()

    # TODO copyzom a curr képet és betolom a newPict-be, startpos a left-top corner
    # TODO kell a kép mérete pixelben az eltoláshoz
    # new_pict.paste(copy_pict)
    # pictPath = os.path.join(PICTS_DIR_PATH, pictName)
    # # print pictPath
    # # pict = PIL.Image.Image()
    # orig_pict = PIL.Image.open(pictPath)
    # copy_pict = orig_pict.copy()


def main():
    allCardData = cards.generateAllCardsWithProperties()

    # print PICTS_DIR_PATH

    reDeal = False
    addCards = False
    cardsInSet = ()
    lastCardNumbersOnTable = []
    freeCardsInPack = range(1, 81 + 1)

    while len(freeCardsInPack) > 70:
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

        if cardsInSet is None:
            addCards = True
        else:
            addCards = False


#TODO le kell kezelni azt az esetet, ha nincs SET az asztalon, ekkor fel kell rakni még 3 kártyát stb....
#TODO az utolsó 12 kártyát végig kell járni, az összes SET-et meg kell keresni

if __name__ == '__main__':
    # before = time.time()
    main()
# after = time.time()

# print after - before
