def ogon(tab):
    if jestPusta(tab) == True:
        nowaTablica = []
        for i in range(1, len(tab)):
            nowaTablica.append(tab[i])
        return nowaTablica


def glowa(tab):
    if jestPusta(tab) == True:
        return tab[0]


def jestPusta(tab):
    if len(tab) != 0:
        return True
    else:
        return False


def sprawdzam(Tab1, Tab2):
    if not jestPusta(Tab1) or not jestPusta(Tab2):
        return
    if glowa(Tab1) < glowa(Tab2):
        return sprawdzam(ogon(Tab1), Tab2)
    elif glowa(Tab1) > glowa(Tab2):
        return sprawdzam(Tab1, ogon(Tab2))
    elif glowa(Tab1) == glowa(Tab2):
        wspolnaTablica.append(glowa(Tab1))
        return sprawdzam(ogon(Tab1), ogon(Tab2))


Tab1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Tab2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
wspolnaTablica = []

sprawdzam(Tab1, Tab2)

print(Tab1)
print(Tab2)
print(wspolnaTablica)
