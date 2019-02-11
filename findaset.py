#!/usr/bin/env python
# coding=utf-8

import random
import itertools
import time
import cards
import PIL.Image
import PIL.ImageFilter
import PIL.ImageDraw
import PIL.ImageFont
import PIL.ImageEnhance

import sys
import os
import pyautogui
import copy

# print pyautogui.locateOnScreen('snip.jpg')

# exit()

#pylint: disable=mixed-indentation
#pylint: disable=bad-continuation
#pylint: disable=invalid-name
#pylint: disable=dangerous-default-value
#pylint: disable=missing-docstring
#pylint: disable=bad-whitespace
#pylint: disable=wrong-import-order



TEST = False
allCardData = cards.generateAllCardsWithProperties()
PICTS_DIR_PATH = os.path.join(os.getcwd(), 'cards')
pict_width = 194
pict_height = 108


def getCards(reDeal = False,
                   cardsInSet = (),
                   lastCardNumbersOnTable = [],
                   freeCardsInPack = []):

    '''kiválaszt 12db random lapot a kezdéshez'''

    defaultCardNum = 12

    print '\n'
    print '------------------------------------------------'
    print '--------------------NEW ROUND-------------------'
    print '------------------------------------------------'

    if reDeal:
        # print '\tlast card numbers:', len(lastCardNumbersOnTable), lastCardNumbersOnTable
        # print '\tcardsInSet:', cardsInSet
        # print '\tlastCardNumbersOnTable', len(lastCardNumbersOnTable)
        # print '\tnewCardNum:', newCardNum, len(cardsInSet)

        if cardsInSet:
            for cc in cardsInSet:
                lastCardNumbersOnTable.remove(cc)

            newCardNum = min(defaultCardNum - len(lastCardNumbersOnTable), len(freeCardsInPack))
        else:
            newCardNum = 3

        reducedCardNumbersOnTable = lastCardNumbersOnTable
        newCards = random.sample(freeCardsInPack, newCardNum)
        cardsOnTable = reducedCardNumbersOnTable + newCards
        freeCardsInPack = tuple(set(freeCardsInPack) - set(newCards))
    else:
        if TEST:
            cardsOnTable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 22]
            # cardsOnTable = random.sample(freeCardsInPack, defaultCardNum)
        else:
            cardsOnTable = random.sample(freeCardsInPack, defaultCardNum)

        # print '\tStart random cards: ', cardsOnTable
        freeCardsInPack = tuple(set(freeCardsInPack) - set(cardsOnTable))

    # print '\tcardsOnTable', cardsOnTable

    print 'A pakliban meg ' + '{:d}'.format(len(freeCardsInPack)) + ' kartya van,' + \
          ' az asztalon levo kartyak:'

    return cardsOnTable, freeCardsInPack


def getCardData_list(cardnum):
    '''visszadja az adptt kártya tulajdonságait'''

    return allCardData[cardnum]


def search_intersections_of_2(set1, set2):
    '''összhasonlít 2db 3as szettet és veszi a közös tulajdonságokat'''

    return set(set1).intersection(set2)


def search_intersections_of_3(currCombi):
    '''összhasonlítja a 3as szetteket hármasával:
    SET, ha:
    -3 tulajdonság megegyezik vagy,
    -2 tulajdonság megegyezik vagy,
    -nincs egyező tulajdonság
    '''

    set1 = getCardData_list(currCombi[0])
    set2 = getCardData_list(currCombi[1])
    set3 = getCardData_list(currCombi[2])

    sum_12 = search_intersections_of_2(set1, set2)
    sum_13 = search_intersections_of_2(set1, set3)
    sum_23 = search_intersections_of_2(set2, set3)

    if sum_12 == sum_13 and sum_12 == sum_23 and sum_12 != 1:
        return True

    return False


def checkCards(cardsOnTable):
    '''legenerálja a létező összes 3as kombót az asztalon lévő lapokból, és ezeken csekkolja a SET-eket'''

    # ii = 1
    # for cardNum, values in cardsData.items():
    #     print ii, '{:2d}'.format(cardNum) + '. szamu kartya'    # (' + '{}'.format(', '.join(values)) + ')'
    #     ii += 1

    for i, cardNum in enumerate(cardsOnTable):
        print i + 1, '{:4d}'.format(cardNum) + '. szamu kartya'
    print '------------------------------------------------'
    # time.sleep(2)

    cardsInSet = []
    temp_cardsOnTable = copy.copy(cardsOnTable)
    bFoundSet = True
    while bFoundSet:
        allCombination = itertools.combinations(temp_cardsOnTable, 3)

        for currCombination in allCombination:
            bFoundSet = search_intersections_of_3(currCombination)

            if bFoundSet:
                print '***SET FOUND***' + ', kartyak szama: ' + str(currCombination)
                print currCombination[0], getCardData_list(currCombination[0])
                print currCombination[1], getCardData_list(currCombination[1])
                print currCombination[2], getCardData_list(currCombination[2])

                for cc in currCombination:
                    temp_cardsOnTable.remove(cc)
                    cardsInSet.append(cc)

                break

    drawCardsWithSet(cardsOnTable, cardsInSet)

    if len(cardsInSet) == 0:
        print 'NO SET FOUND!!!'

    return cardsInSet


