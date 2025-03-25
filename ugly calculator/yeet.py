import nope

def yote(menuselect,temp):
    options = "1"
    while options != "4":
        print("\nOptions Menu")
        print("1) Memory (prints up to last 10 calculations")
        print("2) Save/Load")
        print("3) Return to main menu")
        print("4) Quit\n")
        options = input("Please make a selection: ")
        match options:
            case "1":
                
                if len(temp) > 0:
                    
                    for i in range(len(temp)):
                        print("Operation",i+1)
                        match temp[i][0]:
                                
                            case 1:
                                print("\nAdded the following variables:")
                                print(temp[i][2:(2+temp[i][1])])
                                print("Resulting in: "+str(temp[i][12])+"\n")
                            case 2:
                                print("\nTook",str(temp[i][2]),"and subtracted the following variables:")
                                print(temp[i][3:(3+(temp[i][1]-1))])
                                print("Resulting in: "+str(temp[i][12])+"\n")
                            case 3:
                                print("\nFound the product of the following variables:")
                                print(temp[i][2:(2+temp[i][1])])
                                print("Resulting in: "+str(temp[i][12])+"\n")
                            case 4:
                                print("\nDivided",str(temp[i][2]),"by the following variables, in order:")
                                print(temp[i][3:(3+(temp[i][1]-1))])
                                print("Resulting in: "+str(temp[i][12])+"\n")
                            case 5:
                                print("\nFound the roots of the following variables:")
                                for c in range(temp[i][1]):
                                    print(str(temp[i][2+c]),"resulting in",str(temp[i][12+c]))

                else:
                    print("\nNothing in memory!")
                    
            case "2":
                sl = "1"
                while sl != "5":
                    print("\nSave/Load menu:")
                    print("1) Save memory to file")
                    print("2) Load file to memory")
                    print("3) Return to Options Menu")
                    print("4) Return to Main Menu")
                    print("5) Quit")
                    print("Note that 1 and 2 will overwrite their respective destinations.")
                    sl = input("Please make a selection: ")
                    
                    match sl:
                        case 1:
                            temp = temp
                        case 2:
                            temp = temp
                        case 3:
                            options = "1"
                            menuselect = "1"
                        case 4:
                            options = "4"
                            menuselect = "1"
                        case 5:
                            print("\nGoodbye!\n")
                            menuselect = "7"
                        case _:
                            nope.nah(sl,"9")
            case "3":
                options = "4"
                menuselect = "1"
                
            case "4":
                print("\nGoodbye!\n")
                menuselect = "7"
                
            case _:
                nope.nah(options,"6")
                
    return menuselect, temp