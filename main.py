from includes.nft_creator import NftCreator
from includes.utils import Args
from includes.rarity_calculator import RarityCalculator

#Folders names that will store ur uniques nfts, u can add more!
folderPaths = ['public_mint_assets','whitelist_mint_assets','giveaway_assets']
numberNFTs, testRarities, randomizedOutput = Args([0 for i in folderPaths], False, False)

#Rarities categories and color associated (can be modified adding/deleting) DONT USE (#000000)
colors = {
    'Legendary':'#ff8000',
    'Epic':'#a335ee',
    'Rare': '#0070dd',
    'Uncommon': '#6bca06',
    'Common': '#a0a0a0'
}

#Rarities that will be stored on ur json rarity displayer, this will have the same lenght as len(colors)
rarities = list(colors.keys())

#Percentage cut value to an item be considered with an rarity
#(legendary_percentage, epic_percentage,...,uncommon_percentage). Has to be the len(rarities)-1
percentages = [3.0, 6.5, 10.0, 17.0] 
#Any item with less than 3% will be considered as LEGENDARY, any item with less than 17.0 will be considered as UNCOMMON 
#and any item with greater-equal than 17 will be considered as COMMON


nfts = NftCreator(numberNFTs, folderPaths, testRarities, randomizedOutput)

print()
print('-------------------------------------------------------------------------')
print()

rarities = RarityCalculator(nfts, colors, rarities, percentages)
