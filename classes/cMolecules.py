from cAtom import cAtom

oAtom = cAtom()


class cMolecule(object):
    def mH2O(self, intH, intO, intH2O):
        if (intH == 2 and intO == 1):
            intH2O += 1
            return intH2O
        else:
            return intH2O

    def mH2(self, intH, intH2):
        if (intH == 2):
            intH2 += 1
            return intH2
        else:
            return intH2
