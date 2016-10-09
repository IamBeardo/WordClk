import random, os
from collections import Counter

wordList=[]
sizeX=0
sizeY=0
directionDistribution = "000111222"

fit_OutOfRange            = -50 #prevented in getRandom word
fit_InRange               =   5
fit_PositiveIntersection  =  43
fit_NegativIntersection   =  -203
fit_PositiveGroupOrder    =  188
fit_NegativeGroupOrder    = -420

evo_TournamentSize = 3
evo_Elitism = 0
evo_MutationRate = 0.02

d=Counter()

tempGenInd=0

def OLD_getParents(lst):
    
    t=set() 
    while len(t) < min(2,len(lst)):
        n=getIndFromTournament(evo_TournamentSize)
        t.add(n)
        #print(len(t))
        #os.system("pause")
        #print(t)
    
    #print("Parents:",list(t))
    return sorted(list(t))

def OLD___getIndFromTournament(lst, candidates):
    #selects <candidates> number of elements at random from <lst>
    #returning the highest in the selection
    t =set()
    lstLen = len(lst)
    if lstLen < candidates: candidates = lstLen
    #print("")
    while len(t) < candidates:
        ttt=(lst[random.randrange(lstLen)])
        t.add(ttt)
        #print(" added: ", ttt, end="") 
    ret = max(list(t))
    #print("returning:[" + str(ret.index) +"]",ret)

    return ret



def debugInd(ind):
    for i,w in enumerate(ind.words):
        tt=individual()
        tt.words= ind.words[:i]
        display(tt,debug=True)
        os.system("pause")

def display(ind,debug=False):
    _grid = dict()

    for count,w in enumerate(ind.words):
        _grid.update(w.grid)

    print("#" * (sizeX+2))
    for y in range(sizeY):
        print("#",end="")
        for x in range(sizeX):
            key = ''.join([str(x),":",str(y)])
            if key in _grid:
                print(_grid[key].text,end="")
            else:
                print(" ",end=""),
        print("#")
    print("#" * (sizeX+2))

    print(ind.fitness(debug))
    return ""



def calcFitness(ind,debug=False):
    _fitness =0
    _grid = dict()
    _intersections = []    




    ########### NEEEEEEEDS rework..... grp order 0...n needs to be top contributare to fitness.

    for count,w in enumerate(ind.words):
        ### CHECK OUT OF BOUND ###################################
        # check if a word exeeds the set sizeX/sizeY-grid size
        ##########################################################
        if (w.positionEnd[0] > sizeX) or (w.positionEnd[1] > sizeY):
            _fitness += fit_OutOfRange
            if debug: print(w.text, "out of range", _fitness)
        else:
            _fitness += fit_InRange
            if debug: print(w.text, "in range", _fitness)

        ### CHECK OVERLAP CHARS AND CREATE GRID SUMMARY ##########
        #  
        ##########################################################
        # create a set of intersecting positions and rank them
        _intersections = (_grid.keys() & w.grid)
        for i in _intersections:        
            if _grid[i].text == w.grid[i].text:
                #intersection with matching text values (letter)
                _fitness += fit_PositiveIntersection
                if debug: print(i, "pos intersect", _grid[i].text, _fitness)
            else:
                #intersection with missmatching text values (letter)
                _fitness += fit_NegativIntersection
                if debug: print(i, "neg intersect", _grid[i].text, _fitness)
            
        #w.grid.difference_update(_grid)
        _grid.update(w.grid)
        #_grid = dict(w.grid.items() + _grid.items())

    #CHECK GRP ORDER   
    #print(ind.words)   
    wSorted = ind.words[:]
    wSorted.sort()
    #print(wSorted)
    orderingIndex=0
    
    for i in range(1,len(wSorted)):
        #print(wSorted[i-1].group,wSorted[i].group,groupInOrder(wSorted[i-1].group,wSorted[i].group))
        if groupInOrder(wSorted[i-1].group,wSorted[i].group):
            orderingIndex += 1
            _fitness += fit_PositiveGroupOrder * orderingIndex
            if debug: print(i, "grp order pos", _fitness)
        else:
            orderingIndex = 0
            _fitness += fit_NegativeGroupOrder
            if debug: print(i, "grp order neg", _fitness)

    return _fitness

