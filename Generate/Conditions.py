from GetLayerDataList import getData

def charactersConditions():
    return getData()[1]

def backgroundsConditions(character):
    backgrounds = []
    if character == charactersConditions()[0]:
        backgrounds = [
            getData()[0][0],
            getData()[0][1],
            getData()[0][4],
            getData()[0][6],
            getData()[0][7],
            getData()[0][10],
            getData()[0][11]
        ]
        
    elif character == charactersConditions()[1]:
        backgrounds = [
            getData()[0][1],
            getData()[0][2],
            getData()[0][5],
            getData()[0][9],
            getData()[0][10]
        ]
    
    elif character == charactersConditions()[2]:
        backgrounds = [
            getData()[0][2],
            getData()[0][3],
            getData()[0][4],
            getData()[0][8],
            getData()[0][9],
            getData()[0][10]
        ]
    
    elif character == charactersConditions()[3]:
        backgrounds = [
            getData()[0][0],
            getData()[0][6],
            getData()[0][7],
            getData()[0][8],
            getData()[0][10],
            getData()[0][11]
        ]

    elif character == charactersConditions()[4]:
        backgrounds = [
            getData()[0][3],
            getData()[0][6],
            getData()[0][7],
            getData()[0][8],
            getData()[0][9],
            getData()[0][10],
            getData()[0][12]
        ]

    else:
        backgrounds = [
            getData()[0][0],
            getData()[0][1],
            getData()[0][3],
            getData()[0][5],
            getData()[0][9],
            getData()[0][11],
            getData()[0][12]
        ]
        
    return backgrounds

def suitsConditions(character):
    suits = []
    if character == charactersConditions()[0]:
        suits = [
            getData()[5][0],
            getData()[5][1],
            getData()[5][2],
            getData()[5][3],
            getData()[5][5],
            getData()[5][6]
        ]
    
    elif character == charactersConditions()[1]:
        suits = [
            getData()[5][0],
            getData()[5][3],
            getData()[5][4],
            getData()[5][5]
        ]
    
    elif character == charactersConditions()[2]:
        suits = [
            getData()[5][0],
            getData()[5][3],
            getData()[5][4],
        ]
        
    elif character == charactersConditions()[3]:
        suits = [
            getData()[5][0],
            getData()[5][1],
            getData()[5][5]
        ]
    
    elif character == charactersConditions()[4]:
        suits = [
            getData()[5][0],
            getData()[5][2]
        ]

    else:
        suits = [
            getData()[5][0],
            getData()[5][5]
        ]

    return suits

def helmetsConditions(character, suit):
    helmets = []
    if character == charactersConditions()[0]:
        if suit != getData()[5][0]:
            if suit != getData()[5][3]:
                helmets = [
                    getData()[2][0],
                    getData()[2][2]
                ]
            
            else:
                helmets =  [
                    getData()[2][1]
                ]
        
        else:
            helmets = [
                getData()[2][0]
            ]
    
    elif character == charactersConditions()[1]:
        if suit != getData()[5][0]:
            helmets = [
                getData()[2][0],
                getData()[2][2]
            ]
        
        else:
            helmets = [
                getData()[2][0]
            ]

    elif character == charactersConditions()[2]:
        if suit != getData()[5][0]:
            if suit == getData()[5][4]:
                helmets = [
                    getData()[2][0]
                ]
            
            else:
                helmets = [
                    getData()[2][1]
                ]
        
        else:
            helmets = [
                getData()[2][0]
            ]
    
    elif character == charactersConditions()[3]:
        helmets = [
            getData()[2][0]
        ]

    elif character == charactersConditions()[4]:
        helmets = [
            getData()[2][0]
        ]

    else:
        helmets = [
            getData()[2][0]
        ]
            
    return helmets

