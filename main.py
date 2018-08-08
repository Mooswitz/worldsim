# Copyright 2018 by Moritz Will
# Everyone is allowed to copy this code and to make his own changes.
# Nobody is allowed to share this work on other places. You are
# also not allowed to claim this work as your own, as long as you 
# use parts of my code.
# This counts for every file in this repository!

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
            RandomNumber1 = obj_random.iAtomSeed()
            RandomNumber2 = obj_random.iAtomSeed()
            iElectron = RandomNumber
            iProton = RandomNumber1
            iNeutron = RandomNumber2
            strAtom = objAtom.strWhichAtom(iElectron, iProton, iNeutron)

            if strAtom != "NO_ATOM":
                print("Atom: "), strAtom, ("\r\n")

    except KeyboardInterrupt:
        pass

    return


if __name__ == "__main__":
    main()
