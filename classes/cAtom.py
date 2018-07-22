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
        Protoncount and Neutroncount.Neutroncount atm not implementedself.
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

        return strAtomName
