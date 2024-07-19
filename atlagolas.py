# hány perc az átlaga?
ido = ['11:23', '12:35', '12:56', '13:41', '14:54', '15:30']

def mpbe(ora:int, perc:int):
    return (ora * 60) + perc
# megtudjuk, hogy az időpont hanyadik perce a napnak. 11:23 == 683. perce a napnak.

mpbe_ben = [] #[683, 755, 776, ..., 930]
for egyelem in ido:
    mpbe_ben.append(mpbe(int(egyelem.split(":")[0]), int(egyelem.split(":")[1]))) # mpbe(11, 23)
print(mpbe_ben)

print(f"Az idő átlaga (percben): {sum(mpbe_ben) // len(mpbe_ben)} ")

# a split elválaszt valami mentén, ez esetben a ":"-nál elválaszt.
# egyelem.split(":")[0] -> egyelem-et szétválasztja a kettőspontnál,
# ha az index 0 [0], akkor az elválasztásjel baloldalát adja csak vissza -> 11
# ha az index 1 [1], akkor a jobboldalát -> 23
