#Python module for all project classes

class PressureVessel:

    def __init__(self):
        pass

    plate_thickness = [.1875, .25, .3125, .375, .4375, .5, .5625, .625, .6875, .75, .8125, .875, 1, 
                           1.125, 1.25, 1.375, 1.5, 1.625, 1.75, 1.875, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 4, 5] 

    nozzle_size = {1: .5, 2: .625, 3: .625, 4: .75, 5: .75, 6: .875}

    #P: Design Pressure (psi)
    #R: Inside Radius (inches)
    #D: Inside Diameter (inches)
    #S: Material Stress (psi)
    #E: Joint Efficiency
    #CA: Corrosion Allowance (inches)
    #t: Minimum Required Thickness of Shell (inches)
    #tn: Nominal Thickness of Shell (inches)
    #Ps: Static Pressure Head (psi)
    #NS: Nozzle Size (inches)
    #tnoz: Nozzle Thickness (inches)

    #Calculate shell minimum thickness, MAWP and MAP
    def shell(self, P, R, S, E, CA):
        Ps = (((R * 2) + (CA * 2)) / 12) / 2.31
        t = (((P + Ps) * (R + CA)) / ((S * E) - (.6 * (P + Ps)))) + CA
        counter = 1
        for thickness in self.plate_thickness:
            if 0 < t <= .1875:
                tn = thickness
                print("Use .1875\" thick plate.")
                break
            if self.plate_thickness[counter - 1] <= t <= self.plate_thickness[counter]:
                tn = self.plate_thickness[counter]
                print("Use " + str(self.plate_thickness[counter]) + "\" thick plate.")
                break
            counter = counter + 1
        MAWP = ((S * E * (tn - CA)) / ((R + CA) + (.6 * (tn - CA)))) - Ps
        MAP = (S * E * tn) / (R + (.6 * tn))
        return round(t, 4), round(MAWP, 2), round(MAP, 2)

    def head(self, P, D, S, E, CA):
        Ps = ((D + (CA * 2)) / 12) / 2.31
        t = (((P + Ps) * (D + (2 * CA))) / ((2 * S * E) - (.2 * (P + Ps)))) + CA
        counter = 1
        for thickness in self.plate_thickness:
            if 0 < t <= .1875:
                tn = thickness
                print("Use .1875\" thick plate.")
                break
            if self.plate_thickness[counter - 1] <= t <= self.plate_thickness[counter]:
                tn = self.plate_thickness[counter]
                print("Use " + str(self.plate_thickness[counter]) + "\" thick plate after forming.")
                print("Use " + str(self.plate_thickness[counter + 1]) + "\" thick plate prior to forming.")
                break
            counter = counter + 1
        MAWP = ((2 * S * E * (tn - CA)) / ((D + (2 * CA)) + (.2 * (tn - CA)))) - Ps
        MAP = (2 * S * E * tn) / (D + (.2 * tn))
        return round(t, 4), round(MAWP, 2), round(MAP, 2)

    #Assume all openings are radial to avoid Nozzle Opening Chord Length and nozzles are CL150 and located in the shell
    def limit(self, P, R, S, E, CA, NS):
        Ps = (((R * 2) + (CA * 2)) / 12) / 2.31
        t = (((P + Ps) * (R + CA)) / ((S * E) - (.6 * (P + Ps)))) + CA
        counter = 1
        for thickness in self.plate_thickness:
            if 0 < t <= .1875:
                tn = thickness
                print("Use .1875\" thick plate.")
                break
            if self.plate_thickness[counter - 1] <= t <= self.plate_thickness[counter]:
                tn = self.plate_thickness[counter]
                print("Use " + str(self.plate_thickness[counter]) + "\" thick plate.")
                break
            counter = counter + 1
        tnoz = self.nozzle_size[NS]
        if NS > (NS / 2) + tnoz + tn:
            return NS
        else:
            return (NS / 2) + tnoz + tn