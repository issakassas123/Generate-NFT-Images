from json import dump
from PIL import Image
import colorama
from colorama import Fore
from Conditions import backgroundsConditions, charactersConditions, crownsConditions, \
helmetsConditions, hornsConditions, logosConditions, suitsConditions, weaponsConditions, wingsConditions
from Constant import ASSETS_FOLDERS, LAYERS_FOLDERS, \
LAYERS_INDEX_IMAGES, METADATA_FOLDERS, OUTPUT_FOLDERS
from Metadata import template
from os import mkdir

def Create_save_img(ImageFileName , tokenid , backgroundFolder):
    img = Image.open(rf"{ASSETS_FOLDERS}\None.png").convert('RGBA')
    
    for folder, layer in zip(LAYERS_FOLDERS, LAYERS_INDEX_IMAGES):
        imgLayer = Image.open(f"{ASSETS_FOLDERS}\{folder}\{nft[layer]}.png").convert('RGBA')
        # Paste/Merge Required PNGs, as layers on base. Paste in order of how you want the layers.
        # Last paste will be top layer.
        img = Image.alpha_composite(img , imgLayer)
    
    img.save(f"{OUTPUT_FOLDERS}\{ImageFileName}\{backgroundFolder}\{ImageFileName} #{tokenid}.png", 'png', quality = 100)
    
def Generate_Metadata(ImageFileName , tokenid , backgroundFolder):
    metadata = template
    metadata_file_name = f"{METADATA_FOLDERS}\{ImageFileName}\{backgroundFolder}\{ImageFileName} #{tokenid + 1}.json"
    metadata["nft_name"] = f"AntiChrist {ImageFileName} #{tokenid + 1}"
    metadata["description"] = f"The Legend AntiChrist {ImageFileName} #{tokenid + 1}"
    metadata["file_path"] = f"{OUTPUT_FOLDERS}\\{ImageFileName}\\{backgroundFolder}\\{ImageFileName} #{tokenid + 1}.png"
    metadata['collection'] = 'Anti-Christ-Dajjal'
    metadata["duration"] = "6 months"
    metadata["properties"] = list()
    metadata["properties"].extend(
       [{
            'type' : 'BACKGROUND',
            'name': nft[0]
        },
        {
            'type': 'WING',
            'name': nft[1] 
        },
        { 
            'type' : 'CREATURE',
            'name': nft[2]
        },
        { 
            'type' : 'SUIT',
            'name': nft[3]
        },
        { 
            'type' : 'HELMET',
            'name': nft[4]
        },
        { 
            'type' : 'HORN',
            'name': nft[5]
        },
        {
            'type': 'CROWN',
            'name': nft[6]
        },
        { 
            'type' : 'LOGO',
            'name': nft[7]
        },
        {
            'type': 'WEAPON',
            'name': nft[8]
        }]
    )
    
    price = 0

    if metadata["properties"][2]["name"] == "Gold":
        price = 0.1
    
    if metadata["properties"][2]["name"] == "Angel":
        price = 0.09

    if metadata["properties"][2]["name"] == "Human":
        price = 0.08
        
    if metadata["properties"][2]["name"] == "Devil":
        price = 0.07
    
    if metadata["properties"][2]["name"] == "Jinn":
        price = 0.065
        
    if metadata["properties"][2]["name"] == "Fusion":
        price = 0.06
    
    if metadata["properties"][1]["name"] != "None":
        price += 0.014
        
    if metadata["properties"][3]["name"] != "None":
        price += 0.011
    
    if metadata["properties"][4]["name"] != "None":
        price += 0.012
        
    if metadata["properties"][5]["name"] != "None":
        price += 0.013
        
    if metadata["properties"][6]["name"] != "None":
        price += 0.013
    
    if metadata["properties"][7]["name"] != "None":
        price += 0.01
    
    if metadata["properties"][8]["name"] != "None":
        price += 0.015
    
    metadata["price"] = round(price, 3)
    
    keys = list(metadata.keys())
    for key in keys:
        new_key = key.replace(str(tokenid), str(tokenid + 1))
        if new_key != key:
            metadata[new_key] = metadata[key]
            del metadata[key]
            
    with open(metadata_file_name , "w") as file:
        dump(metadata , file)

def CombineNFT():
    global nft
    nft = []
    for character in charactersConditions():
        mkdir(f'{OUTPUT_FOLDERS}\{character}')
        mkdir(f'{METADATA_FOLDERS}\{character}')
        count, tokenid = 0, 0
        for background in backgroundsConditions(character):
            mkdir(f'{OUTPUT_FOLDERS}\{character}\{background}')
            mkdir(f'{METADATA_FOLDERS}\{character}\{background}')
            for suit in suitsConditions(character):
                for helmet in helmetsConditions(character, suit):
                    for horn in hornsConditions(character, suit, helmet):
                        for crown in crownsConditions(character, suit, helmet, horn):
                            for weapon in weaponsConditions(character, suit):
                                for wing in wingsConditions(character, suit):
                                    for logo in logosConditions(character, suit):
                                        nft = [background, wing, character, suit, 
                                                helmet, horn, crown, logo, weapon]
                                    
                                        string = ' '.join(str(e) for e in nft)
                                        tokenid += 1
                                        count += 1
                                        print(Fore.RED + f"Creating NFT #{count} ...")
                                        print(f"Combination {character} {tokenid}: {string}\n")
                                        Create_save_img(character , tokenid, background)
                                        print(Fore.BLUE + f"{character} #{tokenid} has been created", end = ", ")
                                        Generate_Metadata(character , tokenid - 1, background)
                                        print(Fore.GREEN + f"json #{tokenid} has been created")
                                        print('-' * 60 + '\n')

if __name__ == '__main__':
    colorama.init(autoreset = True)
    print("")
    CombineNFT()