def hornsConditions(character, suit, helmet):
    horns = []
    if character == charactersConditions()[0]:
        if suit != getData()[5][0]:
            if helmet == getData()[2][0]:
                if suit == getData()[5][3] or suit == getData()[5][6]:
                    horns = [
                        getData()[3][3],
                        getData()[3][4]
                    ]
                
                else:
                    horns = [
                        getData()[3][0],
                        getData()[3][1]
                    ]
                    
            else:
                horns = [
                    getData()[3][0]
                ]
                
        else:
            horns = [
                getData()[3][0],
                getData()[3][1]
            ]
            
    elif character == charactersConditions()[1]:
        if suit != getData()[5][0]:
            if helmet == getData()[2][0]:
                horns = [
                    getData()[3][0],
                    getData()[3][2],
                    getData()[3][4]
                ]
            
            else:
                horns = [
                    getData()[3][0]
                ]
                
        else:
            horns = [
                getData()[3][0],
                getData()[3][1]
            ]
            
    elif character == charactersConditions()[2]:
        if suit == getData()[5][0]:
            if helmet == getData()[2][0]:
                horns = [
                    getData()[3][0],
                    getData()[3][2]
                ]
            
            else:
                horns = [
                    getData()[3][0]
                ]
            
        else:
            if helmet == getData()[2][0]:
                horns = [
                    getData()[3][0],
                    getData()[3][1],
                    getData()[3][2],
                ]
                
            else:
                horns = [
                    getData()[3][0]
                ]
        
    elif character == charactersConditions()[3]:
        if suit == getData()[5][0]:
            if helmet == getData()[2][0]:
                horns = [
                    getData()[3][0],
                    getData()[3][2],
                ]
                
            else:
                horns = [
                    getData()[3][0]
                ]
        
        else:
            if helmet == getData()[2][0]:
                horns = [
                    getData()[3][0],
                    getData()[3][4]
                ]
            
            else:
                horns = [
                    getData()[3][0]
                ]
    
    elif character == charactersConditions()[4]:
        horns = [
            getData()[3][0]
        ]

    else:
        horns = [
            getData()[3][0]
        ]

    return horns

def crownsConditions(character, suit, helmet, horn):
    crowns = []
    if character == charactersConditions()[0]:
        if suit != getData()[5][0]:
            if helmet == getData()[2][0]:
                if horn == getData()[3][0]:
                    crowns = [
                        getData()[4][0],
                        getData()[4][1],
                        getData()[4][2]
                    ]
                
                else:
                    crowns = [
                        getData()[4][0]
                    ]
                    
            else:
                crowns = [
                    getData()[4][0]
                ]
        
        else:
            if helmet == getData()[2][0]:
                if horn == getData()[3][0]:
                    crowns = [
                        getData()[4][0],
                        getData()[4][3]
                    ]
                    
                else:
                    crowns = [
                        getData()[4][0]
                    ]
                    
            else:
                crowns = [
                    getData()[4][0]
                ]

    elif character == charactersConditions()[1]:
        if suit != getData()[5][0]:
            if helmet == getData()[2][0]:
                if horn == getData()[3][0]:
                    crowns = [
                        getData()[4][1]
                    ]
                
                else:
                    crowns = [
                        getData()[4][0]
                    ]
            
            else:
                crowns = [
                    getData()[4][0]
                ]

        else:
            if horn == getData()[3][0]:
                crowns = [
                    getData()[4][0],
                    getData()[4][1]
                ]
                
            else:
                crowns = [
                    getData()[4][0]
                ]
            
    elif character == charactersConditions()[2]:
        if suit != getData()[5][0]:
            if helmet == getData()[2][0]:
                if horn == getData()[3][0]:
                    crowns = [
                        getData()[4][0],
                        getData()[4][1]
                    ]
                    
                else:
                    crowns = [
                        getData()[4][0]
                    ]
                
            else:
                crowns = [
                    getData()[4][0]
                ]
        
        else:
            if horn == getData()[3][0]:
                crowns = [
                    getData()[4][0],
                    getData()[4][1],
                    getData()[4][2]
                ]
            
            else:
                crowns = [
                    getData()[4][0]
                ]
    
    elif character == charactersConditions()[3]:
        if suit != getData()[5][0]:
            if helmet == getData()[2][0]:
                if horn == getData()[3][0]:
                    crowns = [
                        getData()[4][0],
                        getData()[4][2]
                    ]
                
                else:
                    crowns = [
                        getData()[4][0]
                    ]
                
            else:
                crowns = [
                    getData()[4][0]
                ]
        
        else:
            crowns = [
                getData()[4][0],
                getData()[4][1]
            ]

    elif character == charactersConditions()[4]:
        crowns = [
            getData()[4][0],
            getData()[4][3]
        ]

    else:
        crowns = [
            getData()[4][0],
            getData()[4][3]
        ]

    return crowns

