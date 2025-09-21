from Dictionaries import WeaponsDictionary, BackgroundsDictionary, MainCharactersDictionary,\
CrownsDictionary, LogosDictionary, WingsDictionary, SuitsDictionary, HelmetsDictionary , HornsDictionary

def getData():
    MainCharactersList, BackgroundsList, SuitsList, HornsList , WeaponsList,\
    HelmetsList, WingsList, LogosList , CrownsList = [], [], [], [], [], [], [], [], []

    for i in BackgroundsDictionary:
        BackgroundsList.append(BackgroundsDictionary[i])
        
    for i in MainCharactersDictionary:
        MainCharactersList.append(MainCharactersDictionary[i])

    for i in SuitsDictionary:
        SuitsList.append(SuitsDictionary[i])

    for i in HelmetsDictionary:
        HelmetsList.append(HelmetsDictionary[i])
        
    for i in HornsDictionary:
        HornsList.append(HornsDictionary[i])

    for i in WeaponsDictionary:
        WeaponsList.append(WeaponsDictionary[i])

    for i in WingsDictionary:
        WingsList.append(WingsDictionary[i])
        
    for i in LogosDictionary:
        LogosList.append(LogosDictionary[i])
    
    for i in CrownsDictionary:
        CrownsList.append(CrownsDictionary[i])
        
    return BackgroundsList, MainCharactersList, HelmetsList , HornsList, \
    CrownsList, SuitsList, WeaponsList, WingsList, LogosList
