class Terrain():
    def __init__(self, color):
        self.terrainBlocks = {(0, 590):(600, 10)} # default base terrain
        self.color = color

    def getColor(self):
        return self.color

    def getBlocks(self):
        return self.terrainBlocks

    def getBlocksLocation(self):
        return list(self.terrainBlocks)
    
    def getSpecificBlockSize(self, x, y):
        if (x, y) in self.terrainBlocks:
            return self.terrainBlocks[(x, y)]
        else:
            return None

    def addBlock(self, x, y, w, h):
        self.terrainBlocks[(x, y)] = (w, h)

    # def isLegalX(self, object):
    #     oX, oY = object.getLocation()
    #     oW, oH = object.getSize()
    #     blocksLocations = self.getBlocksLocation()
    #     for loc in blocksLocations:
    #         tx, ty = loc
    #         tw, th = self.terrainBlocks[loc]
    #         # print(oX + oW > tx, oY + oH > ty, oX < tx + tw, oH < ty + th)
    #         if oX + oW > tx and oX < tx + tw:
    #             return False
    #     return True

    # def isLegalY(self, object):
    #     oX, oY = object.getLocation()
    #     oW, oH = object.getSize()
    #     blocksLocations = self.getBlocksLocation()
    #     for loc in blocksLocations:
    #         tx, ty = loc
    #         tw, th = self.terrainBlocks[loc]
    #         # print(oX + oW > tx, oY + oH > ty, oX < tx + tw, oH < ty + th)
    #         if oY + oH < ty and oH > ty + th:
    #             return False
    #     return True

    # if true, then colliding with no terrain, else, return the location of the 
    # terrain that collides with the object.
    def isLegalLocation(self, object): # inputs an object
        # if self.isLegalX(object) or self.isLegalY(object):
        #     return True
        # return False
        oX, oY = object.getLocation()
        oW, oH = object.getSize()
        blocksLocations = self.getBlocksLocation()
        for loc in blocksLocations:
            tx, ty = loc
            tw, th = self.terrainBlocks[loc]
            # print(oX + oW > tx, oY + oH > ty, oX < tx + tw, oH < ty + th)
            if oX + oW > tx and oY + oH < ty and \
                oX < tx + tw and oH > ty + th:
                return (tx, ty)
        return True

    def isLegalLocation2(self, oX, oY, oW, oH): # inputs location and size
        blocksLocations = self.getBlocksLocation()
        for loc in blocksLocations:
            tx, ty = loc
            tw, th = self.terrainBlocks[loc]
            # print(oX + oW > tx, oY + oH > ty, oX < tx + tw, oH < ty + th)
            if oX + oW > tx and oY + oH < ty and \
                oX < tx + tw and oH > ty + th:
                return (tx, ty)
        return True
    
    # def getFloor(self, object, HEIGHT): # app.height
    #     oX, oY = object.getLocation()
    #     oW, oH = object.getSize()
    #     miniDiff = None
    #     floor = HEIGHT
    #     blocksLocations = self.getBlocksLocation()
    #     for loc in blocksLocations:
    #         tx, ty = loc
    #         tw, th = self.terrainBlocks[loc]
    #         # print(ty >= oY + oH, oX + oW > tx, oX < tx + tw)
    #         if ty >= oY + oH and oX + oW > tx and oX < tx + tw:
    #             diff = ty - (oY + oH)
    #             if miniDiff == None or (diff < miniDiff):
    #                 miniDiff = diff
    #                 floor = ty
    #     return floor
    
    # def getRoof(self, object):
    #     oX, oY = object.getLocation()
    #     oW, oH = object.getSize()
    #     miniDiff = None
    #     roof = 0
    #     blocksLocations = self.getBlocksLocation()
    #     for loc in blocksLocations:
    #         tx, ty = loc
    #         tw, th = self.terrainBlocks[loc]
    #         print(ty + th <= oY, oX + oW > tx, oX < tx + tw)
    #         if ty + th <= oY and oX + oW > tx and oX < tx + tw:
    #             diff = oY - (ty + th)
    #             if miniDiff == None or (diff < miniDiff):
    #                 miniDiff = diff
    #                 roof = ty + th
    #     return roof

testTerrain = Terrain('grey')

# print(testTerrain.getTerrainBlocks())
# print(testTerrain.getTerrainBlocksLocation())

def roomGeneration():
    testTerrain.addBlock(0, 500, 100, 10)

def illegalAreas():
    pass