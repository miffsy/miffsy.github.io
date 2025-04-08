import textwrap
import WorldDict
import time
import curses
from curses import wrapper

UprWHeight = 20 #Heights of windows
LwrWHeight = 5

GraDef00 = [] #Holds defaults for GraCch to save on re-running the setup loop or having a massing ugly list in the code
GraDef01 = "|                                                                   |" #Default graphical blocks
GraDef02 = "x - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - x" 
GraDef03 = "|0000000000000000000000000000000000000000000000000000000000000000000|" 
GraDef04 = "x - - - - - - - - - - - - - - - - - - - x - - - - - - - - - - - - - x"
GraDef05 = "|                                       |                           |"
GraDef06 = "                                                                  "
GraDef07 = ([GraDef06] * UprWHeight) #Default visual window area 5x66 # not 67 because newline causes addstr error, and the alternative is overwriting borders etc
GraDef08 = "                                      "
GraDef09 = ([GraDef08] * LwrWHeight) #Default dialogue window area 5x39 #" "
GraDef10 = "                          "
GraDef11 = ([GraDef10] * LwrWHeight) #Default menu window area 5x27 # " "

GraDef00 = [GraDef02] + ([GraDef01] * UprWHeight) + [GraDef04] + ([GraDef05] * LwrWHeight) + [GraDef04] #Most compact/fast way to "store" default borders
GraDef12 = "                                                                 "
GraDef13 = " [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ] "
GraDef14 = " [ ]   [ ]   [ ]   [ ]   [ ]   [ ]   [ ]   [ ]   [ ]   [ ]   [ ] "
#             S     1     2     3     4     5     6     7     8     B     E
GraDef15 = ([GraDef12] * 9) + [GraDef13] + [GraDef14] + ([GraDef12] * 9)

boxsize1 = 35 #Acceptable width for dialogue box
boxsize2 = 25 #Menu width
boxsize3 = 67 #Visuals width
boxsize4 = 3 #Menu/Dialogue height
boxsize5 = 20 #Visuals height

def BasicBorders(): #Returns layout of default window/borders

    dlim = "\n"
    
    return dlim.join(GraDef00)

def GO(godata, uidata):
    def showme(stdscr):
        inputdict = {87: 'W',119: 'w', 65: 'A',97: 'a', 83: 'S',115: 's', 68: 'D',100: 'd', 32: ' ',}
        curses.curs_set(0)  # Hide the cursor
        stdscr.nodelay(1)   # Non-blocking input
        stdscr.timeout(50)
        stdscr.clear() #empties what's in so it doesn't just append
        stdscr.addstr(BasicBorders()) #Sets the border/background
        stdscr.refresh() #show borders
        dw = curses.newwin(5,39,22,1) #dialogue window
        dw.nodelay(1)   # Non-blocking input
        dw.timeout(50)
        mw = curses.newwin(5,27,22,41) #menu window
        mw.nodelay(1)   # Non-blocking input
        mw.timeout(50)
        vw = curses.newwin(20,67,1,1) #menu window
        vw.nodelay(1)   # Non-blocking input
        vw.timeout(50)
        Loutput = "" #placeholder to prevent repeat outputs ig

        while True:
            npt = stdscr.getch() #hey press
            if npt in [ord(x) for x in ["W","w","A","a","S","s","D","d"," "]]:   #make list of keycode for each 1 char string, check if npt matches any
                                                                                #doing it this way so I don't need to update by personally referencing a key map
                                                                                #plus this may work in multiple terminals or whatever
                                                                                #should I use a dict entry? then I can have conditional valid inputs..
                chnpt = chr(npt)
                uidata.put(chnpt, block=False) #queue value corresponding to ch's key code
                time.sleep(0.01)
            if (npt == ord("q")):
                gmem = "Goodbye"
                vw.clear()
                vw.addstr(0,0,f"{gmem}")
                vw.refresh()
                curses.endwin()
                try:
                    uidata.put(chr(npt), block=False)
                except:
                    pass
                time.sleep(0.05)
                break
            else:
                if not godata.empty():
                    #dw.addstr(0,0,"Hello, world!", curses.A_BOLD) #figuring out how this works even
                    gmem = godata.get_nowait() #grab inputs
                    if gmem != Loutput:
                        match gmem[1]:
                            case 1:
                                dw.clear()
                                dw.addstr(0,0,MakeItSo(gmem[0],gmem[1],gmem[2]))#send inputs to formatter, receive formatted text #unsure how to pass varying numbers of list items as individual things
                                dw.refresh()
                            case 2:
                                mw.clear()
                                mw.addstr(0,0,MakeItSo(gmem[0],gmem[1],gmem[2]))
                                mw.refresh()
                            case 3:
                                vw.clear()
                                vw.addstr(0,0,MakeItSo(gmem[0],gmem[1],gmem[2]))
                                vw.refresh()
                        Loutput = gmem
            time.sleep(0.01)
        
    wrapper(showme)

