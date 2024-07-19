szamlista = [1, 5, 4, 3, 7, 8, 8, 9, -5, 4, 5]
rendezett_lista = []
# -5 1 ... 9
szam = 0
for i in range(min(szamlista), max(szamlista) + 1): #[-5, -4, -3, ..., 8, 9]
    for elem in szamlista: #[1, 5, 4, 3, 7, 8, 8, 9, -5, 4, 5]
        if elem == i and elem not in rendezett_lista:
            rendezett_lista.append(elem)
print(f"Íme a rendezett lista 1:", *rendezett_lista, "folytatom ")
print(f"Íme a rendezett lista 2:", rendezett_lista, "folytatom. ") # ez a sor, meg a következő teljesen ugyanaz.
print(f"Íme a rendezett lista 3: {rendezett_lista} folytatom. ")


# futtatunk egy range-et (kilengés = range) induljon a minimumától (-5),
# és menjen el a maxig (9). i_1 = -5, i_2 = -4, i_3 = -3 .... i_n = 8
# nézzük a legelső i-t, amikor egyenlő -5-tel.
# Belemegy a második for ciklusba, és végigfuttatja a szamlista listát.
# És hogyha kiszúrja, hogy hoppá, a szamlistaban szerepel a jelenlegi i változonk,
# akkor appendelje a rendezett_lista-ba.
# A not in azt jelenti, hogy a listában, nincsen benne.
# Ezt általában használjuk akkor, ha nem akarjuk, hogy egy elem, érték, bármi kétszer
# szerepeljen egy listába, lásd: a fenti példán nem akarjuk, hogy pl.: a 4-es kétszer szerepeljen
# úgyhogy amikor a range i-je = 4-gyel, és azonbelül futtatja a szamlistat, és a szamlistaban
# kétszer szerepel a 4-es, akkor a második 4-est a szamlistaban nem fogja beleappendelni már
# ha odaírjuk pluszban (and) [and == és (+), or == vagy (*)], hogy not in, tehát
# nincs benne magyarul a listában, akkor ne nyúljon hozzá, ne appendelje.