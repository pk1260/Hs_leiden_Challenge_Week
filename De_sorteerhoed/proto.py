def resultaat():
    antwoorden = ['fict', 'fict', 'se', 'se', 'se', 'iat', 'bdam', 'fict']
    fict_aantal = antwoorden.count('fict')
    se_aantal = antwoorden.count('se')
    bdam_aantal = antwoorden.count('bdam')
    iat_aantal = antwoorden.count('iat')
    print(fict_aantal)
    print(se_aantal)
    print(iat_aantal)
    print(bdam_aantal)
    aantal_lijst = {
        'fict': fict_aantal,
        'se': se_aantal,
        'iat': iat_aantal,
        'bdam': bdam_aantal
    }

# dictA = {'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 4}
#changes
    print("Given Dictionary :", aantal_lijst)

    dictB = {}
    for key, value in aantal_lijst.items():
        dictB.setdefault(value, set()).add(key)

    res = max(filter(lambda x: len(x) > 1, dictB.values()))
    res_lijst = list(res)
# Result
    print("New Dictionary:", res)
    if len(res) > 1:
        print('is meer dan 1 gelijk')
    else:
        print("1 resultaat")


resultaat()
# print(max_key)
# print(aantal_lijst)
# print(max(aantal_lijst))
# max_key = max(aantal_lijst, key=aantal_lijst.get)
# print("Er zijn meerdere gelijke resultante")
# else:
