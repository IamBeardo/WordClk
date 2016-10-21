#from GI_classes import individual, word, population, letter
#import GI_classes
import hashlib
import copy
#print ("Hell0 W0rld")
import os
import random

wL = [
                ["hello"        ,0,0,0,     0],


                ["It"           ,1,0,1,     1],
                ["is"           ,1,0,2,     2],

                ["about"        ,2,0,0,     3],
                ["almost"       ,2,0,0,     3],
                ["soon"         ,2,0,0,     3],

                ["ten"          ,3,0,0,     4],
                ["quarter"      ,3,0,0,     4],
                ["twenty"       ,3,0,0,     4],
                ["half"         ,3,0,0,     4],

                ["twenty"       ,3,0,1,     5],
                ["five"         ,3,0,2,     6],

                ["to"           ,4,0,0,     7],
                ["past"         ,4,0,0,     7],

                ["one"          ,5,0,0,     8],
                ["two"          ,5,0,0,     8],
                ["three"        ,5,0,0,     8],
                ["four"         ,5,0,0,     8],
                ["five"         ,5,0,0,     8],
                ["six"          ,5,0,0,     8],
                ["seven"        ,5,0,0,     8],
                ["eight"        ,5,0,0,     8],
                ["nine"         ,5,0,0,     8],
                ["ten"          ,5,0,0,     8],
                ["eleven"       ,5,0,0,     8],
                ["twelve"       ,5,0,0,     8],
                ["noon"         ,5,0,0,     8],
                ["midnight"     ,5,0,0,     8],

            ]
#wordList = [
#                ["First_1"           ,1,0,1,     1],
#                ["First_2"           ,1,0,2,     2],

#                ["Second_A"        ,2,0,0,     3],
#                ["Second_B"       ,2,0,0,     3],

#                ["TRE"          ,3,0,0,     4]]

#GI_classes.wordList = wordList
#GI_classes.sizeX = 15
#GI_classes.sizeY = 15
#random.seed("k u k e n")
#c=population(55)
#print("i")

#c.printStat()
#tmp=max(c.individuals)
#GI_classes.display(tmp)
#os.system("pause")

#for i in range(1000):
#    c.evolve(15)
#    c.printStat()    max(c.individuals).indDetails()


import wkGlobals
#import wkWord
from wkWord import *
from wkGlobals import *
from wkInd import * 
from wkPop import * 

from operator import *

random.seed()
wkGlobals.apa = 15

wordlist.set(wL)

p = pop(10)
print(p.STATS)

for apa in range(10   ):

    p=p.evolve()
    print(p.STATS)

    ind.printTracking()
    os.system("pause")




#i=ind()

#i=ind(-1,-1,
      # [
      # word(None,'hello',[0, 0, 0, 0],[10, 11],[1, 1]), 
      # word(None,'It',[1, 0, 1, 1],[0, 0],[1, 0]), 
      # word(None,'Is',[1, 0, 2, 2],[0, 0],[0, 1]), 
      # word(None,'about',[2, 0, 0, 3],[5, 0],[1, 1]), 
      # word(None,'almost',[2, 0, 0, 3],[9, 7],[0, 1]), 
      # word(None,'soon',[2, 0, 0, 3],[0, 1],[1, 0]), 
      # word(None,'ten',[3, 0, 0, 4],[6, 2],[0, 1]), 
      # word(None,'quarter',[3, 0, 0, 4],[10, 9],[0, 1]), 
      # word(None,'twenty',[3, 0, 0, 4],[12, 11],[1, 1]), 
      # word(None,'half',[3, 0, 0, 4],[5, 9],[1, 0]), word(None,'twenty',[3, 0, 1, 5],[12, 5],[1, 0]), word(None,'five',[3, 0, 2, 6],[3, 4],[1, 1]), word(None,'to',[4, 0, 0, 7],[12, 2],[1, 0]), word(None,'past',[4, 0, 0, 7],[11, 13],[0, 1]), word(None,'one',[5, 0, 0, 8],[12, 1],[1, 1]), word(None,'two',[5, 0, 0, 8],[6, 11],[0, 1]), word(None,'three',[5, 0, 0, 8],[2, 5],[1, 0]), word(None,'four',[5, 0, 0, 8],[10, 8],[1, 1]), word(None,'five',[5, 0, 0, 8],[6, 0],[1, 1]), word(None,'six',[5, 0, 0, 8],[3, 4],[0, 1]), word(None,'seven',[5, 0, 0, 8],[6, 5],[1, 0]), word(None,'eight',[5, 0, 0, 8],[0, 9],[1, 1]), word(None,'nine',[5, 0, 0, 8],[6, 3],[0, 1]), word(None,'ten',[5, 0, 0, 8],[11, 2],[0, 1]), word(None,'eleven',[5, 0, 0, 8],[8, 8],[1, 0]), word(None,'twelve',[5, 0, 0, 8],[11, 11],[1, 0]), word(None,'noon',[5, 0, 0, 8],[11, 6],[1, 0]), word(None,'midnight',[5, 0, 0, 8],[4, 7],[0, 1])
      # ])


#ii=eval(repr(i))
#i=ii.clone()
#ii=None
#print(i)
#print(word.printTracking())
#print (i.fitness)


