import wkGlobals
from wkWord import *
from wkGlobals import *
from wkInd import *
from operator import *
from collections import defaultdict




##############################################################################
#
#  CLASS population
#
###############################################################################
class pop(object):
    """ pop """
    def __init__(self,size=0,order=True):
        self.generation = 0
        self.size = size
        self.mateCount = defaultdict(int)

#        self.individuals= [individual(["ONE","TWO","THREE","4"]) for i in range(size)]
        self.individuals= [ind(i) for i in range(size)]
        #print(self.individuals[5].index)
        if order: self.order()

    def calcStat(self):
        self.STATS = dict()
        self.STATS['MIN'] = self.individuals[0].fitness
        self.STATS['MAX'] = self.individuals[self.size-1].fitness
        self.STATS['TOTAL'] = sum(i.fitness for i in self.individuals)
        self.STATS['AVR'] = self.STATS['TOTAL'] / self.size
        self.STATS['MEDIAN'] = self.individuals[int(self.size/2)].fitness
        self.STATS['indviduals'] = len(ind.instances)
        self.STATS['words'] = len(word.instances)
    def order(self):

        self.individuals.sort(key=attrgetter('fitness'))
        for i,indi in enumerate(self.individuals):
            indi.index = i
        self.calcStat()

    def add(self,ind,order=True):
        self.individuals.append(ind)
        self.size +=1
        if order: self.order()

    def evolve(self):

        nextGeneration = pop(order=False )

        # Add elitism
        for elit in self.individuals[-evolution.ELITISM:]:
            nextGeneration.add(elit,order=False)

        # Add new random individuals                
        for i in range(evolution.RANDOMPOPULATION):
            nextGeneration.add(ind(),order=False)

        #mate , get parents
        for sexEncounters in self.orgy(self.size - nextGeneration.size):
            print (sexEncounters)

        nextGeneration.order()
        return nextGeneration
    

    def orgy(self, count):
        listOfParents=set()

        while len(listOfParents) < count:
            ps=self.getParents()
            if ps not in listOfParents:
                valid=True
                a,b = ps
                if self.mateCount[a] < evolution.MAXOFFSPRING and self.mateCount[b] < evolution.MAXOFFSPRING:
                    listOfParents.add(ps)
                    self.mateCount[a] +=1
                    self.mateCount[b] +=1
                    print(self.mateCount)
        return listOfParents

    def getParents(self):
        ps=set()
        while len(ps) <2:
            ps.add(self.tournament(evolution.TOUR_SIZE))
        return tuple(ps)

    def tournament(self,size):
        #t=[random.randrange[self.size] for i in range(size)]
        return max([random.randrange(self.size) for i in range(size)])
