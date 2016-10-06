import random

wordList=[]
sizeX=0
sizeY=0
directionDistribution = "000111222"

fit_OutOfRange = -10
fit_InRange = 5


def fitness(ind):
    _fitness =0
    _grid = set()
    _intersections = []    

    for w in ind.words:
        ### CHECK OUT OF BOUND ###################################
        # check if a word exeeds the set sizeX/sizeY-grid size
        ##########################################################
        if (w.positionEnd[0] > sizeX) or (w.positionEnd[1] > sizeY):
            _fitness += fit_OutOfRange
        else:
            _fitness += fit_InRange

        ### CHECK OVERLAP CHARS AND CREATE GRID SUMMARY ##########
        # check if a word exeeds the set sizeX/sizeY-grid size
        ##########################################################

        
        
        _intersections = list(_grid.intersection(w.grid))
        for i in _inter        
        _grid = _grid.union(w.grid)
        print(_grid)
        print("##################################")
        print(list(_grid))

        #CHECK GRP ORDER    
        pass

    #
    pass
    return _fitness

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


    def test(self,str):
        print(str)

    def __init__(self):
        self.words = [word().getRandom(w[0],True) for w in wordList]
        pass
    
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

    def __init__(self,text="",position=[0,0],direction=0):

        if text == "": 
            pass
        else:
            self.dirOffset=getDirectionOffset(direction)

            self.text=text
            self.textLen = len(text)
            self.grid = [ letter([position[0]+(self.dirOffset[0]*i),position[1]+(self.dirOffset[1]*i)],c) 
                                for i, c in enumerate(text) ]
            print(self.grid)
            self.positionStart=position
            self.positionEnd=[ position[0] + (self.textLen-1)*self.dirOffset[0],
                               position[1] + (self.textLen-1)*self.dirOffset[1]]



    def getRandom(self,text,checkBoundery = False):
        tDir =  int(random.choice(directionDistribution))
        self.dirOffset=getDirectionOffset(tDir)
        self.textLen = len(text)
        
        if checkBoundery:
            lenght = [(self.textLen-1)*self.dirOffset[0],(self.textLen-1)*self.dirOffset[1]]

            self.__init__(text, [random.randint(0,sizeX-lenght[0]),
                                 random.randint(0,sizeY-lenght[1])] ,tDir)
        else:
            self.__init__(text, [random.randint(0,sizeX),random.randint(0,sizeY)],tDir)
        

        print(self.text)
        print(self.textLen)
        print(self.positionStart)
        print(self.positionEnd)
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

