import math
import decimal
import collections
import GraphicalOutput
import multiprocessing
import sys
import time
import WorldDict
from Combat import battlecalc,enemymove
from GraphicalOutput import GO
from multiprocessing import active_children
from WorldDict import GiveDialogue

def menuwasd(userinput,currentpos):
        if userinput in ["w","a","s","d"]: #if input corresponds to a direction
            locations = [[0,1], #2d array of cursor locations
                         [2,3]]
            coorddict = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)} #y and x changes to move across menu array(locations)
            flat = len(locations) #length of flattened array
            sub = len(locations[0]) #length of sub array
            
            oldy,oldx = divmod(currentpos,sub) #1D position to 2D
            shifty, shiftx = coorddict[userinput] #assigning movement values from d to individual ints
            newy = (oldy + shifty) % flat #find new vertical position but letting movement wrap around
            newx = (oldx + shiftx) % sub # "" buthorizontal
            return locations[newy][newx] #return new position           
        else:
            return currentpos #if some rubbish was input, just keep the cursor where it was
    
def gameinput(gamestate, dialogue, godata, uidata, gi, mmenu, dialoguelist, player, enemies, bttl, bttlchoice, bttlstage):

    last = 0 #previous time
    slep = 0.2 #timeout
    ccurpos = 0 #menu cursor position
    l = False #progressor bool
    inputqueue = uidata
     #on 3rd menu in index

    if gamestate == "Battle":
        #print(bttlstage)
        menustate = GiveDialogue(mmenu[bttlstage+1])
        print("gameinput",gamestate)
        while l == False: 
            now = time.time()
            if ((now - last) > slep): #if slep time has passed
                bttlchoice, bttlstage, ccurpos = gameoutput(gamestate, dialogue, ccurpos, godata, "", mmenu, dialoguelist, player, enemies, bttl, bttlchoice, bttlstage)
                print("still running")
                last = now
            if not inputqueue.empty():
                gi = inputqueue.get_nowait()
                print("debug gi",gi)
                if gi == "q":
                    gamestate = "Quit"
                    break
                if gi == " ":
                    print("debug menustate 2",menustate)
                    bttlchoice = menustate[ccurpos] #this is an issue
                    print("debug bttlchoice",bttlchoice)
                    if bttlchoice == "Quit":
                        print("Weird exit") #This is shouldn't be available
                        break
                    l = True
                bttlchoice, bttlstage, ccurpos = gameoutput(gamestate, dialogue, ccurpos, godata, gi, mmenu, dialoguelist, player, enemies, bttl, bttlchoice, bttlstage)
            else: time.sleep(0.01)
        return bttlchoice,bttlstage,gamestate
    elif gamestate == "Main":
        menustate = GiveDialogue(mmenu[dialogue+1])
        print("gameinput",gamestate)
        while l == False: 
            now = time.time()
            if ((now - last) > slep): #if slep time has passed
                gamestate, dialogue, ccurpos = gameoutput(gamestate, dialogue, ccurpos, godata, "", mmenu, dialoguelist, player, enemies, bttl, bttlchoice, bttlstage)
                #print("still running")
                last = now

            if not inputqueue.empty():
                gi = inputqueue.get_nowait()
                
                if gi == "q":
                    gamestate = "Quit"
                    break
                    
                if gi == " ":
                    gamestate = menustate[ccurpos]
                    
                    if gamestate == "Quit":
                        print("Main menu exit") #This isn't working
                        break
                    l = True
                gamestate,dialogue,ccurpos = gameoutput(gamestate, dialogue, ccurpos, godata, gi, mmenu, dialoguelist, player, enemies, bttl)
            else: time.sleep(0.01)
        return gamestate,dialogue

