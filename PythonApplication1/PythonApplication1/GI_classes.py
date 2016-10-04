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
        pass

        self.text=text
        self.position=position
        self.direction=direction


    def getRandom(self,text):
        self.text=text
        self.position = [random.randint(0,15),random.randint(0,15)]
        return word(text,self.position,random.choice("012")  )  



    def getPosX(self):
        return self.position[0]
    def getPosY(self):
        return self.position[1]
        
    def __repr__(self):
           return "".join("Text:" + self.text + 
                          " Pos:" + str(self.position[0]) + "," + str(self.position[1]) +
                          " Dir:" + str(self.direction) 
                          )
        