def groupInOrder(a,b):
    # Compare list of groups like: a[1,3,0] b[0,4,1]
    # Zero (0) - indicates no order
    for i in range(len(a)):
        if (a[i] > b[i]) and (b[i] > 0):
            return False
    return True


def getDirectionOffset(direction):
    if direction == 0:   #Left-Right
        return [1,0]
    elif direction == 1: #Top-Down
        return [0,1]
    elif direction == 2: #Diagonal Down
        return [1,1]    



def getOffspring(parents,popSize,dual=True):
        parentsMatrix=[parents]        
        if dual: parentsMatrix.append(list(reversed(parents)))
        #print(parentsMatrix) 
        children=[]               
        crosspoint = random.randrange(len(wordList))
        for p in parentsMatrix:
            a,b = p
            d.update([a.index,b.index])
            child = individual(-1,(a.index + b.index)/2/popSize)
            child.words = a.words[:crosspoint] + b.words[crosspoint:]
            #print (child)
            children.append(child)

        return children


def mutate(ind):
    if random.random() < evo_MutationRate:
        rWord=random.randrange(len(wordList))
        #print("orig",ind.words[rWord])
        ind.words[rWord].getRandom(wordList[rWord],True)
        #print("orig",ind.words[rWord])
    return ind
##############################################################################
#
#  CLASS population
#
###############################################################################
class population(object):
    """ pop """
    def __init__(self,size):
        self.generation = 0
        self.size = size
#        self.individuals= [individual(["ONE","TWO","THREE","4"]) for i in range(size)]
        self.individuals= [individual(i) for i in range(size)]
        self.order()

    def printStat(self):
        #for ind in self.individuals:
        #    print("FITNESS:",ind.fitness())
        print("GENERATION:", self.generation)
        print("MAX:",max(self.individuals).fitness())
        print("MIN:",min(self.individuals).fitness())
        print("SUM:",sum(self.individuals))
        print("AVR:",sum(self.individuals)/len(self.individuals))
        print("GENPOOL:",len(self.getGenPool()))

    def getParents(self):
    
        t=set() 
        while len(t) < 2:
            n=self.getIndFromTournament(evo_TournamentSize)
            #print("FROM TOURNAMENT:", n)
            t.add(n)
        #print("returning:", t)
        return sorted(list(t))

    def getIndFromTournament(self,candidates):
        #selects <candidates> number of elements at random individuals
        #returning the highest in the selection
        return max([random.choice(self.individuals) for i in range(candidates)])

    def getPersonalitys(self):
        #return "asdölf"
        return [hash(i) for i in self.individuals]


    def getGenPool(self):
        #return "asdölf"
        return set([hash(i) for i in self.individuals])

    def order(self):
        self.individuals.sort()
        for i,ind in enumerate(self.individuals):
            ind.index=i

    def evolve(self,generations=1):
        
        for gens in range(generations):
            nextGeneration = population(0)
            # Add elits if any
            nextGeneration.add(max(self.individuals))

            while nextGeneration.size < self.size:
                for child in getOffspring(self.getParents( ),self.size):
                    if nextGeneration.size < self.size: nextGeneration.add(mutate(child))
                    #print("Child Added", child)
            self.individuals = nextGeneration.individuals.copy()
            self.generation +=1
            self.order()




    def add(self,ind):
        ind.index=self.size+1
        ind.fitness(force=True)
        self.individuals.append(ind)
        self.size+=1

        







