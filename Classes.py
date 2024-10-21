#Python module for all project classes

class PressureVessel:

    def __init__(self):
        pass

    #P: Design Pressure
    #IR: Inside Radius in Inches
    #OR: Outside Radius in Inches
    #S: Material Stress
    #E: Joint Efficiency
    #CA: Corrosion Allowance
    #t: Minimum Required Thickness of Shell

    #Calculate shell minimum thickness in terms of Inside Radius
    def shellMinThicknessIR(self, P, IR, S, E, CA = 0):
        if CA == 0:
            t = (P * IR) / ((S * E) - (0.6 * P))
        else:
            t = ((P * (IR + CA)) / ((S * E) - (0.6 * P))) + CA
        return round(t, 4)

    #Calculate shell minimum thickness in terms of Outside Radius
    def shellMinThicknessOR(self, P, OR, S, E, CA = 0):
        if CA == 0:
            t = (P * OR) / ((S * E) + (0.4 * P))
        else:
            t = ((P * OR) / ((S * E) - (0.6 * P))) + CA
        return round(t, 4)


class Pump:
    
    def __init__(self):
        pass

class HeatExchanger:
    
    def __init__(self):
        pass

class PSV:
    
    def __init__(self):
        pass