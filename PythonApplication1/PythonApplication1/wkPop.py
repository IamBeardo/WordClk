import wkGlobals
from wkWord import *
from wkGlobals import *
from wkInd import *
from operator import *
from collections import defaultdict
import os




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
        self.mateCount =  defaultdict(int)
        self.seedster = None
        #print (self.mateCount.items())

#        self.individuals= [individual(["ONE","TWO","THREE","4"]) for i in range(size)]
        self.individuals= [ind(i) for i in range(size)]
        #print(self.individuals[5].index)
        if order: self.order()

    def calcStat(self):
        self.STATS = dict()
        self.STATS['GENERATION'] = self.generation
        self.STATS['Seedster'] = self.seedster
        self.STATS['MIN'] = self.individuals[0].fitness
        self.STATS['MAX'] = self.individuals[self.size-1].fitness
        self.STATS['TOTAL'] = sum(i.fitness for i in self.individuals)
        self.STATS['AVR'] = self.STATS['TOTAL'] / self.size
        self.STATS['MEDIAN'] = self.individuals[int(self.size/2)].fitness
        self.STATS['indviduals'] = len(ind.instances)
        self.STATS['words'] = len(word.instances)

        self.evaluateGenPool()
        self.STATS['PoolCount'] = len(self.poolSet)
        self.STATS['Diversity'] = int(self.diversity *10000)/100
        
    def order(self):

        self.individuals.sort(key=attrgetter('fitness'))
        for i,indi in enumerate(self.individuals):
            indi.index = i
        self.calcStat()

    def add(self,ind,order=True):
        self.individuals.append(ind)
        self.size +=1
        if order: self.order()

    def evolve(self,count=1):
        for c in range(count):
            #print("EVO")
            self.mateCount.clear()
            nextGeneration = pop(order=False )
            nextGeneration.generation = self.generation +1
            nextGeneration.seedster = self.seedster
        

            # Add elitism
            for elit in self.individuals[-evolution.ELITISM:]:
                nextGeneration.add(elit,order=False)

            # Add new random individuals                
            for i in range(evolution.RANDOMPOPULATION):
                nextGeneration.add(ind(),order=False)

            #mate , get parents
            for sexEncounters in self.orgy(self.size - nextGeneration.size):
                nextGeneration.add(self.offspring(sexEncounters))

            nextGeneration.order()
            self=nextGeneration
            #self.mateCount.clear()
        return self


    def evaluateGenPool(self):

        n,N=0,0
        sumOfn=0
        sumOfN=0
        self.poolSet = defaultdict(int)
        self.poolSet.clear
        #self.pool=[( i.genString + str(i.grandIndex) +','+ str(i.index)) for i in self.individuals]
        for i in self.individuals:
            self.poolSet[i.genString] +=1

        # calc genpool diversity d=SUM(individuals * (individuals-1)/sum(nrOfIndividuals * (nrOfIndividuals-1)) 
        # d is reversed to diversity where 0 is no diversity and 1 full diversity 
        for k in self.poolSet:
            n = self.poolSet[k]
            sumOfn += n*(n-1)        
            N += n
        sumOfN = N*(N-1)
        d=sumOfn/sumOfN
        self.diversity = 1-d
        #self.pool.sort()
        #for g in pool:
        #print(self.poolSet)
        



    def offspring(self,ps):
        pass
        a,b = ps
        child = ind(fromList=[])
        crossPointOffset = int(evolution.CROSSPOINTBOUNDERY*wordlist.lenght)

        crossPoint=random.randrange(crossPointOffset,wordlist.lenght-crossPointOffset)
        child.words= self.individuals[a].words[:crossPoint] + self.individuals[b].words[crossPoint:]
        child.grandIndex = [a,b]
        child.calcFitness()
        if random.random() < evolution.MUTATIONRATE:
           return child.mutate()
        else:
            return child

    def orgy(self, count):
        listOfParents=set()
        i=0
        while len(listOfParents) < count:
            i+=1
            ps=self.getParents()
            if ps not in listOfParents:
                valid=True
                a,b = ps
                if self.mateCount[a] < evolution.MAXOFFSPRING and self.mateCount[b] < evolution.MAXOFFSPRING:
                    listOfParents.add(ps)
                    #print("NOT IN LIST")
                    self.mateCount[a] +=1
                    self.mateCount[b] +=1
                    #print(self.mateCount)
                else:
                    pass
                    #print("IN LIST")
        #print("Count {}, reached in {} executions".format(count,i))
        #os.system("pause")
        return listOfParents

    def getParents(self):
        ps=set()
        while len(ps) <2:
            ps.add(self.tournament(evolution.TOUR_SIZE))
        return tuple(ps)

    def tournament(self,size):
        #t=[random.randrange[self.size] for i in range(size)]
        return max([random.randrange(self.size) for i in range(size)])
