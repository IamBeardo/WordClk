import random

wordList=[]
sizeX=0
sizeY=0
directionDistribution = "000111222"

fit_OutOfRange            = -50
fit_InRange               =   5
fit_PositiveIntersection  =  10
fit_NegativIntersection   =  -5
fit_PositiveGroupOrder    =  10
fit_NegativeGroupOrder    = -20

def display(ind):
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


    return ""



def calcFitness(ind):
    _fitness =0
    _grid = dict()
    _intersections = []    

    for count,w in enumerate(ind.words):
        ### CHECK OUT OF BOUND ###################################
        # check if a word exeeds the set sizeX/sizeY-grid size
        ##########################################################
        if (w.positionEnd[0] > sizeX) or (w.positionEnd[1] > sizeY):
            _fitness += fit_OutOfRange
        else:
            _fitness += fit_InRange

        ### CHECK OVERLAP CHARS AND CREATE GRID SUMMARY ##########
        #  
        ##########################################################
        # create a set of intersecting positions and rank them
        _intersections = (_grid.keys() & w.grid)
        for i in _intersections:        
            if _grid[i].text == w.grid[i].text:
                #intersection with matching text values (letter)
                _fitness += fit_PositiveIntersection
            else:
                #intersection with missmatching text values (letter)
                _fitness += fit_NegativIntersection
            
        _grid.update(w.grid)

    #CHECK GRP ORDER   
    #print(ind.words)   
    wSorted = ind.words[:]
    wSorted.sort()
    #print(wSorted)
    for i in range(1,len(wSorted)):
        if groupInOrder(wSorted[i-1].group,wSorted[i].group):
            _fitness += fit_PositiveGroupOrder
        else:
            _fitness += fit_NegativeGroupOrder
        


    #
    pass
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

###############################################################################
#
#  CLASS population
#
###############################################################################
class population(object):
    """ pop """

    def __init__(self,size):
        self.size = size
#        self.individuals= [individual(["ONE","TWO","THREE","4"]) for i in range(size)]
        self.individuals= [individual() for i in range(size)]

    def getPersonalitys(self):
        #return "asdölf"
        return [hash(i) for i in self.individuals]
        pass






###############################################################################
#
#  CLASS individual
#
###############################################################################
class individual(object):
    """A single individual, sub-partical of a population"""

    _fitness = None
    def fitness(self):
        if self._fitness is None:
            self._fitness=calcFitness(self)
        return self._fitness

    def __init__(self):
        self.words = [word().getRandom(w,True) for w in wordList]
        #print("asdf")
    
    def __repr__(self):
        return "".join(str(i)  for i in self.words)

    def __hash__(self):
        #print (hash(repl(self)))
        return hash(repr(self))
        pass
        
                    

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

