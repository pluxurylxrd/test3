def treug(x,y,z):
    if ((x+y) > z) and ((x+z) > y) and ((y+z) > x):
        return True
    return False
def ostr(x,y,z):
    if (x**2 < y**2 + z**2) or (y**2 < x**2 + z**2) or (z**2 < x**2 + y**2):
        return True
    return False
print(treug(2,4,5))
print(ostr(2,4,5))