def gameoutput(*args): #rework this so repeated code is lessened and redundant assignment is lessened
        gamestate = args[0]
        dialogue = args[1]
        ccurpos = args[2]
        outputqueue = args[3]
        keyinput = args[4]
        mmenu = args[5]
        dialoguelist = args[6]
        Lput = [] #default for preventing redundant refreshes

        print("gameoutput",gamestate)

        
        match gamestate:
            case "Battle":
                playerstate = args[7]
                enemystate = args[8]
                battlestate = args[9]
                bttlchoice = args[10]
                bttlstage = args[11]
                if keyinput in ["W","w","A","a","S","s","D","d"]:
                    ccurpos = menuwasd(keyinput,ccurpos)
                    print("wasd")
                    outputqueue.put([GiveDialogue(mmenu[bttlstage+1]),2,ccurpos]) #send dict entry,menu type, and cursor position to output queue
                elif keyinput == " ":
                    print("debug gameoutput bttlstage:",bttlstage)
                    #outputqueue.put([GiveDialogue(dialoguestate[bttlstage+1]),1,ccurpos])
                    outputqueue.put([GiveDialogue(mmenu[bttlstage+1]),2,ccurpos])
                else:
                    outputqueue.put([GiveDialogue(mmenu[bttlstage+1]),2,ccurpos])
                return bttlchoice, bttlstage, ccurpos
            case "Main":  
                if keyinput in ["W","w","A","a","S","s","D","d"]:
                    ccurpos = menuwasd(keyinput,ccurpos)
                    outputqueue.put([GiveDialogue(mmenu[dialogue+1]),2,ccurpos]) #send dict entry,menu type, and cursor position to output queue

                elif keyinput == "q":

                    gamestate = "Quit" #this shouldn't be reached
                    time.sleep(0.2)
                    return gamestate,dialogue,ccurpos
                elif keyinput == " ":
                    print("fix this")
                else:    #this is for the default refreshes
                    outputqueue.put([GiveDialogue(dialoguelist[dialogue+1]),1,ccurpos])
                    outputqueue.put([GiveDialogue(mmenu[dialogue+1]),2,ccurpos])
                    #outputqueue.put([GiveDialogue(dialoguestate[dialogue+1]),1,ccurpos])
                    #use dict key from mmenu to grab dialogue, send dialogue menu type and cursor position to GO #structure is wrong atm
            case "New" |"Next":

                selec = dialoguelist[dialogue]

                Nput = [] + [GiveDialogue(selec),1,ccurpos]

                #outputqueue.put(Nput)
                #dialogue += 1
                time.sleep(0.05)
                #dialogue +=1  #this isn't right probably
            case "Play":
                time.sleep(0.05)

        return gamestate,dialogue,ccurpos

