
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
