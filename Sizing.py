import math
import decimal
import Classes


Exxon = Classes.PressureVessel()
P = input("Enter design pressure in psi: ")
R = input("Enter inside radius in inches: ")
S = input("Enter allowable material stress in psi: ")
E = input("Enter joint efficiency: ")
CA = input("Enter corrosion allowance: ")
shellMinThickness = Exxon.shellMinThickness(int(P), int(R), int(S), int(E), float(CA))
print("The Minimum Required Thickness for the Shell is: " + str(shellMinThickness) + " inches.")

