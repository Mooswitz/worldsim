"""This is the Class, which defines an Atom"""


class cAtom(object):
    def iElectrons(self, iECount):
        if iECount <= 0:
            return
        else:
            return iECount

    def iProtons(self, iPCount):
        if iPCount <= 0:
            return
        else:
            return iPCount

    def iNeutrons(self, iNCount):
        if iNCount <= 0:
            return
        else:
            return iNCount

    def strWhichAtom(self, iECount, iPCount, iNCount):
        """Defines which Atom it can be, based on Electron count,
        Protoncount and Neutroncount. Neutroncount atm not implemented.
        """

        if iPCount == 1:
            if iECount == 0:
                strAtomName = "Proton"
            elif iECount == 1:
                strAtomName = "Hydrogen"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 2:
            if iECount == 2:
                strAtomName = "Helium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 3:
            if iECount == 3:
                strAtomName = "Lithium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 4:
            if iECount == 4:
                strAtomName = "Beryllium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 5:
            if iECount == 5:
                strAtomName = "Borum"
        if iPCount == 6:
            if iECount == 6:
                strAtomName = "Carbon"
        if iPCount == 7:
            if iECount == 7:
                strAtomName = "Nitrogen"
        if iPCount == 8:
            if iECount == 8:
                strAtomName = "Oxygen"
        if iPCount == 9:
            if iECount == 9:
                strAtomName = "Fluorum"
        if iPCount == 10:
            if iECount == 10:
                strAtomName = "Neon"
        if iPCount == 11:
            if iECount == 11:
                strAtomName = "Natrium"
        if iPCount == 12:
            if iECount == 12:
                strAtomName = "Magnesium"
        if iPCount == 13:
            if iECount == 13:
                strAtomName = "Aluminium"
        if iPCount == 14:
            if iECount == 14:
                strAtomName = "Silicium"
        if iPCount == 15:
            if iECount == 15:
                strAtomName = "Phosphorus"
        if iPCount == 16:
            if iECount == 16:
                strAtomName = "Sulphur"
        if iPCount == 17:
            if iECount == 17:
                strAtomName = "Chlorum"
        if iPCount == 18:
            if iECount == 18:
                strAtomName = "Argon"
        if iPCount == 19:
            if iECount == 19:
                strAtomName = "Kalium"
        if iPCount == 20:
            if iECount == 20:
                strAtomName = "Calcium"
        if iPCount == 21:
            if iECount == 21:
                strAtomName = "Scandium"
        if iPCount == 22:
            if iECount == 22:
                strAtomName = "Titanium"
        if iPCount == 23:
            if iECount == 23:
                strAtomName = "Vanadium"
        if iPCount == 24:
            if iECount == 24:
                strAtomName = "Chromium"

        return strAtomName
