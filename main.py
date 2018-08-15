from classes.cAtom import cAtom
from classes.cRandom import cWRandom
from classes.cWorld import cWorld
# import cv2
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
        # k = cv2.waitKey(1) & 0xFF
        RandomNumber = obj_random.iAtomSeed()
        RandomNumber1 = obj_random.iAtomSeed()
        RandomNumber2 = obj_random.iAtomSeed()
        iElectron = RandomNumber
        iProton = RandomNumber1
        iNeutron = RandomNumber2
        strAtom = objAtom.strWhichAtomv2(iElectron, iProton, iNeutron)

        # if k == ord('p'):
        if strAtom != "NO_ATOM":

            print("Atom: "), strAtom, ("\r")

        # elif k == ord('q'):
        # break

    return


if __name__ == "__main__":
    main()
