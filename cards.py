#!/usr/bin/env python
# coding=utf-8

# import pygame

import collections

COLOURS = ['Red', 'Green', 'Blue']
FORMS = ['Elips', 'Amorf', 'Tiles']
FILLS = ['Full', 'Strip', 'Empty']
NUMBERS = ['One', 'Two', 'Three']


def generateAllCardsWithProperties():
    '''legenerálja a teljes kártyapaklit (81db (3*3*3*3) kártya)'''
    allCardData = {}
    num = 1

    for fill in FILLS:
        for colour in COLOURS:
            for form in FORMS:
                for number in NUMBERS:
                    allCardData[num] = [fill, colour, form, number]
                    num += 1

    return allCardData


def buildCards(xx, c, a=10, b='20'):
    '''na ez az'''

    # print 'aa'

    pass


class va:
    def __init__(self):
        self.szam = 0

    def nov(self):
        self.szam += 1

        return self.szam
    pass


def fa(*args, **kwargs):

    print type(args), type(kwargs)


if __name__ == '__main__':
    print 'TEST OK!'
    # buildCards()

    # all = generateAllCardsWithProperties()
    # print type(all)
    # for key, value in all.items():
    #     print key, value

    # sz = va()
    # sz2 =va()
    #
    # print sz.nov()
    # print sz2.nov()
    #
    # fa(1, 2, 3, 4, aa = 'a', bb = 'b', cc = 'c', dd = 'd')