def Selected(a,b):
    select1 = "[▶]" #icons for menu selection
    select2 = "[ ]"
    if a == b:
        return select1
    else:
        return select2

def MakeItSo(*args): #This takes strings fetched from WD and formats them for each window. It will take more arguments in future.

    length1 = len(args) #number of arguments passed  
    if length1 > 1: #if args were received

        n = args[1] #window choice arg handling placeholder
        
        match n: #checking window being handled
            case 1:
                GraCch = [] + GraDef09 #Graphics "memory" set to blank defaults #Unsure why just doing = GraDef00 isn't working, it's like GraDef00 is updated and instead of GraCch being separately accessed
                boxsizea = boxsize1 #sets formatting based on window height
                boxsizeb = boxsize4 #and width
                fetcher1 = args[0] #fetches dialogue
                wrap1 = textwrap.TextWrapper(width=boxsizea) #wrapper function set to boxsize
                dedent1 = textwrap.dedent(fetcher1) #dedents fetched dialogue
                boxtextlist = wrap1.fill(dedent1) #wraps dedented dialogue to boxsize
                boxtextlist = boxtextlist.splitlines() #splitting it into suitable lines?
                length2 = len(boxtextlist) #number of lines dialogue takes up #I kind of want this whole thing to be able to receive multiple lines to simplify WorldDict

                for i in range(length2): #for each line to be added to the window
                    j = len(boxtextlist[i]) #length of specific line
                    GraCch[1+i] = GraCch[1+i][:2] + boxtextlist[i] + GraCch[1+i][j+2:] #This should replace the chunk of the cache's string with another, apparently necessary because strings are immutable?

            case 2:
                cplace = args[2] #cursor position, function needs some fleshing out #calculate position based on arrow input...
                GraCch = [] + GraDef11
                boxsizea = boxsize2
                boxsizeb = boxsize4
                fetcher1 = [] + args[0] #might need to address this duplication
                for i in range(len(fetcher1)):
                    fetcher1[i] = Selected(cplace,i) + fetcher1[i] + " "
                GraCch[1] = "  " + fetcher1[0] + ((12-len(fetcher1[0])) * " ") + fetcher1[1] + ((11-len(fetcher1[1])) * " ") #Setting the menu pieces on their own lines, adjusting for option length
                GraCch[3] = "  " + fetcher1[2] + ((12-len(fetcher1[2])) * " ") + fetcher1[3] + ((11-len(fetcher1[3])) * " ")
                #27 width box: 2 + option + 1 + option + 2

            case 3:
                GraCch = [] + GraDef07
                boxsizea = boxsize3
                boxsizeb = boxsize5
                #visuals "engine" stuff goes here ig
                spc = " " #placeholder stuff
                GraCch[0] = spc.join(args[0])

        
    
    #I need to figure out how to get the menu items in the right spot
    delimiter = "\n"
    
    return delimiter.join(GraCch)
