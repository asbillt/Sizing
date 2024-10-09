#Python module for all project classes

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
            t = (P * R) / ((S * E) - (0.6 * P))
        else:
            t = ((P * (R + CA)) / ((S * E) - (0.6 * P))) + CA
        return round(t, 4)
