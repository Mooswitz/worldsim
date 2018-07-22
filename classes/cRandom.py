import random


class cWRandom:
    def randomnessSeeder(self):
        # obj_list = []
        # for i in range(10):
        #     i = cWRandom()
        #     obj_list.append(i)

        # for j in range(10):
        #     obj_list[j].terrainSeed(random.randrange(1, 10000, 1), j)

        return

    def iAtomSeed(self):
        random.seed = self.randomnessSeeder()
        return

    def iBioCellSeed(self, iBCSeed):
        return

    def iTerrainSeed(self, iTSeed, count):
        print("terrainSeed "+str(count)+": " +
              str(random.randrange(1, iTSeed, 1)))
        return

    def iWorldSeed(self, iWSeed):
        return
