import math
import decimal
import Classes

userInput = input("What equipment do you want to size?\n"
                  "Type \"PV\" for Pressure Vessel sizing\n"
                  "Type \"P\" for Pump sizing\n"
                  "Type \"HEX\" Heat Exchanger sizing\n"
                  "Type \"PSV\" for Pressure Safety Valve sizing\n")

if userInput == "PV":
    PressureVessel = Classes.PressureVessel()
    user_input_pv = input("What calculation do you want to run?\n"
                          "Type \"minthickIR\" for UG-27(c)(1) Minimum Required Thickness of Shell under Internal Pressure in terms of Inside Radius\n"
                          "Type \"minthickOR\" for Mandatory Appendix 1-1 Minimum Required Thickness of Shell under Internal Pressure in terms of Outside Radius\n")
    if user_input_pv == "minthickIR":
        P = input("Enter design pressure in psi: ")
        R = input("Enter inside radius in inches: ")
        S = input("Enter allowable material stress in psi: ")
        E = input("Enter joint efficiency: ")
        CA = input("Enter corrosion allowance: ")
        shellMinThickness = PressureVessel.shellMinThicknessIR(int(P), int(R), int(S), int(E), float(CA))
    elif user_input_pv == "minthickOR":
        P = input("Enter design pressure in psi: ")
        R = input("Enter outside radius in inches: ")
        S = input("Enter allowable material stress in psi: ")
        E = input("Enter joint efficiency: ")
        CA = input("Enter corrosion allowance: ")
        shellMinThickness = PressureVessel.shellMinThicknessOR(int(P), int(R), int(S), int(E), float(CA))
    print("The Minimum Required Thickness for the Shell is: " + str(shellMinThickness) + " inches.")