def drawCardsWithSet(cardsOnTable, cardsInSet):

    # print
    # print 'cardsOnTable:', cardsOnTable
    # print 'cardsInSet:', cardsInSet
    # print

    list_cardsToShowPict = []
    for cardNum in cardsOnTable:
        if cardNum in allCardData:
            values = allCardData[cardNum]
            list_cardsToShowPict.append(values[0] + '_' +
                                        values[1] + '_' +
                                        values[2] + '_' +
                                        values[3])


    number_of_rows_in_table = 4
    number_of_cols_in_table = 5
    new_pict = PIL.Image.new(mode = 'RGB', size=(pict_width * number_of_rows_in_table, pict_height * number_of_cols_in_table))

    for i, cardInTable in enumerate(cardsOnTable):
        table_pict = list_cardsToShowPict[i]
        pictName = table_pict + '.png'
        pictPath = os.path.join(PICTS_DIR_PATH, pictName)
        orig_pict = PIL.Image.open(pictPath)
        copy_pict = orig_pict.copy()

        # highlight SET cards
        bResizePict = False
        if cardInTable in cardsInSet: # SET card!
            cardIndex = (cardsInSet.index(cardInTable))
            setNumToPrint = ((cardIndex - (cardIndex % 3)) / 3) + 1

            mod_pict = copy_pict
            draw = PIL.ImageDraw.Draw(mod_pict)
            fnt = PIL.ImageFont.truetype('arial.ttf', 20)
            draw.text((5, 5), str(setNumToPrint), font=fnt, fill=(255, 40, 0, 0))
            del draw

            # draw = PIL.ImageDraw.Draw(mod_pict)
            # draw.line((0, 0) + mod_pict.size, fill = 128)
            # draw.line((0, mod_pict.size[1], mod_pict.size[0], 0), fill = 128)
            # del draw
        else:
            bResizePict = True
            mod_pict = copy_pict.resize((int(pict_width * 0.8), int(pict_height * 0.8)))
            enh = PIL.ImageEnhance.Color(mod_pict)
            enh.enhance(0)
            del enh

        pictPosX = (i % 4) * pict_width + int(pict_width * 0.1) * bResizePict
        pictPosY = ((i - (i % 4)) / 4) * pict_height + int(pict_height * 0.1) * bResizePict
        new_pict.paste(mod_pict, box=(pictPosX, pictPosY))

    new_pict.show()


def drawCustomCards_forTest(list_cardsToShow):

    list_cardsToShowPict = []
    for cardNum in list_cardsToShow:
        if cardNum in allCardData:
            values = allCardData[cardNum]
            list_cardsToShowPict.append(values[0] + '_' +
                                        values[1] + '_' +
                                        values[2] + '_' +
                                        values[3])

    number_of_rows_in_table = 3
    number_of_cols_in_table = int(len(list_cardsToShow) / 3) + 1
    new_pict = PIL.Image.new(mode = 'RGB', size=(pict_width * number_of_rows_in_table, pict_height * number_of_cols_in_table))

    for i, table_pict in enumerate(list_cardsToShowPict):
        pictName = table_pict + '.png'
        pictPath = os.path.join(PICTS_DIR_PATH, pictName)
        orig_pict = PIL.Image.open(pictPath)
        copy_pict = orig_pict.copy()

        bResizePict = False
        mod_pict = copy_pict

        pictPosX = (i % 3) * pict_width + pict_width / 4 * bResizePict
        pictPosY = ((i - (i % 3)) / 3) * pict_height + pict_height / 4 * bResizePict
        new_pict.paste(mod_pict, box=(pictPosX, pictPosY))

    new_pict.show()


def main():
    # drawCustomCards_forTest([55, 43, 22])
    # exit()

    reDeal = False
    cardsInSet = ()
    lastCardNumbersOnTable = []
    freeCardsInPack = range(1, 81 + 1)

    while len(freeCardsInPack) > 70:
        cardsOnTable, freeCardsInPack = getCards(reDeal = reDeal,
                                                      cardsInSet = cardsInSet,
                                                      lastCardNumbersOnTable = lastCardNumbersOnTable,
                                                      freeCardsInPack = freeCardsInPack)

        cardsInSet = checkCards(cardsOnTable)      # lista a SET kártyáiról, lehet 3 nál több elemű is, ha több SET-et talál
        reDeal = True
        lastCardNumbersOnTable = cardsOnTable   # lista az asztalon lévő kártyákról

    print
    print 'VÉGE'
    if cardsInSet:
        for cc in cardsInSet:
            cardsOnTable.remove(cc)
    print 'Megmaradt kártyák: ', cardsOnTable


if __name__ == '__main__':
    # before = time.time()
    main()
    # after = time.time()
    # print after - before
