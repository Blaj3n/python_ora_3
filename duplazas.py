szamlista = [1, 5, 4, 3, 7, 8, 8, 9, -5, 4, 5]
szamlista_2 = [] # [2, 10, 8, 6, 14...]
for elem in szamlista:
    szamlista_2.append(elem * 2)
print(f"A számlista elemek duplázása 1: {szamlista_2} ")

# második megoldás
def duplazas(szam:int):
    return szam * 2
print(f"Duplázás metódussal: {duplazas(5)} ")

szamlista_2 = [] # [2, 10, 8, 6, 14...]
for elem in szamlista:
    szamlista_2.append(duplazas(elem))
print(f"A számlista elemek duplázása 2:", *szamlista_2)

# elem = szamlista[0]
# elem = szamlista[1]
# elem = szamlista[2]
# ...
# elem = szamlista[len(szamlista) - 1]
