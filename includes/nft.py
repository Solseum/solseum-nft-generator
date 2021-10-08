from PIL import Image
import os
import json
class Nft:
    metadata = ''
    number = 0
    layers = ''
    dnaPaths = ''
    folder_path = ''
    def __init__(self, number, name, attributes, jsonTemplate, dnaPath, layers, folder_path):
        self.metadata = jsonTemplate
        self.dnaPaths = dnaPath
        self.layers = layers
        self.name = name
        self.attributes = attributes
        self.number = number
        self.folder_path = folder_path
    
    def CreateImage(self):
        baseLayer = Image.open(os.path.dirname(__file__) + '/../input/assets/' + self.layers[0] + '/' + self.dnaPaths[0])
        for i in range(1, len(self.layers)):
            frontLayer = Image.open(os.path.dirname(__file__) + '/../input/assets/' + self.layers[i] + '/' + self.dnaPaths[i])
            baseLayer = Image.alpha_composite(baseLayer, frontLayer)
        baseLayer.save(os.path.dirname(__file__) + '/../output/nfts/' + self.folder_path + '/' + str(self.number) + '.png')

    def CreateMetadata(self):
        with open(os.path.dirname(__file__) + '/../output/nfts/' + self.folder_path + '/' + str(self.number) + '.json', 'w') as jsonFile:
            json.dump(self.metadata, jsonFile, indent = 4)




