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
    #t: Minimum Required Thickness of Shell in Inches
    #tn: Nominal Thickness of Shell in Inches
    #Ps: Static Pressure Head in PSI

    #Calculate shell minimum thickness in terms of Inside Radius
    def shellMinThickIR(self, P, IR, S, E, CA = 0):
        if CA == 0:
            Ps = ((IR * 2) / 12) / 2.31
            t = ((P + Ps) * IR) / ((S * E) - (0.6 * (P + Ps)))
        else:
            Ps = (((IR * 2) + (CA * 2)) / 12) / 2.31
            t = (((P + Ps) * (IR + CA)) / ((S * E) - (0.6 * (P + Ps)))) + CA
        return round(t, 4)

    #Calculate shell minimum thickness in terms of Outside Radius
    def shellMinThickOR(self, P, OR, S, E, CA = 0):
        if CA == 0:
            #Ps = 
            t = (P * OR) / ((S * E) + (0.4 * P))
        else:
            #Ps = 
            t = ((P * OR) / ((S * E) + (0.4 * P))) + CA
        return round(t, 4)

    #Calculate MAWP in terms of Inside Radius
    def MAWP_IR(self, IR, S, E, tn, CA = 0):
        #Calculate Static Pressure Head assuming Specific Gravity = 1
        #Divide by 12 to convert inches to feet. Divide by 2.31 to convert from feet to psi.
        if CA == 0:
            Ps = ((IR * 2) / 12) / 2.31
            MAWP = ((S * E * tn) / (IR + (.6 * tn))) - Ps
        else:
            Ps = (((IR * 2) + (CA * 2)) / 12) / 2.31
            MAWP = ((S * E * (tn - CA)) / ((IR + CA) + (.6 * (tn - CA)))) - Ps
        return round(MAWP, 2)

    #Calculate MAWP in terms of Outside Radius
    def MAWP_OR(self, OR, S, E, tn, CA = 0):
        #Calculate Static Pressure Head assuming Specific Gravity = 1
        #Divide by 12 to convert inches to feet. Divide by 2.31 to convert from feet to psi.
        if CA == 0:
            Ps = (((OR * 2) - (tn * 2)) / 12) / 2.31
            MAWP = ((S * E * tn) / (OR - (.4 * tn))) - Ps
        else:
            Ps = (((OR * 2) - ((tn - CA) * 2)) / 12) / 2.31
            MAWP = ((S * E * (tn - CA)) / (OR - (.4 * (tn - CA)))) - Ps
        return round(MAWP, 2)


class Pump:
    
    def __init__(self):
        pass

class HeatExchanger:
    
    def __init__(self):
        pass

class PSV:
    
    def __init__(self):
        pass