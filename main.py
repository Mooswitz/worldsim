from classes.cRandom import cWRandom
from classes.cWorld import cWorld
"""THis now gets into git"""


def main():
    """test"""
    obj_earth = cWorld()
    obj_earth.fContinents(7)

    obj_random = cWRandom()
    obj_random.randomnessSeeder()

    while 1:  # mainloop
        break

    return


if __name__ == "__main__":
    main()
