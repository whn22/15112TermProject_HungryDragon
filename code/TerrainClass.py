class Terrain():
    def __init__(self, color):
        self.terrainBlocks = {(0, 590):(1000, 10)} # default base terrain
        self.color = color

    def addBlock(self, x, y, w, h):
        self.terrainBlocks[(x, y)] = (w, h)

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

    def isLegalLocation(self, object): # inputs an object
        oX, oY = object.getLocation()
        oW, oH = object.getSize()
        blocksLocations = self.getBlocksLocation()
        for loc in blocksLocations:
            tx, ty = loc
            tw, th = self.terrainBlocks[loc]
            if oX + oW > tx and oX < tx + tw and oY + oH > ty and oY < ty + th:
                return (tx, ty)
        return True

    def isLegalLocation2(self, oX, oY, oW, oH): # inputs location and size
        blocksLocations = self.getBlocksLocation()
        for loc in blocksLocations:
            tx, ty = loc
            tw, th = self.terrainBlocks[loc]
            if oX + oW > tx and oX < tx + tw and oY + oH > ty and oY < ty + th:
                return (tx, ty)
        return True

testTerrain = Terrain('grey')

# def roomGeneration():
#     testTerrain.addBlock(0, 500, 100, 10)

# def illegalAreas():
#     pass