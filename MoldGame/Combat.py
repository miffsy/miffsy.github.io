import math
import decimal
import random
from random import randint

#level  basedam boost   acc critch  critmult    maxhealth   current health  armor   health  health regen    max mana    current mana    mana regen  special available xp  name    description
#0      1       2       3   4       5           6           7               8       9       10              11          12              13          14                15  16      17

def battlecalc(a,b,c): #attacker, enemy, move chosen, later there will be environment variable e
    basedam = a[1]

    match c:
        case 0:
            boost = a[2]
            acc = a[3]
            critch = a[4]
            critmult = a[5]
            enmarm = b[8]
        case 1:
            boost = a[2] + 20
            acc = a[3]
            critch = a[4] + 3
            critmult = a[5]
            enmarm = b[8] * .99
        case 2:
            boost = a[2] + 35
            if a[3] > 95: #boost accuracy by 5 if possible
                acc = 100
            else:
                acc = a[3] + 5
            critch = a[4] + 10
            critmult = a[5] + 15
            enmarm = b[8] * .9

    dealt = Damage(basedam,boost,acc,critch,critmult,enmarm)
    #print("debug35")
    if c == 1:
        blowback = dealt/10
        a[7] = a[7] - blowback
    if c == 2:
        a[12] = a[12] - 5
    b[7] = b[7] - dealt
    #mana/stamina costs applied here

    return a,b

def Damage(basedam,boost,acc,critch,critmult,enmarm):
    #print("debug47")
    roll = randint(1,100)
    if roll < (100-acc):
        basedam = 0
    elif roll > (100-critch):
        basedam = (basedam * (1-(critch/100))) + (basedam * (critch/100) * (critmult/100))
        basedam = basedam + (basedam * (boost/100))
    else:
        basedam = basedam + (basedam * (boost/100))
    return basedam - enmarm

def enemymove(a,b,c):
    #a enemy type
    #b has used special already
    #c weapon type
    if b == 0:
        d = randint(1,2)
    else:
        d = randint(1,3)
    return d

#This all works