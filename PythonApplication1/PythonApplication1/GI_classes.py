import random

###############################################################################
#
#  CLASS word
#
###############################################################################
class population(object):
    """ pop """

    def __init__(self,size):
        self.size = size

        self.individuals= [individual(["ONE","TWO","THREE","4"]) for i in range(size)]






###############################################################################
#
#  CLASS individual
#
###############################################################################
class individual(object):
    """A single individual, sub-partical of a population"""


    def test(self,str):
        print(str)

    def __init__(self,wordlist):
        self.test ="asdfa"
        self.words = [word().getRandom(w) for w in wordlist ]
        pass
    
    def __repr__(self):
        return "".join(str(i)  for i in self.words)
                    

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
        
        if direction == 0:   #Left-Right
            self.xD=1
            self.yD=0
        elif direction == 1: #Top-Down
            self.xD=0
            self.yD=1
        elif direction == 2: #Diagonal Down
            self.xD=1
            self.yD=1

            
        self.text=text
        self.grid = { letter([position[0]+(self.xD*i),position[1]+(self.yD*i)],c) 
                            for i, c in enumerate(text) }

        self.position=position
        self.direction=direction

    def getRandom(self,text):
        self.__init__(text,[random.randint(0,15),random.randint(0,15)],int(random.choice("012")))
        return self 

    def getPosX(self):
        return self.position[0]

    def getPosY(self):
        return self.position[1]
        
    def __str__(self):
           return "".join("Text:" + self.text + 
                          " Pos:" + str(self.position[0]) + "," + str(self.position[1]) +
                          " Dir:" + str(self.direction) 
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

