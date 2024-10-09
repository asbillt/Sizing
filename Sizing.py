import math
import decimal

class PressureVessel:

    def __init__(self):
        pass

    #P: Design Pressure
    #R: Inside Radius in Inches
    #S: Material Stress
    #E: Joint Efficiency
    #CA: Corrosion Allowance
    #t: Minimum Required Thickness of Shell
    def shellMinThickness(self, P, R, S, E, CA = 0):
        if CA == 0:
            t = (int(P) * int(R)) / ((int(S) * int(E)) - (0.6 * int(P)))
        else:
            t = ((int(P) * (int(R) + float(CA))) / ((int(S) * int(E)) - (0.6 * int(P)))) + float(CA)
        return round(t, 4)


Exxon = PressureVessel()
P = input("Enter design pressure in psi: ")
R = input("Enter inside radius in inches: ")
S = input("Enter allowable material stress in psi: ")
E = input("Enter joint efficiency: ")
CA = input("Enter corrosion allowance: ")
shellMinThickness = Exxon.shellMinThickness(P, R, S, E, CA)
print("The Minimum Required Thickness for the Shell is: " + str(shellMinThickness) + " inches.")

