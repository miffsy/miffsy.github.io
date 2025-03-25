def nah(huh,whuh):
    match whuh:
        case "0":
            print("\""+huh+"\" is invalid, please use numeric input (1-7)")
        case "1" | "2" | "3" | "3" | "4" | "5":
            print("\""+huh+"\" is invalid, please use numeric input (1-11)")
        case "6":
            print("\""+huh+"\" is invalid, please use numeric input (1-4)")
        case "7":
            print("\""+huh+"\" is invalid, please enter a number")
        case "8":
            print("\""+huh+"\" is invalid, please enter a positive number")
        case "9":
            print("\""+huh+"\" is invalid, please use numeric input (1-5)")