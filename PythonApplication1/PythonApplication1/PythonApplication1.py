from GI_classes import individual, word, population, letter
import GI_classes
#print ("Hell0 W0rld")






wordList = [
                ["It"           ,1,0,1],
                ["is"           ,1,0,2],

                ["about"        ,2,0,0],
                ["almost"       ,2,0,0],
                ["soon"         ,2,0,0],

                ["ten"          ,3,0,0],
                ["quarter"      ,3,0,0],
                ["twenty"       ,3,0,0],
                ["half"         ,3,0,0],

                ["twenty"       ,3,0,1],
                ["five"         ,3,0,2],

                ["to"           ,4,0,0],
                ["past"         ,4,0,0],

                ["one"          ,5,0,0],
                ["two"          ,5,0,0],
                ["three"        ,5,0,0],
                ["four"         ,5,0,0],
                ["five"         ,5,0,0],
                ["six"          ,5,0,0],
                ["seven"        ,5,0,0],
                ["eight"        ,5,0,0],
                ["nine"         ,5,0,0],
                ["ten"          ,5,0,0],
                ["eleven"       ,5,0,0],
                ["twelve"       ,5,0,0],
                ["noon"         ,5,0,0],
                ["midnight"     ,5,0,0],

                ["hello"        ,0,0,0],
            ]

GI_classes.wordList = wordList
GI_classes.sizeX = 15
GI_classes.sizeY = 15

c=population(1)


print ("".join(str(P) + "\n" for P in c.getPersonalitys()))

print (GI_classes.calcFitness(c.individuals[0]))
print (c.individuals[0].fitness())

GI_classes.display(c.individuals[0])


