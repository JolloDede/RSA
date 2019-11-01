import math

def EnoughSpaceBetween(x,y):
    if x > y:
        if 0.1 > math.log2(y) - math.log2(x) > 30:
            return  True
        else:
            return False
    else:
        if 0.1 > math.log2(y) - math.log2(x) > 30:
            return True
        else:
            return False


def modernEuklidischerAlgo(a, b):
    if b == 1:
        return True
    if b == 0:
        return False
    else:
        return modernEuklidischerAlgo(b, a % b)


def expandedEuklidischerAlgo(Phi, e):
    


def isPrim(p, x):
    while(x < p):
        if p % x == 0:
           return False;
        x = x + 1
    print(x)
    return True


while True:
    p = int(input("1. Primzalh eingeben: "))
    if not isPrim(p):
        continue
    q = int(input("2. Primzalh eigeben: "))
    if not isPrim(q):
        continue
    if EnoughSpaceBetween(p, q):
        RSAModul = p * q
        if int(math.log(RSAModul, 10)+1) > 6:
            break

Phi = (p - 1) * (q - 1)
while True:
    e = int(input("Eine teilerfremde Zahl zu "+Phi+" eingeben: "))
    if modernEuklidischerAlgo(Phi, e):
        break