def weaponsConditions(character, suit):
    weapons = []
    if character == charactersConditions()[0]: 
        if suit == getData()[5][0]:
            weapons = getData()[6]
            weapons.remove(getData()[6][4])
            weapons.remove(getData()[6][9])
            weapons.remove(getData()[6][10])
            weapons.remove(getData()[6][12])
        
        elif suit == getData()[5][1]:
            weapons = [
                getData()[6][0],
                getData()[6][2],
                getData()[6][3],
                getData()[6][4],
                getData()[6][6],
                getData()[6][7],
                getData()[6][12]
            ]
            
        elif suit == getData()[5][2]:
            weapons = [
                getData()[6][0],
                getData()[6][1],
                getData()[6][2],
                getData()[6][3],
                getData()[6][6],
                getData()[6][8],
                getData()[6][11]
            ]
            
        elif suit == getData()[5][4]:
            weapons = [
                getData()[6][0],
                getData()[6][1],
                getData()[6][4],
                getData()[6][7],
                getData()[6][9],
                getData()[6][11]
            ]
            
        elif suit == getData()[5][5]:
            weapons = [
                getData()[6][0],
                getData()[6][3],
                getData()[6][4],
                getData()[6][7],
                getData()[6][11],
                getData()[6][12]
            ]
        
        else:
            weapons = [
                getData()[6][0],
                getData()[6][1],
                getData()[6][4],
                getData()[6][5],
                getData()[6][8],
                getData()[6][9],     
                getData()[6][12]
            ]
            
    elif character == charactersConditions()[1]:
        weapons = [
            getData()[6][0],
            getData()[6][1],
            getData()[6][5],
            getData()[6][8],
            getData()[6][9],
            getData()[6][12],
        ]
        
    elif character == charactersConditions()[2]:
        weapons = [
            getData()[6][0],
            getData()[6][5],
            getData()[6][8],
            getData()[6][9],
            getData()[6][10],
            getData()[6][12]
        ]

    elif character == charactersConditions()[3]:
        weapons = [
            getData()[6][0],
            getData()[6][1],
            getData()[6][4],
            getData()[6][8],
            getData()[6][10],
        ]

    elif character == charactersConditions()[4]:
        weapons = [
            getData()[6][0],
            getData()[6][1],
            getData()[6][2],
            getData()[6][7]
        ]

    else:
        weapons = [
            getData()[6][0],
            getData()[6][1],
            getData()[6][6],
            getData()[6][10]
        ]
             
    return weapons

def wingsConditions(character, suit):
    wings = []
    if character == charactersConditions()[0]:
        if suit == getData()[5][0]:
            wings = getData()[7]
            wings.remove(getData()[7][1])
            
        else:
            wings = [
                getData()[7][0],
                getData()[7][5],
                getData()[7][6]
            ]
        
    elif character == charactersConditions()[1]:
        wings = [
            getData()[7][0],
            getData()[7][1],
            getData()[7][2],
            getData()[7][3]
        ]

    elif character == charactersConditions()[2]:
        wings = [
            getData()[7][0],
            getData()[7][2],
            getData()[7][3],
            getData()[7][5],
            getData()[7][6]
        ]
        
    elif character == charactersConditions()[3]:
        wings = [
            getData()[7][2],
            getData()[7][5],
            getData()[7][6]
        ]

    elif character == charactersConditions()[4]:
        wings = [
            getData()[7][0],
            getData()[7][1],
            getData()[7][5],
            getData()[7][6],
        ]

    else:
        wings = [
           getData()[7][1],
           getData()[7][2],
           getData()[7][5] 
        ]
         
    return wings

def logosConditions(character, suit):
    logos = []
    if character == charactersConditions()[0]:
        if suit == getData()[5][0]:
            logos = [
                getData()[8][1],
                getData()[8][2]
            ]
        
        else:
            logos = [
                getData()[8][0]
            ]
        
    elif character == charactersConditions()[1]:
        if suit == getData()[5][0]:
            logos = [
                getData()[8][2]
            ]
        
        else:
            logos = [
                getData()[8][0]
            ]
    
    elif character == charactersConditions()[2]:
        if suit == getData()[5][0]:
            logos = [
                getData()[8][4]
            ]
        
        else:
            logos = [
                getData()[8][0]
            ]
        
    elif character == charactersConditions()[3]:
        if suit == getData()[5][0]:
            logos = [
                getData()[8][5]
            ]
            
        else:
            logos = [
                getData()[8][0]
            ]

    elif character == charactersConditions()[4]:
        if suit == getData()[5][0]:
            logos = [
                getData()[8][5]
            ]
        
        else:
            logos = [
                getData()[8][0]
            ]

    else:
        if suit == getData()[5][0]:
            logos = [
                getData()[8][5]
            ]
        
        else:
            logos = [
                getData()[8][0]
            ]

    return logos