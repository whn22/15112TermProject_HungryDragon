class Terrain():
    def __init__(self):
        self.terrainBlocks = {}
    
    def getTerrainBlocks(self):
        return self.terrainBlocks

    def addBlock(self, x, y, w, h):
        self.terrainBlocks[(x, y)] = (w, h)
    
testTerrain = Terrain()
testTerrain.addBlock(0, 100, 10, 10)

print(testTerrain.getTerrainBlocks())