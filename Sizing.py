import math
import decimal
import Classes

#Take user input to determine which equipment will be sized
userInput = input("What equipment do you want to size?\n"
                  "Type \"PV\" for Pressure Vessel sizing\n"
                  "Type \"P\" for Pump sizing\n"
                  "Type \"HEX\" Heat Exchanger sizing\n"
                  "Type \"PSV\" for Pressure Safety Valve sizing\n")

if userInput == "PV":
    pressureVessel = Classes.PressureVessel()
    metalPlateThickness = [.1875, .25, .3125, .375, .4375, .5, .5625, .625, .6875, .75, .8125, .875, 1, 
                           1.125, 1.25, 1.375, 1.5, 1.625, 1.75, 1.875, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 4, 5]
    userInputPV = input("What calculation do you want to run?\n"
                          "Type \"minthickIR\" for UG-27(c)(1) Minimum Required Thickness of Shell under Internal Pressure in terms of Inside Radius\n"
                          "Type \"minthickOR\" for Mandatory Appendix 1-1 Minimum Required Thickness of Shell under Internal Pressure in terms of Outside Radius\n")
    if userInputPV == "minthickIR":
        P = input("Enter design pressure in psi: ")
        R = input("Enter inside radius in inches: ")
        S = input("Enter allowable material stress in psi: ")
        E = input("Enter joint efficiency: ")
        CA = input("Enter corrosion allowance: ")
        shellMinThickness = pressureVessel.shellMinThicknessIR(int(P), int(R), int(S), float(E), float(CA))
    elif userInputPV == "minthickOR":
        P = input("Enter design pressure in psi: ")
        R = input("Enter outside radius in inches: ")
        S = input("Enter allowable material stress in psi: ")
        E = input("Enter joint efficiency: ")
        CA = input("Enter corrosion allowance: ")
        shellMinThickness = pressureVessel.shellMinThicknessOR(int(P), int(R), int(S), float(E), float(CA))
    print("The Minimum Required Thickness for the Shell is: " + str(shellMinThickness) + " inches.")

    #Loop through metal plate gauges to determine choice from the shellMinThickness
    n = 1
    for thickness in metalPlateThickness:
        if shellMinThickness <= metalPlateThickness[0]:
            print("Use .1875\" thick plate")
            break;
        if shellMinThickness <= metalPlateThickness[n] and shellMinThickness > metalPlateThickness[n - 1]:
            print("Use " + str(metalPlateThickness[n]) + "\" thick plate")
            break;
        n += 1


