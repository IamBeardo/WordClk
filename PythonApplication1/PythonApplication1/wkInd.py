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
        self.grpOutOfOrder  = 0
        self.grpInOrder     = 0
        self.wrdInBound     = 0
        self.wrdOutOfBound  = 0
        self.intValid       = 0
        self.intInValid     = 0

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

    def printGrpOrder(self):
        t = [w.groupIndex for w in sorted(self.words, key=attrgetter('absStart'))]
        print (t, self.fitness)

    def groupOrderRating(self, a, b):
        diff = (b.groupIndex - a.groupIndex)
        order=True
        if diff == 0:
            #same grp
            modifier=1
        elif diff == 1:
            #next grp
            modifier=0.9 
        else:            
            #grp out of order
            order=False
            modifier =0.6 * (1-(abs(diff)/10))
        return modifier, order




    def calcFitness(self):
  
        self.fitness        = 0
        self.grpOutOfOrder  = 0
        self.grpInOrder     = 0
        self.wrdInBound     = 0
        self.wrdOutOfBound  = 0
        self.intValid       = 0
        self.intInValid     = 0

        _intersections=dict()
        sWords = sorted(self.words, key=attrgetter('absStart'))

        ### GRP ORDER ############################################
        # the fitness gain for a grp in order is lowred anytime 
        # a grp is out of order.
        # bigger difference between cmp grps lowers f_gain more
        ##########################################################
        
        grpIdxMultiplier = fit.GROUPORDERPOS
        diff=sWords[0].groupIndex-1
        if not diff:
            self.fitness = grpIdxMultiplier 
        else:
            grpIdxMultiplier = grpIdxMultiplier * 0.6 * (1-(diff/10))
        a=sWords[0]
        for b in sWords[1:]:
            m, o = self.groupOrderRating(a,b)
            grpIdxMultiplier *= m
            if o:
                self.fitness += grpIdxMultiplier
                self.grpInOrder += 1
            else:
                 self.grpOutOfOrder += 1
            a=b   

        self.fitness = int(self.fitness)
        #for i,w in enumerate(sWords):
        #    relDiff = i - w.groupIndex
        #    if relDiff == 0: relDiff = 0.5
        #    self.fitness += (10 / relDiff) * fit.GROUPORDERPOS


        ### CHECK OUT OF BOUND ###################################
        # check if a word exeeds the set sizeX/sizeY-grid size
        ##########################################################

        for w in self.words:
            if w.inRange:
                self.fitness += fit.INBOUND
                self.wrdInBound += 1
            else:
                self.fitness += fit.OUTOFBOUND
                self.wrdOutOfBound += 1


            ### CHECK OVERLAP CHARS AND CREATE GRID SUMMARY ##########
            #  
            ##########################################################
            #create a set of intersecting positions and rank them
            
            _intersections=self.grid.keys() & w.grid
            for i in _intersections:
                if self.grid[i]==w.grid[i]:
                    #intersection with matching text values (letter)
                    self.fitness += fit.INTERSECTIONPOS
                    self.intValid += 1
                else:
                    #intersection with missmatching text values (letter)
                    self.fitness += fit.INTERSECTIONNEG
                    self.intInValid += 1
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

    def mutate_push_coordinate(self):
        #random coordinate
        mWord = random.randrange(wordlist.lenght)
        xm,ym = random.choice([[1,0],[-1,0],[0,1],[0,-1]])
        xc,yc = self.words[mWord].coordinate
        newX,newY = xc+xm, yc+ym
        if newX < 0 or newX > xSize: newX = xm
        if newY < 0 or newY > ySize: newY = ym

        mutant = self.clone()
        mutant.words[mWord].coordinate = [newX,newY]
        #print("MUTATEEEE")
        return mutant.clone()

    def mutate_mod_direction(self):
        #random coordinate
        mWord = random.randrange(wordlist.lenght)
        dir = random.choice(direction.directions)
        mutant = self.clone()
        mutant.words[mWord].dir=dir
        #print("MUTATEEEE")
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
        m = random.choice( [
                            #self.mutate_random_cordinate,
                            self.mutate_swap_words,
                            self.mutate_push_coordinate,
                            self.mutate_mod_direction,
                            self.mutate_close_swap_words
                            ])
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
