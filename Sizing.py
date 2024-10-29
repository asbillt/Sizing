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
        metalPlateThickness = [.1875, .25, .3125, .375, .4375, .5, .5625, .625, .6875, .75, .8125, .875, 1, 
                               1.125, 1.25, 1.375, 1.5, 1.625, 1.75, 1.875, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 4, 5]
        userInputPV = input("What calculation do you want to run?\n"
                            "Type \"minthickIR\" for UG-27(c)(1) Minimum Required Thickness of Shell under Internal Pressure in terms of Inside Radius\n"
                            "Type \"minthickOR\" for Mandatory Appendix 1-1 Minimum Required Thickness of Shell under Internal Pressure in terms of Outside Radius\n")
        #Calculate min. required thickness for inside radius or outside radius
        if userInputPV == "minthickIR":
            P = input("Enter design pressure in psi: ")
            R = input("Enter inside radius in inches: ")
            S = input("Enter allowable material stress in psi: ")
            E = input("Enter joint efficiency: ")
            CA = input("Enter corrosion allowance in inches: ")
            shellMinThick = pressureVessel.shellMinThickIR(int(P), int(R), int(S), float(E), float(CA))
        elif userInputPV == "minthickOR":
            P = input("Enter design pressure in psi: ")
            R = input("Enter outside radius in inches: ")
            S = input("Enter allowable material stress in psi: ")
            E = input("Enter joint efficiency: ")
            CA = input("Enter corrosion allowance in inches: ")
            shellMinThick = pressureVessel.shellMinThickOR(int(P), int(R), int(S), float(E), float(CA))
        print("The Minimum Required Thickness for the Shell is: " + str(shellMinThick) + " inches.")

        #Loop through metal plate gauges to determine choice from the shellMinThick
        n = 1
        for thickness in metalPlateThickness:
            if shellMinThick <= metalPlateThickness[0]:
                tn = .1875
                print("Use .1875\" thick plate")
                break;
            if shellMinThick <= metalPlateThickness[n] and shellMinThick > metalPlateThickness[n - 1]:
                tn = metalPlateThickness[n]
                print("Use " + str(metalPlateThickness[n]) + "\" thick plate")
                break;
            n += 1

        #Calculate Maximum Allowable Working Pressure and Maximum Allowable Pressure
        if userInputPV == "minthickIR":
            MAWP_IR = pressureVessel.MAWP_IR(int(R), int(S), float(E), float(tn), float(CA))
            MAP_IR = pressureVessel.MAP_IR(int(R), int(S), float(E), float(tn))
            print("MAWP is: " + str(MAWP_IR) + " psi")
            print("MAP is: " + str(MAP_IR) + " psi")
        else:
            MAWP_OR = pressureVessel.MAWP_OR(int(R), int(S), float(E), float(tn), float(CA))
            MAP_OR = pressureVessel.MAP_OR(int(R), int(S), float(E), float(tn))
            print("MAWP is: " + str(MAWP_OR) + " psi")
            print("MAP is: " + str(MAP_OR) + " psi")

    case "P":
        print("In progress")
    case "HEX":
        print("In progress")
    case "C":
        print("In progress")
    case "PSV":
        print("In progress")
    case default:
        print("You did not choose a correct option.")


