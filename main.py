from classes.cRandom import cWRandom
from classes.cWorld import cWorld
"""This project is work-in-progess and will run
a very long time in development.
"""


def main():
    """This is the main-function for the simulation"""
    obj_earth = cWorld()
    obj_earth.fContinents(7)

    obj_random = cWRandom()
    obj_random.randomnessSeeder()

    while 1:  # mainloop
        break

    return


if __name__ == "__main__":
    main()
