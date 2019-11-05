import math

def EnoughSpaceBetween(x,y):
    if x > y:
        if 0.1 < math.log2(x) - math.log2(y) < 30:
            return  True
        else:
            return False
    else:
        if 0.1 < math.log2(y) - math.log2(x) < 30:
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

# ICh weiss nicht wie ich das machen soll habe einfach auf dem Internet kopiert
def expandedEuklidischerAlgo(Phi, e):
    return null

def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, u, v = extgcd(b, a % b)
        q = a // b
        return g, v, u - q * v


def isPrim(p, x):
    while(x < p):
        if p % x == 0:
           return False;
        x = x + 1
    print(x)
    return True


print("RSA verfahren")
while True:
    p = int(input("1. Primzalh eingeben: "))
    if not isPrim(p, 2):
        continue
    q = int(input("2. Primzalh eigeben: "))
    if not isPrim(q, 2):
        continue
    if EnoughSpaceBetween(p, q):
        N = p * q
        x = int(math.log(N, 10)+1)
        if int(math.log(N, 10)+1) >= 6:
            break


Phi = (p - 1) * (q - 1)
while True:
    e = int(input("Eine teilerfremde Zahl zu " + str(Phi) + " eingeben: "))
    if modernEuklidischerAlgo(Phi, e):
        break

(x, y, d) = extgcd(Phi, e)

print("\nDer öffentliche Schlüssel ist e = " + str(e) + " und N = " + str(N))
print("Der private Schlüssel ist d = " + str(d) + " und N = " + str(N))

m = input("\nBuchstabe eingeben: ")
c = (ord(m)**e) % N
print("\nc = ascii von m hoch e (modulo von N)")
print(str(c) + " = " + str(ord(m)) + " hoch " + str(e) + " (modulo " + str(N) + ")")
print("Der Verschlüsselte Wert von der eingabe " + m + " ist: " + str(c))
e = (c**d) % N
print("\ne = c hoch d (modulo von N)")
print(str(e) + " ist " + str(c) + " hoch " + str(d) + " (modulo " + str(N) + ")")
print("\nDer entschlüsselte Wert ist: " + chr(e))