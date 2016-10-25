#from GI_classes import individual, word, population, letter
#import GI_classes
import hashlib
import copy
#print ("Hell0 W0rld")
import os
import random

wL = [
                #["hello"        ,0,0,0,     0],


                ["it"           ,1,0,1,     1],
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
import hashlib
#import wkWord
from wkWord import *
from wkGlobals import *
from wkInd import * 
from wkPop import * 

from operator import *




#h = hashlib.md5(repr(self).encode())
 #       return h.hexdigest()



random.seed()
seedster= hashlib.md5(str(random.random()).encode()).hexdigest()
#seedster= 'teie'
random.seed(seedster)

#
wordlist.set(wL)

p = pop(117)
p.seedster=seedster
print(p.STATS)

#for i in p.individuals:
    #i.printGrpOrder()
#os.system("pause")


t=None
#t=ind(-1,-1,[word(None,'it',[1, 0, 1, 1],[1, -1],[1, 0]), word(None,'is',[1, 0, 2, 2],[6, -1],[1, 0]), word(None,'about',[2, 0, 0, 3],[7, 0],[1, 0]), word(None,'almost',[2, 0, 0, 3],[7, 0],[1, 1]), word(None,'soon',[2, 0, 0, 3],[11, -1],[1, 0]), word(None,'ten',[3, 0, 0, 4],[7, 1],[1, 1]), word(None,'quarter',[3, 0, 0, 4],[-1, 1],[0, 1]), word(None,'twenty',[3, 0, 0, 4],[7, 1],[0, 1]), word(None,'half',[3, 0, 0, 4],[1, 1],[1, 0]), word(None,'twenty',[3, 0, 1, 5],[9, 1],[1, 1]), word(None,'five',[3, 0, 2, 6],[10, 1],[1, 0]), word(None,'to',[4, 0, 0, 7],[0, 2],[1, 1]), word(None,'past',[4, 0, 0, 7],[1, 2],[1, 0]), word(None,'one',[5, 0, 0, 8],[6, 3],[0, 1]), word(None,'two',[5, 0, 0, 8],[2, 3],[1, 1]), word(None,'three',[5, 0, 0, 8],[9, 8],[0, 1]), word(None,'four',[5, 0, 0, 8],[8, 5],[1, 0]), word(None,'five',[5, 0, 0, 8],[11, 2],[1, 0]), word(None,'six',[5, 0, 0, 8],[12, 3],[1, 0]), word(None,'seven',[5, 0, 0, 8],[9, 7],[1, 0]), word(None,'eight',[5, 0, 0, 8],[10, 7],[0, 1]), word(None,'nine',[5, 0, 0, 8],[2, 8],[1, 0]), word(None,'ten',[5, 0, 0, 8],[0, 3],[1, 1]), word(None,'eleven',[5, 0, 0, 8],[8, 6],[1, 0]), word(None,'twelve',[5, 0, 0, 8],[0, 3],[0, 1]), word(None,'noon',[5, 0, 0, 8],[2, 12],[1, 0]), word(None,'midnight',[5, 0, 0, 8],[1, 9],[1, 0])])
#t=ind(-1,-1,[word(None,'It',[1, 0, 1, 1],[11, 1],[1, 1]), word(None,'is',[1, 0, 2, 2],[0, 2],[1, 0]), word(None,'about',[2, 0, 0, 3],[5, 2],[0, 1]), word(None,'almost',[2, 0, 0, 3],[4, 2],[0, 1]), word(None,'soon',[2, 0, 0, 3],[10, 2],[1, 1]), word(None,'ten',[3, 0, 0, 4],[0, 3],[1, 0]), word(None,'quarter',[3, 0, 0, 4],[3, 4],[1, 1]), word(None,'twenty',[3, 0, 0, 4],[0, 3],[0, 1]), word(None,'half',[3, 0, 0, 4],[10, 2],[0, 1]), word(None,'twenty',[3, 0, 1, 5],[5, 4],[0, 1]), word(None,'five',[3, 0, 2, 6],[0, 5],[0, 1]), word(None,'to',[4, 0, 0, 7],[6, 6],[0, 1]), word(None,'past',[4, 0, 0, 7],[4, 5],[0, 1]), word(None,'one',[5, 0, 0, 8],[1, 14],[0, 1]), word(None,'two',[5, 0, 0, 8],[4, 12],[1, 0]), word(None,'three',[5, 0, 0, 8],[3, 10],[1, 1]), word(None,'four',[5, 0, 0, 8],[6, 7],[1, 0]),word(None,'five',[5, 0, 0, 8],[2, 7],[1, 1]), word(None,'six',[5, 0, 0, 8],[13, 9],[1, 1]), word(None,'seven',[5, 0, 0, 8],[1, 13],[1, 0]), word(None,'eight',[5, 0, 0, 8],[2, 13],[0, 1]), word(None,'nine',[5, 0, 0, 8],[2, 11],[1, 0]), word(None,'ten',[5, 0, 0, 8],[3, 14],[1, 1]), word(None,'eleven',[5, 0, 0, 8],[12, 11],[1, 0]), word(None,'twelve',[5, 0, 0, 8],[12, 14],[0, 1]), word(None,'noon',[5, 0, 0, 8],[0, 10],[1, 1]), word(None,'midnight',[5, 0, 0, 8],[14, 10],[0, 1])])

#'Seedster': 0.995557454442144,
#t=ind(-1,-1,[word(None,'It',[1, 0, 1, 1],[1, 2],[1, 1]), word(None,'is',[1, 0, 2, 2],[12, 1],[1, 1]), word(None,'about',[2, 0, 0, 3],[0, 11],[0, 1]), word(None,'almost',[2, 0, 0, 3],[11, 10],[1, 0]), word(None,'soon',[2, 0, 0, 3],[5, 8],[0, 1]), word(None,'ten',[3, 0, 0, 4],[13, 7],[1, 1]), word(None,'quarter',[3, 0, 0,4],[12, 8],[1, 1]), word(None,'twenty',[3, 0, 0, 4],[12, 2],[1, 0]), word(None,'half',[3, 0, 0, 4],[14, 7],[0, 1]), word(None,'twenty',[3, 0, 1, 5],[6, 2],[1, 0]), word(None,'five',[3, 0, 2, 6],[9, 12],[1, 0]), word(None,'to',[4, 0, 0, 7],[11, 7],[0, 1]), word(None,'past',[4, 0, 0, 7],[10, 12],[0, 1]), word(None,'one',[5, 0, 0, 8],[1, 3],[1, 1]), word(None,'two',[5, 0, 0, 8],[2, 3],[1, 0]), word(None,'three',[5, 0, 0, 8],[8, 6],[0, 1]), word(None,'four',[5, 0, 0, 8],[5, 7],[0, 1]), word(None,'five',[5, 0, 0, 8],[7, 7],[1, 1]), word(None,'six',[5, 0, 0, 8],[4, 5],[0, 1]), word(None,'seven',[5, 0, 0, 8],[5, 0],[0, 1]), word(None,'eight',[5, 0, 0, 8],[8, 4],[1, 0]), word(None,'nine',[5, 0, 0, 8],[5, 7],[1, 1]), word(None,'ten',[5, 0, 0, 8],[10, 6],[1, 0]), word(None,'eleven',[5, 0, 0, 8],[9,10],[1, 1]), word(None,'twelve',[5, 0, 0, 8],[11, 3],[1, 1]), word(None,'noon',[5, 0, 0, 8],[9, 9],[1, 0]), word(None,'midnight',[5, 0, 0, 8],[6, 5],[0, 1])])
if t is not None:
    t.calcFitness()
    for w in t.words:
        print (w, w.absStart)
    t.printSet()
    os.system("pause")




with open('apa.dat','w') as f:
    f.write("GENERATIONS,MAX,AVR,MEDIAN,DIVERSITY\n")
    f.close
#C:\Users\adama\Desktop\GitHub\WordClk\PythonApplication1\PythonApplication1
filename = "apa.dat"
for apa in range(1000):

    p=p.evolve(20,filename)
    print(p.STATS)
    #for k in p.poolSet:
    #    print(k, p.poolSet[k])
    #p.evaluateGenPool()
    print(p.individuals[p.size-1].intInValid,p.individuals[p.size-1].intValid )
 
    p.individuals[p.size-1].printGrpOrder()
    p.individuals[p.size-1].printSet()
    #for i in p.individuals:
    #    i.printGrpOrder()
    #os.system("pause")
    
    
    if  (p.individuals[p.size-1].intInValid == 0)  and (
         p.individuals[p.size-1].grpOutOfOrder == 0) and (
         p.individuals[p.size-1].wrdOutOfBound == 0):
        print("#####################################################")
        print("    DONE")
        print("#####################################################")
        print("GENERATION: "+str(p.generation))
        print(p.STATS)
        p.individuals[p.size-1].printGrpOrder()
        p.individuals[p.size-1].printSet()
        print(p.individuals[p.size-1])

        os.system("pause")

    #ind.printTracking()
    #p.individuals[p.size-1].printSet()
    #print((p.individuals[p.size-1].genString))
    #os.system("pause")




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


