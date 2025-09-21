import json
import os
for file in os.listdir(r"C:\Users\USER\Desktop\NFT Final - Project\NFTS\Metadata"):
    with open(rf"C:\Users\USER\Desktop\NFT Final - Project\NFTS\Metadata\{file}" , 'r+') as f:
        data = json.load(f)
        data["collection"] = "Messiah-Antichrist"
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent = 4)
        f.truncate()