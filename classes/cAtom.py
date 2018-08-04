"""This is the Class, which defines an Atom"""


class cAtom(object):
    def iElectrons(self, iECount):
        if iECount <= 0:
            return 0
        else:
            return iECount

    def iProtons(self, iPCount):
        if iPCount <= 0:
            return 0
        else:
            return iPCount

    def iNeutrons(self, iNCount):
        if iNCount <= 0:
            return 0
        else:
            return iNCount

    def strWhichAtom(self, iECount, iPCount, iNCount):
        """Defines which Atom it can be, based on Electron count,
        Protoncount and Neutroncount. Neutroncount atm not implemented.
        """
        strAtomName = "NO_ATOM"

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
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 6:
            if iECount == 6:
                strAtomName = "Carbon"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 7:
            if iECount == 7:
                strAtomName = "Nitrogen"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 8:
            if iECount == 8:
                strAtomName = "Oxygen"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 9:
            if iECount == 9:
                strAtomName = "Fluorum"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 10:
            if iECount == 10:
                strAtomName = "Neon"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 11:
            if iECount == 11:
                strAtomName = "Natrium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 12:
            if iECount == 12:
                strAtomName = "Magnesium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 13:
            if iECount == 13:
                strAtomName = "Aluminium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 14:
            if iECount == 14:
                strAtomName = "Silicium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 15:
            if iECount == 15:
                strAtomName = "Phosphorus"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 16:
            if iECount == 16:
                strAtomName = "Sulphur"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 17:
            if iECount == 17:
                strAtomName = "Chlorum"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 18:
            if iECount == 18:
                strAtomName = "Argon"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 19:
            if iECount == 19:
                strAtomName = "Kalium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 20:
            if iECount == 20:
                strAtomName = "Calcium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 21:
            if iECount == 21:
                strAtomName = "Scandium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 22:
            if iECount == 22:
                strAtomName = "Titanium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 23:
            if iECount == 23:
                strAtomName = "Vanadium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 24:
            if iECount == 24:
                strAtomName = "Chromium"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 25:
            if iECount == 25:
                strAtomName = "Manganum"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 26:
            if iECount == 26:
                strAtomName = "Ferrum"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 27:
            if iECount == 27:
                strAtomName = "Cobaltum"
            else:
                strAtomName = "NO_ATOM"
        if iPCount == 28:
            if iECount == 28:
                strAtomName = "Niccolum"
            else:
                strAtomName = "NO_ATOM"

        else:
            strAtomName = "NO_ATOM"

        return strAtomName

    def getAtom(self):

        Atom = {}
        return Atom[1]
