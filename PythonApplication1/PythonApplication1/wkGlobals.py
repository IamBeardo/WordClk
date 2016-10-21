
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
        lenght=len(wl)


class fit():
    OUTOFBOUND = -100
    INBOUND = 10
    INTERSECTIONPOS = 33
    INTERSECTIONNEG = -222
    GROUPORDERPOS=44
    GROUPORDERNEG=-555


class evolution():
    OVERPOPULATION=0
    ELITISM=1

    RANDOMPOPULATION=1
    MAXKIDS=5

    TOURNAMENT=1
    TOUR_SIZE=3

    MUTATIONRATE=0.1 
    MUT_MOD_XY=0
    MUT_MOD_DIR=0
    MUT_PUSH_DIR=0
    MUT_SWAP_POS=0
    MUT_SHIFT_SECTION=0