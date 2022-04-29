#!/usr/bin/env python3

import sys
import time
from math import floor
from random import seed, shuffle
# Regex /^([0-9]+) (.*)$/

def printHelp():
    print("Usage: "+sys.argv[0]+" <deck file> <draw amount>\n"+
            "The deck file must be in the format exported from mtg arena\n"+
            "if draw amount is 0 the result of the shuffle will be displayed\n")

def prepareDeck(deck):
    cardlist = open(sys.argv[1],"r")
    for card in cardlist :
        tmp = card.split(' ',1)
        if len(tmp) == 1 :
            if tmp[0] == "Deck\n":
                continue
            else:
                return
        cardcount = int(tmp[0])
        cardname = tmp[1]
        for i in range(cardcount):
            deck.append(cardname)

def cutDeck(deck):
    upperHalf = deck[0:floor(len(deck)/2)]
    lowerHalf = deck[floor(len(deck)/2):len(deck)-floor(len(deck)/2)]
    deck = lowerHalf + upperHalf



def main():
    if len(sys.argv) == 1:
        printHelp()
        exit()
    if len(sys.argv) == 3:
       try:
           drawcount = int(sys.argv[2])
       except:
           print("Error: Invalid draw count")
           printHelp()
           exit()
    else:
        drawcount = 7

       
    deck = []
    prepareDeck(deck)
    t = int( time.time() * 1000.0 )
    seed(((t & 0xff000000) >> 24) + ((t & 0x00ff0000) >>  8) + ((t & 0x0000ff00) <<  8) + ((t & 0x000000ff) << 24))
    shuffle(deck)
    deck.reverse()
    seed(((t & 0xff000000) >> 24) + ((t & 0x00ff0000) >>  8) + ((t & 0x0000ff00) <<  8) + ((t & 0x000000ff) << 24))
    shuffle(deck)
    deck.reverse()
    seed(((t & 0xff000000) >> 24) + ((t & 0x00ff0000) >>  8) + ((t & 0x0000ff00) <<  8) + ((t & 0x000000ff) << 24))
    shuffle(deck)
    cutDeck(deck)
    if drawcount == 0:
        for card in deck:
            print(card,end="")
    else :
        for i in range(drawcount):
            print(deck[i],end="")



if __name__ == '__main__':
    main()
