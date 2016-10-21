import  random
import wkGlobals
import weakref
from wkGlobals import *
from wkWord import *
from operator import *
import operator
class ind(object):
    """description of class"""
    instances=weakref.WeakValueDictionary() 
    iCount=0
    
    ###############################
    #
    #  __init__ 
    #
    ###############################    
    def __init__(self,index=-1,grandIndex=-1,fromList=None):
        self.fitness=None
        self.index=index
        self.grandIndex=grandIndex
        if fromList is not None:
            self.words= fromList       
        else:
            self.words= [word.fromRandom(txtGrp=w) for w in wordlist.lst]    
        
        self.grid=dict()    
        self.grpOutOfOrder = 0
        self.grpInOrder = 0

        self.calcFitness()
        ind.track(self)


    def clone(self):
        return eval(repr(self))

    def groupInOrder(self,a,b):
        # Compare list of groups like: a[1,3,0] b[0,4,1]
        # Zero (0) - indicates no order
        for i in range(len(a)):
            if (a[i] > b[i]) and (b[i] > 0):
                return False
        return True

    def calcFitness(self):
        self.fitness=0
        _intersections=dict()
        sWords = sorted(self.words, key=attrgetter('absStart'))

        #CHECK GRP ORDER 
        a=sWords[0]
        for b in sWords[1:]:
            if self.groupInOrder(a.group,b.group):
                self.fitness += (2-(b.groupIndex-a.groupIndex))* fit.GROUPORDERPOS
                self.grpInOrder += 1
            else:
                self.fitness += (a.groupIndex-b.groupIndex) * fit.GROUPORDERNEG
                self.grpOutOfOrder += 1
            a=b   

        ### CHECK OUT OF BOUND ###################################
        # check if a word exeeds the set sizeX/sizeY-grid size
        ##########################################################

        for w in self.words:
            if w.inRange:
                self.fitness += fit.INBOUND
            else:
                self.fitness += fit.OUTOFBOUND

            ### CHECK OVERLAP CHARS AND CREATE GRID SUMMARY ##########
            #  
            ##########################################################
            #create a set of intersecting positions and rank them
            
            _intersections=self.grid.keys() & w.grid
            for i in _intersections:
                if self.grid[i]==w.grid[i]:
                    #intersection with matching text values (letter)
                    self.fitness += fit.INTERSECTIONPOS
                else:
                    #intersection with missmatching text values (letter)
                    self.fitness += fit.INTERSECTIONNEG
            self.grid.update(w.grid)

    def __repr__(s):
        return "{}({},{},{})".format(s.__class__.__name__,s.index,s.grandIndex,
                                     [w for w in s.words])



    ###############################
    #
    #  Instance tracking
    #
    ###############################
    @classmethod
    def track(c,s):
        ind.iCount += 1
        ind.instances[ind.iCount] = s
    @classmethod
    def printTracking(c):
        for k in ind.instances:
            print(k,ind.instances[k].index)
