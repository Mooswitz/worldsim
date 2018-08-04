from classes.cAtom import cAtom
from classes.cRandom import cWRandom
from classes.cWorld import cWorld
"""This project is work-in-progess and will run
a very long time in development.
"""


def main():
    """This is the main-function for the simulation"""
    obj_earth = cWorld()
    obj_earth.fContinents(7)
    objAtom = cAtom()

    obj_random = cWRandom()

    while 1:  # mainloop
        iElectron = objAtom.iElectrons(obj_random.iAtomSeed())
        iProton = objAtom.iProtons(obj_random.iAtomSeed())
        iNeutron = objAtom.iNeutrons(obj_random.iAtomSeed())
        strAtom = objAtom.strWhichAtom(iElectron, iProton, iNeutron)

        if strAtom != "NO_ATOM":
            print "Atom: " + strAtom

    return


if __name__ == "__main__":
    main()
