# 8kyu - Volume of a Cuboid

""" Bob needs a fast way to calculate the volume of a cuboid with three values: 
length, width and the height of the cuboid. Write a function to help Bob with this calculation. """


def getVolumeOfCubiod(length, width, height):
    return length * width * height


q = getVolumeOfCubiod(1, 2, 2)  # 4
q
q = getVolumeOfCubiod(6.3, 2, 5)  # 63
q
