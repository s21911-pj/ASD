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


def rewersSłowa(rewers):
    if not jestPusta(rewers):
        return
    noweSłowo = glowa(rewers)
    rewersSłowa(ogon(rewers))
    print(noweSłowo, end='')


rewers = "słowo do rewersu"
rewersSłowa(list(rewers))
