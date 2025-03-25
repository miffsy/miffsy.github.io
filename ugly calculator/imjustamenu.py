import nope
import trans
import yeet

def calcmenu():
    menuselect = "1"
    temp = []
    while menuselect != "7":
        print("\n1) Addition +")
        print("2) Subtraction -")
        print("3) Multiplication x")
        print("4) Division ÷")
        print("5) Square root √")
        print("6) Options ~")
        print("7) Quit ☹")
        menuselect = input("Please make a selection: ")

        def choice(ye):
            match ye:
                case "1":
                    ye = "Addition!"
                case "2":
                    ye = "Subtraction!"
                case "3":
                    ye = "Multiplication!"
                case "4":
                    ye = "Division!"
                case "5":
                    ye = "Square root!"
            return ye        
            
        def calc(menu):
            calcselect = "1"
            while calcselect != "11":
                calcselect = input("Please select a number of variables (1-10), or 11 to quit: ")
                match calcselect:
                    case "1" | "2" | "3" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10":
                        print("\nYou selected: ",calcselect,"\n")
                        temp.append(trans.lesbian(menu,calcselect))
                        yn = input("Would you like to perform another operation? (y/n): ")
                        match yn:
                            case "y":
                                menu = "1"
                                calcselect = "11"
                            case "n":
                                print("\nGoodbye!\n")
                                menu = "7"
                                calcselect = "11"
                            case _:
                                print("\nPlease select y or n: \n")
                    case "11":
                        print("\nGoodbye!\n")
                        menu = "7"
                    case _:
                        nope.nah(calcselect,menu)
            return menu
        
        match menuselect: 
            case "1" | "2" | "3" | "4" | "5":
                print("\nYou selected:",choice(menuselect),"\n")
                menuselect = calc(menuselect)
            case "6":
                menuselect, temp = yeet.yote(menuselect,temp)
            case "7" | "Seven" | "seven":
                print("\nGoodbye!\n")
            case _:
                nope.nah(menuselect,"0")
                menuselect = "1"