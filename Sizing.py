import Classes
from tkinter import *
from tkinter import ttk

#Create root window
root = Tk()
root.title("Sizing")
root.iconbitmap("logo.ico")
root.state("zoomed")

#Create notebook and frames
notebook = ttk.Notebook(root)
frame_PV = ttk.Frame(notebook)
frame_PSV = ttk.Frame(notebook)

#Place notebook and frame
notebook.add(frame_PV, text = "Pressure Vessel")
notebook.add(frame_PSV, text = "Pressure Safety Valve")
notebook.pack()

#Use a StringVar to store the selected Radio Button value
radius = StringVar(value = "Inside Radius")

#Create Pressure Vessel Tab Widgets
button_IR = ttk.Radiobutton(frame_PV, text = "Inside Radius", variable = radius, value = "UG-27(c)(1) Calculation")
button_MA = ttk.Radiobutton(frame_PV, text = "Outside Radius", variable = radius, value = "Mandatory Appendix 1 Calculation")

label_radius = ttk.Label(frame_PV, text = "test")
label_P = ttk.Label(frame_PV, text = "Design Pressure (psi)")
label_R = ttk.Label(frame_PV, text = "Radius (in)")
label_S = ttk.Label(frame_PV, text = "Allowable Stress (psi)")
label_E = ttk.Label(frame_PV, text = "Joint Efficiency")
label_CA = ttk.Label(frame_PV, text = "Corrosion Allowance (in)")

entry_P = ttk.Entry(frame_PV, width = 20)
entry_R = ttk.Entry(frame_PV, width = 20)
entry_S = ttk.Entry(frame_PV, width = 20)
entry_E = ttk.Entry(frame_PV, width = 20)
entry_CA = ttk.Entry(frame_PV, width = 20)

calculate = ttk.Button(frame_PV, text = "Calculate")

output = ttk.Label(frame_PV, text = "Output")
label_shell = ttk.Label(frame_PV, text = "Minimum Required Thickness (in):")
label_MAWP = ttk.Label(frame_PV, text = "MAWP (psi):")
label_MAP = ttk.Label(frame_PV, text = "MAP (psi):")
label_shell_output = ttk.Label(frame_PV, text = "min. output")
label_MAWP_output = ttk.Label(frame_PV, text = "MAWP")
label_MAP_output = ttk.Label(frame_PV, text = "MAP")

#Place Pressure Vessel Tab Widgets
button_IR.grid(row = 0, column = 0)
button_MA.grid(row = 0, column = 1)

label_radius.grid(row = 1, column = 0, columnspan = 2)
label_P.grid(row = 2, column = 0, stick = "w")
label_R.grid(row = 3, column = 0, stick = "w")
label_S.grid(row = 4, column = 0, stick = "w")
label_E.grid(row = 5, column = 0, stick = "w")
label_CA.grid(row = 6, column = 0, stick = "w")

entry_P.grid(row = 2, column = 1)
entry_R.grid(row = 3, column = 1)
entry_S.grid(row = 4, column = 1)
entry_E.grid(row = 5, column = 1)
entry_CA.grid(row = 6, column = 1)

calculate.grid(row = 7, column = 0, columnspan = 2)

output.grid(row = 8, column = 0, columnspan = 2)
label_shell.grid(row = 9, column = 0, stick = "w")
label_MAWP.grid(row = 10, column = 0, stick = "W")
label_MAP.grid(row = 11, column = 0, stick = "w")
label_shell_output.grid(row = 9, column = 1)
label_MAWP_output.grid(row = 10, column = 1)
label_MAP_output.grid(row = 11, column = 1)

#Run eventloop
root.mainloop()

'''
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
                print("The Parallel Limit of Reinforcement is: " + str(parallel_limit) + " inches.")'''