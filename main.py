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

    try:
        while 1:  # mainloop
            RandomNumber = obj_random.iAtomSeed()
            print RandomNumber
            iElectron = RandomNumber
            iProton = RandomNumber
            iNeutron = RandomNumber
            strAtom = objAtom.strWhichAtom(iElectron, iProton, iNeutron)

            if strAtom != "NO_ATOM":
                print "Atom: " + strAtom

    except KeyboardInterrupt:
        pass

    return


if __name__ == "__main__":
    main()
