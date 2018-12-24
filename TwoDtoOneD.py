
def convert(dimension):
    oneD = []
    for i in range(dimension):
        for j in range(dimension):
            oneD.append((j * dimension) + i)
    return oneD

print(convert(10))
