from GI_classes import individual, word, population, letter
import GI_classes
import hashlib
import copy
#print ("Hell0 W0rld")
import os





wordList = [
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

                #["one"          ,5,0,0,     8],
                #["two"          ,5,0,0,     8],
                #["three"        ,5,0,0,     8],
                #["four"         ,5,0,0,     8],
                #["five"         ,5,0,0,     8],
                #["six"          ,5,0,0,     8],
                #["seven"        ,5,0,0,     8],
                #["eight"        ,5,0,0,     8],
                #["nine"         ,5,0,0,     8],
                #["ten"          ,5,0,0,     8],
                #["eleven"       ,5,0,0,     8],
                #["twelve"       ,5,0,0,     8],
                #["noon"         ,5,0,0,     8],
                ["midnight"     ,5,0,0,     8],

            ]
#wordList = [
#                ["First_1"           ,1,0,1,     1],
#                ["First_2"           ,1,0,2,     2],

#                ["Second_A"        ,2,0,0,     3],
#                ["Second_B"       ,2,0,0,     3],

#                ["TRE"          ,3,0,0,     4]]

GI_classes.wordList = wordList
GI_classes.sizeX = 15
GI_classes.sizeY = 15

import random
random.seed("h r r")
c=population(50)
print("i")


c.printStat()
tmp=max(c.individuals)
GI_classes.display(tmp)
#for apa in tmp.words:
#    print (apa)
#print("after init")
os.system("pause")



for i in range(1000):
    c.evolve(10)
    c.printStat()
    GI_classes.display(max(c.individuals))
    #GI_classes.debugInd(max(c.individuals))

    #for ind in c.individuals:
    #    GI_classes.display(ind)
    #    os.system("pause")
    #os.system("pause")

    


