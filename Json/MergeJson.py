from json import load , dump
from os import listdir
from os.path import isfile, join, abspath
from re import split

def digit(text: str):
    return int(text) if text.isdigit() else text
    
def keys(text: str):
    return [digit(i) for i in split(r"(\d+)" , text)]

def merge_json_files(filename : list):
    for i in range(0, 25):
        result = {
            'nft':[]
        }
        
        for j in range(i * 400 , (i + 1) * 400):
            with open(f'{metadata_path}/{filename[j]}', 'r+', encoding='utf-8') as infile:
                data = load(infile)
                result['nft'].append(data)

        with open(f'{metadata_output_path}/merge{i + 1}.json', 'w+') as output_file:
            dump(result, output_file, indent = 4)
            print(f"the merge{i + 1} file has been created!!!")

if __name__ == '__main__':
    metadata_path = "C:/Users/USER/Desktop/NFT Final - Project/NFTS/Metadata"
    metadata_output_path = "C:/Users/USER/Desktop/NFT Final - Project/NFTS/Mergedata"
    jsonFiles = listdir(metadata_path)
    jsonFiles.sort(key = keys)
    merge_json_files(jsonFiles)
