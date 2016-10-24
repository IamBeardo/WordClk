import  random
import wkGlobals
import weakref
from wkGlobals import *
from wkWord import *
from operator import *
import operator
import hashlib
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
        self.genString = ""
        self.index=index
        self.grandIndex=grandIndex
        if fromList is not None:
            self.words= fromList       
        else:
            self.words= [word.fromRandom(txtGrp=w) for w in wordlist.lst]    
        
        self.grid=dict()    
        self.grpOutOfOrder = 0
        self.grpInOrder = 0

        if self.words != []: 
            self.calcFitness()
        ind.track(self)


    def clone(self):
        return eval(repr(self))


    def printSet(self):
        for y in range(ySize):
            for x in range(xSize):
                pass
                c=" "
                k=str([x,y])
                if k in self.grid:
                    c=self.grid[k]
                print(c,end="")
            print("")

    def groupInOrder(self,a,b,cmp):
        # Compare list of groups like: a[1,3,0] b[0,4,1]
        # Zero (0) - indicates no order
        for i in range(len(a)):
            if (a[i] > b[i]) and (b[i] > 0):
                return False
        return True

    def calcFitness(self):
  
        self.fitness=0
        self.grpInOrder=0
        self.grpOutOfOrder=0

        _intersections=dict()
        sWords = sorted(self.words, key=attrgetter('absStart'))
        
        #CHECK GRP ORDER 
        a=sWords[0]
        cmp=[0,0,0]
        #cmpGRP=sWords[0].group
        for b in sWords[1:]:
            if self.groupInOrder(a.group,b.group,cmp):
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
        self.genString = self.genRepr()

    def genRepr(self):
        h = hashlib.md5(repr(self).encode())
        return h.hexdigest()
            
    def __repr__(s):
        return "{}({},{},{})".format(s.__class__.__name__,-1,-1,
                                     [w for w in s.words])




    
    def mutate_close_swap_words(self):
        #random coordinate
        aWord = random.randrange(wordlist.lenght)
        bWord = aWord +1
        
        if bWord == wordlist.lenght: bWord = 1

        mutant = self.clone()
        #print(mutant.words[aWord].coordinate, mutant.words[bWord].coordinate)
        mutant.words[aWord].coordinate, mutant.words[bWord].coordinate = mutant.words[bWord].coordinate,mutant.words[aWord].coordinate
        #print(mutant.words[aWord].coordinate, mutant.words[bWord].coordinate)
        #print("MUTATBBBBB")
        return mutant.clone()


    def mutate_random_cordinate(self):
        #random coordinate
        mWord = random.randrange(wordlist.lenght)
        coordinate = [random.randrange(xSize),random.randrange(xSize)]
        mutant = self.clone()
        mutant.words[mWord].coordinate = coordinate
        #print("MUTATEEEE")
        return mutant.clone()

    def mutate_swap_words(self):
        #random coordinate
        aWord = random.randrange(wordlist.lenght)
        bWord = random.randrange(wordlist.lenght)
        while bWord == aWord:
            bWord = random.randrange(wordlist.lenght)
        mutant = self.clone()
        #print(mutant.words[aWord].coordinate, mutant.words[bWord].coordinate)
        mutant.words[aWord].coordinate, mutant.words[bWord].coordinate = mutant.words[bWord].coordinate,mutant.words[aWord].coordinate
        #print(mutant.words[aWord].coordinate, mutant.words[bWord].coordinate)
        #print("MUTATBBBBB")
        return mutant.clone()

    def mutate(self):
        m = random.choice( [self.mutate_random_cordinate,
                            self.mutate_swap_words,
                            self.mutate_close_swap_words])
        return m()



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
