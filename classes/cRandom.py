import random


class cWRandom(object):
    """Defines a Class for all the needed randomness"""

    def randomnessSeeder(self):
        print "Seeding..."
        print "done."
        # obj_list = []
        # for i in range(10):
        # # change the value every time, when there is a function added!
        #     i = cWRandom()
        #     obj_list.append(i)

        # for j in range(10): # add every funktion from below.
        #     obj_list[j].terrainSeed(random.randrange(1, 10000, 1), j)

        return

    def iAtomSeed(self):
        random.seed = self.randomnessSeeder()
        return

    def iBioCellSeed(self, iBCSeed):
        return

    def iTerrainSeed(self, iTSeed, count):
        print("terrainSeed " + str(count) + ": " +
              str(random.randrange(1, iTSeed, 1)))
        return

    def iWorldSeed(self, iWSeed):
        return
