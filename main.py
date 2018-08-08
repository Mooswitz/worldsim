# Copyright 2018 by Moritz Will
# Everyone is allowed to copy this code and to make his own changes.
# Nobody is allowed to share this work on other places. You are
# also not allowed to claim this work as your own, as long as you 
# use parts of my code.
# This counts for every file in this repository!

from classes.cRandom import cWRandom
from classes.cWorld import cWorld
"""This project is work-in-progess and will run
a very long time in development.
"""


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
