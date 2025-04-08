everything = {
                'ANY001' : 'Press any key to begin...', 
                'ANY002' : 'Press any key to continue...',

                'SPC001' : 'Press space to advance...',
                'SPC002' : 'Press space to search',

                'PRO001' : ["","ANY001","MDI001","STG001","STG002","STG003","SPC002","STG004","STG005","FND001","STG006","STG007","STT001","STG008"], #INDEX

                'MDI001' : '~Main Menu~                     Please select an option (space/wasd):',

                'STG000' : '                                                                                               ', #Max length to neatly wrap 3 dialogue within 3 dialogue box lines
                'STG001' : 'You awaken in a dimly-lit room...    (Press space to advance)',
                'STG002' : 'Your head throbs and you can\'t remember how you got here...',
                'STG003' : 'Your foot is itching terribly and... oh god WHERE IS YOUR FOOT!?',
                'STG004' : 'You look frantically for your missing appendage...',
                'STG005' : 'In the corner, a pool of presumably your own blood',
                'STG006' : 'You grab it, and in a desperate panic, attempt to re-attach your foot',
                'STG007' : 'Slowly.. surely not.. it works? Not only that, you feel revitalized...',
                'STG008' : 'Not one sign of injury remains. With the headache clearing, you try to stand.',

                'FND001' : 'You have found... your foot!',

                'STT001' : 'Reunited at last:             Health regen +1! Congrats!!!',

                'MIN001' : ["","","MNU001","MNU002","MNU003","MNU004","MNU005","MNU006","MNU007","MNU008","MNU009","MNU010","MNU011"], #INDEX

                'MNU001' : ["New","Load","Settings","Quit"], 
                'MNU002' : ["Next","◼◼◼◼","◼◼◼◼","◼◼◼◼"],
                'MNU003' : ["Action","Gear","Items","Menu"],
                'MNU004' : ["A","B","C","D"],
                'MNU005' : ["Slot 1","Slot 2","Slot 3","Back"],
                'MNU006' : ["Attack","Item","Menu","Flee"], #consumable items not yet implemented #how do I code for AOEs...
                'MNU007' : ["Jab","Bludgeon","Special","Back"],
                'MNU008' : ["One","Back","Back","Back"],
                'MNU009' : ["One","Two","Back","Back"],
                'MNU010' : ["One","Two","Three","Back"],
                'MNU011' : ["Battle","Two","Three","Back"],

                'YOU001' : [1,5, 0,75,5,50,30,30,0,1, 0, 0,0,0,1,"You","Ordinary, aside from the foot"],
                            #level  basedam boost   acc critch  critmult    maxhealth   current health  armor   health  health regen    max mana    current mana    mana regen  special available xp  name    description
                            #0      1       2       3   4       5           6           7               8       9       10              11          12              13          14                15  16      17
                'SLM001' : [1,5, 0,75,0, 0,20,20,0,1, 0, 0,1,0,1,"Green slime","A green slime made of mold and ooze"],  #I may not bother adding items to enemies yet
                'SLM002' : [1,7, 0,80,5,10,25,25,0,2, 0, 0,2,0,1,"Red slime","A red slime made of yet more mold and ooze"],
                'SLM002' : [1,10,0,82,5,25,30,30,0,3,10,10,3,1,1,"Purple slime","A purple slime, it appears to glow"],

                'BIN001' : ["BTL001","BTL002","BTL003","BTL004","BTL005","BTL006","BTL007","BTL008"], #INDEX

                'BTL001' : ["SLM001"],
                'BTL002' : ["SLM001","SLM001"],
                'BTL003' : ["SLM002","SLM001"],
                'BTL004' : ["SLM002","SLM002"],
                'BTL005' : ["SLM001","SLM001","SLM001"],
                'BTL006' : ["SLM003","SLM001","SLM001"],
                'BTL007' : ["SLM003","SLM002","SLM001"],
                'BTL008' : ["SLM003","SLM003","SLM001"], #I think that I either add XP based on individual enemies killed, or encounters cleared #but I don't want this to be grindy

                'ERR001' : 'Error in loop structure, resolving...',
                
                'BYE001' : ["Goodbye","for","now","..."]


             }

def GiveDialogue(choice):
    return everything[choice]

#This works but internalizing it was tricky