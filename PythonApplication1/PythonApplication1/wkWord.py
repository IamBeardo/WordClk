import  random
import wkGlobals
import weakref
from wkGlobals import *
from operator import *
import operator
class word(object):
    """description of class"""
    instances=weakref.WeakValueDictionary() 
    iCount=0
    
    ###############################
    #
    #  __init__ 
    #
    ###############################    
    def __init__(self,txtGrp=None,text=None,group=None,coordinate=None,dir=None):
        if txtGrp is not None:
            text=txtGrp[0]
            group=txtGrp[1:]      
        self.inRange = None
        self.text=text
        self.group      = group
        self.groupIndex = group[3]
        self.dir        = dir
        self.coordinate = coordinate
        self.len        = len(text)

        x,y   = coordinate
        tx,ty = dir
        tx,ty = tx*(self.len-1),ty *(self.len-1)
        
        self.absStart = y*ySize+x
        self.absEnd=ty*ySize+tx
        self.inRange = ((x+tx)<xSize) and ((y+ty)<ySize)
        #print(self.inRange)

        self.updateGrid()
        word.track(self)

        
    ###############################
    #
    #  __init__ override
    #
    ###############################
    @classmethod
    def fromRandom(cls,txtGrp=None,text=None,group=None,coordinate=None,dir=None):
        if txtGrp is not None:
            text=txtGrp[0]
            group=txtGrp[1:]
        if dir is None:
            dir = random.choice(direction.directions)
        if coordinate is None:
            coordinate = [random.randrange(xSize),random.randrange(xSize)]
        return cls(None,text,group,coordinate,dir)

    def cloneTest(self):
        return word.fromRandom("SSSSS")
       

    def updateGrid(self):
        self.grid =dict()
        _pos = self.coordinate
        for c in self.text:
            k=str(_pos)
            self.grid[k]=c
            _pos =  list(map(add,_pos,self.dir))
        #print(self.grid)

    def getGrid():
        return self.grid

    def __repr__(s):
        return "{}({},'{}',{},{},{})".format(s.__class__.__name__,None,s.text,s.group,s.coordinate,s.dir)

    ###############################
    #
    #  Instance tracking
    #
    ###############################
    @classmethod
    def track(c,s):
        word.iCount += 1
        word.instances[word.iCount] = s
    @classmethod
    def printTracking(c):
        for k in word.instances:
            print(k,word.instances[k])


              