###############################################################################
#
#  CLASS individual
#
###############################################################################
class individual(object):
    """A single individual, sub-partical of a population"""

    _fitness = None
    def fitness(self,debug=False,force=False):
        if (self._fitness is None) or (force):
            self._fitness=calcFitness(self,debug)
        return self._fitness

    def __init__(self,index,grandIndex=-1):
        self._fitness= None
        self.index = index
        self.grandIndex = grandIndex
        self.words = [word().getRandom(w,True) for w in wordList]

    
    def __repr__(self):
        return "".join("[" + str(self.index) +"]")
    def __repr2__(self):
        return "".join(str(i)  for i in self.words)
    def __hash__(self):
        #print (hash(repl(self)))
        return hash((self.__repr2__()))
    
    def __lt__(self,other):
        #print (hash(repl(self)))
        return self.fitness() < other.fitness()    
    
    
    def __radd__(self,other):
        #print (hash(repl(self)))
        return self.fitness() + other
     
    def __str__(self):
        t=["Index:[",str(self.index), "], GI:[",str(self.grandIndex),
           "], Fitness: [",str(self.fitness()),"] ,Identity:",str(hash(self))]
        return "".join(t)
                    
    
###############################################################################
#
#  CLASS word
#
###############################################################################
class word(object):
    """ 
    word object 
    """

    def __init__(self,w=["",0,0,0],position=[0,0],direction=0):
        self.grid = dict()
        self.group = w[1:] 
        self.text=w[0]


        if self.text == "": 
            pass
        else:
            self.dirOffset=getDirectionOffset(direction)
            self.textLen = len(self.text)


            for i, c in enumerate(self.text):
                x=position[0]+(self.dirOffset[0]*i)
                y=position[1]+(self.dirOffset[1]*i)
                l=letter([x,y],c)
                self.grid[str(l)] = l


            
#            self.grid = [ letter([position[0]+(self.dirOffset[0]*i),position[1]+(self.dirOffset[1]*i)],c) 
#                                for i, c in enumerate(text) ]
#            print(self.grid)
            self.positionStart=position
            self.positionEnd=[ position[0] + (self.textLen-1)*self.dirOffset[0],
                               position[1] + (self.textLen-1)*self.dirOffset[1]]
            self.positionAbs=self.positionStart[1] * sizeX +self.positionStart[0]


    def getRandom(self,w,checkBoundery = False):
        tDir =  int(random.choice(directionDistribution))
        self.dirOffset=getDirectionOffset(tDir)
        self.textLen = len(w[0])
        
        if checkBoundery:
            lenght = [(self.textLen-1)*self.dirOffset[0],(self.textLen-1)*self.dirOffset[1]]

            self.__init__(w, [random.randint(0,sizeX-lenght[0]),
                                 random.randint(0,sizeY-lenght[1])] ,tDir)
        else:
            self.__init__(w, [random.randint(0,sizeX),random.randint(0,sizeY)],tDir)
        

        #print(self.text)
        #print(self.textLen)
        #print(self.positionStart)
        #print(self.positionEnd)
        return self 

    def getXStart(self):
        return int(self.position[0])

    def getYStart(self):
        return int(self.position[1])
        
    def __str__(self):
        return "".join("Text:" + self.text + 
                          " Pos:" + str(self.positionStart[0]) + "," + str(self.positionStart[1]) +
                          " Dir:" + str(self.dirOffset) 
                          )
    def __repr__(self):
        return self.__str__()

    def __lt__(self,other):
        return self.positionAbs < other.positionAbs
    #def __eq__(self,other):
    #    t= self.positionAbs == other.positionAbs
    #    return t
###############################################################################
#
#  CLASS letter
#
###############################################################################   
class letter(object):
    """ """
    
    def __init__(self, xy, text):
        self.xy = xy
        self.text = text
    
    def __repr__(self):
        return "".join(str(self.xy[0]) + ":" + str(self.xy[1]) )

    def __eq__(self,other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash( repr(self)) 

