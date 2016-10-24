
apa=10
xSize=15
ySize=15


class direction():
    LEFT = [1,0]
    LEFTDOWN = [1,1]
    DOWN = [0,1]
    directions=[LEFT,LEFTDOWN,DOWN]


class wordlist(object):
    lst=[]
    lenght=0
    def set(wl):
        wordlist.lst=wl
        wordlist.lenght=len(wl)


class fit():
    OUTOFBOUND = 0
    INBOUND = 0
    INTERSECTIONPOS = 0
    INTERSECTIONNEG = 0
    GROUPORDERPOS=321
    GROUPORDERNEG= 123


class evolution():
    OVERPOPULATION=0
    ELITISM=1

    RANDOMPOPULATION=0
    MAXOFFSPRING=3

    TOURNAMENT=1
    TOUR_SIZE=2

    #Minimal procentage of gens from each parents
    CROSSPOINTBOUNDERY=0.1

    MUTATIONRATE=0.10
    MUT_MOD_XY=0
    MUT_MOD_DIR=0
    MUT_PUSH_DIR=0
    MUT_SWAP_POS=0
    MUT_SHIFT_SECTION=0