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
        self.grandIndex=index
        if fromList is not None:
            self.words= fromList       
        else:
            self.words= [word.fromRandom(txtGrp=w) for w in wordlist.lst]       
 
        ind.track(self)

    def clone(self):
        return eval(repr(self))



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
        ind.instances[word.iCount] = s
    @classmethod
    def printTracking(c):
        for k in ind.instances:
            print(k,word.instances[k])
