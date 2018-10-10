#!/usr/bin/env python
# coding=utf-8

import random

COLOUR = [
    'Red',
    'Green',
    'Purple'
]

FORM = [
    'Elips',
    'Amorf',
    'Tiles'
]

FILL = [
    'Full',
    'Strip',
    'Empty'
]

NUMBER = [
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


def randomCards():

    cards = {}

    for c in range(1, 13):
        randomCardPropertys = [random.choice(COLOUR),\
        random.choice(FORM),\
        random.choice(FILL),\
        random.choice(NUMBER)]

        cards[c] = randomCardPropertys
        # print c, cards[c]

    return cards
    # randomCard = ''.join(randomCardPropertys)


def checkCards(cardsInTable):
    # print cardsInTable.keys()
    # print cardsInTable.values()

    for cardNum, values in cardsInTable.items():
        print cardNum, values[0], type(values[0])
    pass


checkCards(randomCards())



# 12db random kártyát kell generálni a pakliból, egyedinek kell lenniük
# meg kell vizsgálnia a tulajdonságaikat:
# set:
# -ha 3 tulajd. megegyezik
# -ha pontosan 2 tulajd. megegyezik
# -ha nincs egyező tulajd.




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