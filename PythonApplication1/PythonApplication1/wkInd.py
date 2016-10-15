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
    def __init__(self,index=-1,grandIndex=-1):
        self.fitness=None
        self.index=index
        self.grandIndex=index
        self.words= [word.fromRandom(w) for w in wordlist.lst]       
 
 
        ind.track(self)





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