def game(godata,uidata):

    gamestate = "Battle" #mode choice #this should say Main unless testing a mode
    bttl = GiveDialogue("BIN001") #battle index
    enemies = []
    mmenu = GiveDialogue("MIN001") #menu index
    player = GiveDialogue("YOU001")
    dialoguelist = GiveDialogue("PRO001") #progress index
    dialogue = 1
    xcoord = 0
    ycoord = 0
    
    while (gamestate != "Quit"): #while game should be running
        if gamestate == "Main": #if in the main menu

            gamestate,dialogue = gameinput(gamestate, dialogue, godata, uidata, "", mmenu, dialoguelist, player,enemies,bttl)
            dialogue += 1
        
        elif gamestate == "Load": #I may shove some of the beginning stages here and have separate dict key lists per stage
            k = 0

            godata.put([GiveDialogue(dialoguelist[dialogue]),1,k])
            godata.put([GiveDialogue(mmenu[6]),2,k]) #gives GO window key for WD, window type, and cursor position

            while gtspc != " ":
                #gtspc = dw.getch()
                if gtspc == 32:
                    gtspc = " "
            
            time.sleep(0.2)

        elif (gamestate == "New") | (gamestate == "Next"): 
            gamestate,dialogue = gameinput(gamestate, dialogue, godata, uidata, "", mmenu, dialoguelist, player,enemies,bttl)


        elif gamestate == "Play":
            xcoord = 0
            ycoord = 0
            gamestate,dialogue = gameinput(gamestate, dialogue, godata, uidata, "", mmenu, dialoguelist, player,enemies,bttl)

        elif gamestate == "Battle":

            encounter = GiveDialogue(bttl[0]) #replace default 0 with in-game progress
            enemies = [] + [GiveDialogue(x) for x in encounter] #assign enemy list to battle

            winner = 0 #default zero for battle winner

            turn = 2
            bttloption,bttlmove,enmtarget = 4,4,4 #default outside to activate menu
            bttlplayer = player #fetch player base stats #will replace with mutable after setting up levelling and locale and save

            while True: #should say While True
                #i = "Main" #DEBUG
                #break #DEBUG
                if (turn %2) == 0: #even is your turn

                    bttloption = 4
                    while bttloption == 4:
                        bttlstage = 6 #this loads the right menu options
                        bttloption,bttlstage,gamestate = gameinput(gamestate, dialogue, godata, uidata, "", mmenu, dialoguelist, player, enemies, bttl, bttloption, bttlstage)
                        if gamestate == quit:
                            return 0
                        match bttloption:   
                            case "Attack":
                                #print("debug 191")
                                bttlmove = 4
                                while bttlmove == 4:
                                    bttlstage = 7
                                    bttlmove,bttlstage,gamestate = gameinput(gamestate, dialogue, godata, uidata, "", mmenu, dialoguelist, player, enemies, bttl, bttlmove, bttlstage)
                                    if gamestate == quit:
                                        return 0
                                    #godata.put([GiveDialogue(mmenu[8]),2,k]) #need to figure out intputout options here
                                    #print("debug 197")
                                    match bttlmove:
                                        case "Back":
                                            bttloption = 4
                                            break #return to previous menu
                                        case "Jab" | "Bludgeon" | "Special":
                                            #print("debug 203")
                                            attack = {'Jab' : 0, 'Bludgeon' : 1, 'Special' : 2}                                                              
                                            enmtarget = 4
                                            while enmtarget == 4:
                                                bttlstage = 7
                                                bttlstage += len(enemies) #to get menu 9, 10, or 11
                                                enmtarget,bttlstage,gamestate = gameinput(gamestate, dialogue, godata, uidata, "", mmenu, dialoguelist, player, enemies, bttl, enmtarget, bttlstage)
                                                if gamestate == quit:
                                                    return 0
                                                match enmtarget:
                                                    case "One" | "Two" | "Three":
                                                        victim = {'One' : 0,'Two' : 1,'Three' : 2}
                                                        bttlplayer, enemies[victim[enmtarget]] = battlecalc(bttlplayer,enemies[victim[enmtarget]],attack[bttlmove]) #input player, enemy target, move selection #update based on selection
                                                        #print("debug 211")
                                                        if enemies[victim[enmtarget]][7] <= 0: #if target died
                                                            print("debug 195")
                                                            bttlplayer[15] += enemies[victim[enmtarget]][15]
                                                            print("debug 197")
                                                            enemies.pop(victim[enmtarget]) #remove dead enemies
                                                            print("debug 199")
                                                            #print("Enemies remaining at this time:",enemies)
                                                        if bttlplayer[7] <= 0: #if you died, eg bludgeoning while low health
                                                            break
                                                        turn += 1 #move is made, change turn

                                                    case "Back":
                                                        bttlmove = 4
                                                        break #return to previous menu
                                                    case _: print("Enemy Target:",enmtarget,"Turn:",turn,".")
                                        case _: print("Battle Move:",bttlmove,"Turn:",turn,".")            

                            case "Item":
                                time.sleep(0.05) #item menu goes here
                                itemchosen = 4
                                bttlmove,bttloption = 4 #yeah so this isn't implemented yet
                            case "Menu": 
                                bttlmove,bttloption = 4
                                time.sleep(0.05) #I'm not actually sure what I'd put here for a menu
                            case "Flee":
                                time.sleep(0.1)
                            case _: print("Battle Option:",bttloption,"Turn:",turn,".")

                else:
                    for enmturn in enemies: #enemies attack one by one
                        #enemy chooses move from moveset randomly #bosses get 2 specials
                        #mana/stamina costs applied here
                        enmmove = enemymove(0,enemies[enmturn-1][14],0) #enemy type (game only has 3 attacks right now so whatever, 0), has special available or not, weapon (not yet implemented)?
                        enemies[enmturn-1],bttlplayer = battlecalc(enemies[enmturn-1],bttlplayer,enmmove) 
                        if enemies[enmturn-1][7] <= 0:
                            enemies.pop(enmturn-1)
                            time.sleep(0.2)
                        #Combat.py function here updating entity states based on return values
                    turn += 1
                #print("debug 246")
                if bttloption == "Flee":
                    #godata.put([GiveDialogue("ERR001"),1,k]) #needs its own error state and solution
                    winner = 4
                    break 
                else:                             
                    if len(enemies) == 0:
                        if bttlplayer[7] > 0:
                            winner = 1
                            break
                        else:
                            winner = 3
                            break
                    else:  
                        if bttlplayer[7] > 0:
                            #various regens go here for end of round
                            turn += 1
                        else:
                            winner = 2
                            break

            #print("debug 267")
            match winner:
                case 0:
                    time.sleep(0.5)
                    gamestate = "Main" #This should be "Play" but I need to debug it
                case _:
                    player = bttlplayer
                    match winner:
                        case 1:
                            #return to previous location
                            gamestate = "Main" #Player win code goes here #this should say Play not Main
                            time.sleep(1) 
                        case 2:
                            #respawn
                            gamestate = "Main"
                            time.sleep(1) #Enemies win
                        case 3:
                            #respawn
                            gamestate = "Main"
                            time.sleep(1) #draw somehow
                        case 4:
                            #return to previous location
                            gamestate = "Main"
                            time.sleep(1) #flee
                        case _: print(f"Winner:{winner} Turn: {turn}.",winner,turn)
    
                #godata.put([GiveDialogue("ERR001"),1,k]) #needs its own error state and solution
        else: gamestate = "Main"  #I am using this to debug the while loop



if __name__ == "__main__":
    godata = multiprocessing.Queue(maxsize=3) #memory of stuff to be processed by GraphicalOutput.py
    uidata = multiprocessing.Queue(maxsize=3) #memory of user input to be processed
    print("Loading...")
    time.sleep(0.05)
    gothread = multiprocessing.Process(target=GO,args=(godata,uidata,))
    gothread.start()

    try:
        game(godata,uidata)
    except:
        print("Quitting..")
        gothread.terminate()

    finally:
        gothread.join()
        godata.close()
        godata.join_thread()
        uidata.close()
        uidata.join_thread()
        print("Thanks for playing!")
        if gothread.is_alive():
            print("Graphics still running...")
        children = active_children()
        if children:
            print("Cleaning up...")
            sys.exit(0)