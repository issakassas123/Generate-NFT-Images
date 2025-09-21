from os import listdir, rename, remove, rmdir
from random import choice, randint
from shutil import copy
from os.path import exists 
from json import load, dump
from GetLayerDataList import getData

ImagesFolder = r"C:\Users\USER\Desktop\Images"
MetadataFolder = r"C:\Users\USER\Desktop\Metadata"
destination_images = r"C:\Users\USER\Desktop\NFT Final - Project\NFTS\Images"
destination_json = r"C:\Users\USER\Desktop\NFT Final - Project\NFTS\Metadata"

def copyNFT(token = 1):
    if len(characters) == 0:
        return

    if token % 3 == 0:
        characterChoosen = characters[0]
        
    else:
        characterChoosen = choice(characters)

    if not exists(f"{ImagesFolder}\{characterChoosen}"):
        copyNFT(token)
    
    backgrounds = listdir(f"{ImagesFolder}\{characterChoosen}")
    if len(backgrounds) == 0:
        rmdir(f"{ImagesFolder}\{characterChoosen}")
        rmdir(f"{MetadataFolder}\{characterChoosen}")
        characters.remove(characterChoosen)
        copyNFT(token)
        
    else:
        backgroundChoosen = choice(backgrounds)
        imgsChoosenList = listdir(f"{ImagesFolder}\{characterChoosen}\{backgroundChoosen}")
        if len(imgsChoosenList) == 0:
            rmdir(f"{ImagesFolder}\{characterChoosen}\{backgroundChoosen}")
            rmdir(f"{MetadataFolder}\{characterChoosen}\{backgroundChoosen}")
            copyNFT(token)
                
        else:
            imgChoosen = choice(imgsChoosenList)
            jsonChoosen = imgChoosen.replace('png' , 'json')

            remove(f"{destination_images}\AntiChrist #{token}.png")
            remove(f"{destination_json}\AntiChrist #{token}.json")
            
            copy(f"{ImagesFolder}\{characterChoosen}\{backgroundChoosen}\{imgChoosen}",
                 f"{destination_images}\{imgChoosen}")
            copy(f"{MetadataFolder}\{characterChoosen}\{backgroundChoosen}\{jsonChoosen}",
                f"{destination_json}\{jsonChoosen}")
            
            rename(f"{destination_images}\{imgChoosen}", f"{destination_images}\AntiChrist #{token}.png")
            rename(f"{destination_json}\{jsonChoosen}", f"{destination_json}\AntiChrist #{token}.json")
            
            with open(f"{destination_json}\AntiChrist #{token}.json", "r+") as file:
                data = load(file)
                data["file_path"] = f"{destination_images}\AntiChrist #{token}.png"
                data["nft_name"] = f"AntiChrist #{token}"
                data["description"] = f"The Legend AntiChrist {characterChoosen} #{token}"
                file.seek(0)
                dump(data, file, indent = 4)
                        
            remove(f"{ImagesFolder}\{characterChoosen}\{backgroundChoosen}\{imgChoosen}")
            remove(f"{MetadataFolder}\{characterChoosen}\{backgroundChoosen}\{jsonChoosen}")
            print(f"Image Copied {characterChoosen} #{token}")

if __name__ == "__main__":
    characters = [getData()[1][4], getData()[1][5]]
    for i in range(0, 144):
        token = randint(200, 14000)
        copyNFT(token)
