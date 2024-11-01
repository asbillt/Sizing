import Classes

#Take user input to determine which equipment will be sized
userInput = input("What equipment do you want to size?\n"
                  "Type \"PV\" for Pressure Vessel\n"
                  "Type \"P\" for Pump\n"
                  "Type \"HEX\" for Heat Exchanger\n"
                  "Type \"C\" for Compressor\n"
                  "Type \"PSV\" for Pressure Safety Valve\n")

match userInput:
    case "PV":
        pressureVessel = Classes.PressureVessel()
        #Take user input to determine which Pressure Vessel calculation will be run
        userInputPV = input("What calculation do you want to run?\n"
                            "For UG-27(c)(1) Minimum Required Thickness of Shell under Internal Pressure type \"shell\" \n"
                            "For UG-32(c)(1) Minimum Required Thickness of Ellipsoidal Head under Internal Pressure type \"head\" \n"
                            "For UG-40 Limits of Reinforcement type \"limit\" \n")
        #Calculate minimum required thickness for shell/head, MAWP and MAP
        match userInputPV:
            case "shell":
                P = input("Enter design pressure in psi: ")
                R = input("Enter inside radius in inches: ")
                S = input("Enter allowable material stress in psi: ")
                E = input("Enter joint efficiency: ")
                CA = input("Enter corrosion allowance in inches: ")
                shell, MAWP, MAP = pressureVessel.shell(int(P), int(R), int(S), float(E), float(CA))
                print("Shell Minimum Required Thickness: " + str(shell) + " inches")
                print("MAWP: " + str(MAWP) + " psi")
                print("MAP: " + str(MAP) + " psi")
            case "head":
                P = input("Enter design pressure in psi: ")
                D = input("Enter inside diameter in inches: ")
                S = input("Enter allowable material stress in psi: ")
                E = input("Enter joint efficiency: ")
                CA = input("Enter corrosion allowance in inches: ")
                head, MAWP, MAP = pressureVessel.head(int(P), int(D), int(S), float(E), float(CA))
                print("Head Minimum Required Thickness: " + str(head) + " inches")
                print("MAWP: " + str(MAWP) + " psi")
                print("MAP: " + str(MAP) + " psi")
            case "limit":
                P = input("Enter design pressure in psi: ")
                R = input("Enter inside radius in inches: ")
                S = input("Enter allowable material stress in psi: ")
                E = input("Enter joint efficiency: ")
                CA = input("Enter corrosion allowance in inches: ")
                NS = input("Enter nozzle size in inches: ")
                parallel_limit = pressureVessel.limit(int(P), int(R), int(S), float(E), float(CA), float(NS))
                print("The Parallel Limit of Reinforcement is: " + str(parallel_limit) + " inches.")

    case "P":
        print("In progress, try again later.")
    case "HEX":
        print("In progress, try again later.")
    case "C":
        print("In progress, try again later.")
    case "PSV":
        print("In progress, try again later.")
    case default:
        print("You did not choose a correct option.")