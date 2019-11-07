import math
from tkinter import *
# from appJar import gui


def EnoughSpaceBetween(x, y):
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


# Ich weiss nicht wie ich das machen soll habe einfach auf dem Internet kopiert
def expandedEuklidischerAlgo(Phi, e):
    return null


def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, u, v = extgcd(b, a % b)
        q = a // b
        return g, v, u - q * v


def isprim(p, x):
    while(x < p):
        if p % x == 0:
           return False
        x = x + 1
    print(x)
    return True


# app = gui()
# master = Tk(screenName=ACTIVE)
# c = Canvas(master, width=200, height=200)
# c.pack()
# c.create_rectangle(50, 50, 150, 150, fill="blue")
# mainloop()

print("RSA verfahren")
while True:
    p = int(input("1. Primzahl eingeben: "))
    if not isprim(p, 2):
        continue
    q = int(input("2. Primzahl eingeben: "))
    if not isprim(q, 2):
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
        (x, y, d) = extgcd(Phi, e)
        if d > 0:
            break

# Ich verstehe nicht ganz wann e valid ist und wann e nicht funktioniert


print("\nDer öffentliche Schlüssel ist e = " + str(e) + " und N = " + str(N))
print("Der private Schlüssel ist d = " + str(d) + " und N = " + str(N))

m = input("\nBuchstabe eingeben: ")

c = (ord(m)**e) % N
print("\nc = ascii von " + m + " hoch e (modulo von N)")
print(str(c) + " = " + str(ord(m)) + " hoch " + str(e) + " (modulo " + str(N) + ")")
print("Der Verschlüsselte Wert von der eingabe " + m + " ist: " + str(c))

erg = (c**d) % N
print("\ne = c hoch d (modulo von N)")
print(str(erg) + " ist " + str(c) + " hoch " + str(d) + " (modulo " + str(N) + ")")
print("Der entschlüsselte Wert ist: " + chr(erg))
input("Waiting ...")
