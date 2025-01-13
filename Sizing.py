import Classes
from tkinter import *
from tkinter import ttk

#Create root window
root = Tk()
root.title("Sizing")
root.iconbitmap("logo.ico")
root.state("zoomed")

#Create notebook and parent frame (frame_PV) with child frames (frame_Shell and frame_Head)
notebook = ttk.Notebook(root)
frame_PV = ttk.Frame(notebook)
frame_PSV = ttk.Frame(notebook)
frame_Shell = ttk.Frame(frame_PV)
frame_Head = ttk.Frame(frame_PV)

#Configure frames
frame_PV.config(padding = 1)
frame_PSV.config(padding = 1)
frame_Head.config(padding = 15, relief = "solid")
frame_Shell.config(padding = 15, relief = "solid")

#Place notebook and parent frame
notebook.add(frame_PV, text = "Pressure Vessel")
notebook.add(frame_PSV, text = "Pressure Safety Valve")
notebook.pack()
frame_Shell.grid(row = 1, column = 0, padx = 10, pady = 10)
frame_Head.grid(row = 1, column = 1, padx = 10, pady = 10)

#Use a StringVar to store the selected Radio Button value
radius = StringVar(value = "UG-27(c)(1) Calculation")
head_type = StringVar(value = "ellipsoidal")

#Create Pressure Vessel Tab Widgets
label_title = ttk.Label(frame_PV, text = "Pressure Vessel Calculations")

button_IR = ttk.Radiobutton(frame_Shell, text = "Inside Radius", variable = radius, value = "UG-27(c)(1) Calculation")
button_MA = ttk.Radiobutton(frame_Shell, text = "Outside Radius", variable = radius, value = "Mandatory Appendix 1 Calculation")

button_ellip = ttk.Radiobutton(frame_Head, text = "2:1 Ellipsoidal", variable = head_type, value = "ellipsoidal")
button_hemi = ttk.Radiobutton(frame_Head, text = "Hemispherical", variable = head_type, value = "hemispherical")

label_radius = ttk.Label(frame_Shell, textvariable = radius)
label_Shell_P = ttk.Label(frame_Shell, text = "Design Pressure (psi)")
label_Shell_R = ttk.Label(frame_Shell, text = "Radius (in)")
label_Shell_S = ttk.Label(frame_Shell, text = "Allowable Stress (psi)")
label_Shell_E = ttk.Label(frame_Shell, text = "Joint Efficiency")
label_Shell_CA = ttk.Label(frame_Shell, text = "Corrosion Allowance (in)")

label_Head_P = ttk.Label(frame_Head, text = "Design Pressure (psi)")
label_Head_S = ttk.Label(frame_Head, text = "Allowable Stress (psi)")
label_Head_D = ttk.Label(frame_Head, text = "Diameter (in)")
label_Head_E = ttk.Label(frame_Head, text = "Joint Efficiency")
label_Head_CA = ttk.Label(frame_Head, text = "Corrosion Allowance (in)")

entry_Shell_P = ttk.Entry(frame_Shell, width = 20)
entry_Shell_R = ttk.Entry(frame_Shell, width = 20)
entry_Shell_S = ttk.Entry(frame_Shell, width = 20)
entry_Shell_E = ttk.Entry(frame_Shell, width = 20)
entry_Shell_CA = ttk.Entry(frame_Shell, width = 20)

entry_Head_P = ttk.Entry(frame_Head, width = 20)
entry_Head_S = ttk.Entry(frame_Head, width = 20)
entry_Head_D = ttk.Entry(frame_Head, width = 20)
entry_Head_E = ttk.Entry(frame_Head, width = 20)
entry_Head_CA = ttk.Entry(frame_Head, width = 20)

calculate_Shell = ttk.Button(frame_Shell, text = "Calculate")
calculate_Head = ttk.Button(frame_Head, text = "Calculate")

output_Shell = ttk.Label(frame_Shell, text = "Output")
label_Shell = ttk.Label(frame_Shell, text = "Minimum Required Thickness (in):")
label_Shell_MAWP = ttk.Label(frame_Shell, text = "MAWP (psi):")
label_Shell_MAP = ttk.Label(frame_Shell, text = "MAP (psi):")
label_Shell_output = ttk.Label(frame_Shell, text = "TBD")
label_Shell_MAWP_output = ttk.Label(frame_Shell, text = "TBD")
label_Shell_MAP_output = ttk.Label(frame_Shell, text = "TBD")

output_Head = ttk.Label(frame_Head, text = "Output")

#Place Pressure Vessel Tab Widgets
label_title.grid(row = 0, column = 0, columnspan = 2)

button_IR.grid(row = 0, column = 0)
button_MA.grid(row = 0, column = 1)

button_ellip.grid(row = 0, column = 0)
button_hemi.grid(row = 0, column = 1)

label_radius.grid(row = 1, column = 0, columnspan = 2)
label_Shell_P.grid(row = 2, column = 0, stick = "w")
label_Shell_R.grid(row = 3, column = 0, stick = "w")
label_Shell_S.grid(row = 4, column = 0, stick = "w")
label_Shell_E.grid(row = 5, column = 0, stick = "w")
label_Shell_CA.grid(row = 6, column = 0, stick = "w")

label_Head_P.grid(row = 1, column = 0, stick = "w")
label_Head_S.grid(row = 2, column = 0, stick = "w")
label_Head_D.grid(row = 3, column = 0, stick = "w")
label_Head_E.grid(row = 4, column = 0, stick = "w")
label_Head_CA.grid(row = 5, column = 0, stick = "w")

entry_Shell_P.grid(row = 2, column = 1)
entry_Shell_R.grid(row = 3, column = 1)
entry_Shell_S.grid(row = 4, column = 1)
entry_Shell_E.grid(row = 5, column = 1)
entry_Shell_CA.grid(row = 6, column = 1)

entry_Head_P.grid(row = 1, column = 1)
entry_Head_S.grid(row = 2, column = 1)
entry_Head_D.grid(row = 3, column = 1)
entry_Head_E.grid(row = 4, column = 1)
entry_Head_CA.grid(row = 5, column = 1)

calculate_Shell.grid(row = 7, column = 0, columnspan = 2)
calculate_Head.grid(row = 6, column = 0, columnspan = 2)

output_Shell.grid(row = 8, column = 0, columnspan = 2)
label_Shell.grid(row = 9, column = 0, stick = "w")
label_Shell_MAWP.grid(row = 10, column = 0, stick = "W")
label_Shell_MAP.grid(row = 11, column = 0, stick = "w")
label_Shell_output.grid(row = 9, column = 1)
label_Shell_MAWP_output.grid(row = 10, column = 1)
label_Shell_MAP_output.grid(row = 11, column = 1)

output_Head.grid(row = 7, column = 0, columnspan = 2)

#Create Pressure Safety Valve Tab Widgets
label_title = ttk.Label(frame_PSV, text = "Pressure Safety Valve Calculations")

#Place Pressure Safety Valve Tab Widgets
label_title.grid(row = 0, column = 0)

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