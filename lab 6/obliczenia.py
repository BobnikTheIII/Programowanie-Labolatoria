# Adam Techman 73285
# Wstęp do programowania: Labolatorium 6

import random
import geometria as geo
import temperatura as temp
import time as time
import datetime as dt
import keyword as kw
import math as math

# 1

print("Zadanie 1")

print(geo.obwod_kola(4))
print(geo.pole_kola(4))



# 2

print("Zadanie 2")

print(temp.c_to_f(20))
print(temp.f_to_c(86))
print(temp.c_to_k(20))


# 3

# print("Zadanie 3")
# w innym pliku



# 4

print("Zadanie 4")

print("wylosuje szczemsliwa liczbe")

roczniki = [2000,2001,2002,2003,2004,2005,2006,2006,2007,2008]

print(f"Szczesliwy rocznik to {roczniki[random.randint(0,len(roczniki)-1)]}")



# 5

print("Zadanie 5")

print(f"Wygrywające liczby to: {random.randint(0,49)} {random.randint(0,49)} {random.randint(0,49)} {random.randint(0,49)} {random.randint(0,49)} {random.randint(0,49)}")




# 6

print("Zadanie 6")

sekundy = int(input("Podaj ilość sekund."))

while sekundy > 0:
    print(f"Pozostało {sekundy} sekund.")
    time.sleep(1)
    sekundy = sekundy - 1




# 7

print("Zadanie 7")

ostatnie_laby = dt.date(2025, 12, 19)
kolokwium = dt.date(2026, 1, 16)
dzisiaj = dt.date.today()

dni_od = (dzisiaj - ostatnie_laby).days
dni_do = (kolokwium - dzisiaj).days


print(f"Dzisiaj jest: {dzisiaj}")
print(f"Od 19.12.2025 minęło dni: {dni_od}")
print(f"Do 16.01.2026 pozostało dni: {dni_do}")



# 8

print("Zadanie 8")

print(kw.iskeyword("for")) 
print(kw.iskeyword("print")) 
print(kw.iskeyword("break")) 
print(kw.iskeyword("done")) 
print(kw.iskeyword("bad")) 



# 9

print("Zadanie 9")

print(f"Math: {dir(math)}\nTuple: {dir(tuple)}\nKeyword: {dir(kw)}")


# 10

print("Zadanie 10")

pocz = int(input("Podaj poczatek przedzialu"))
kon = int(input("Podaj koniec przedzialu"))

krotka = (random.randint(pocz,kon),random.randint(pocz,kon),random.randint(pocz,kon),random.randint(pocz,kon),random.randint(pocz,kon),random.randint(pocz,kon),random.randint(pocz,kon),random.randint(pocz,kon),random.randint(pocz,kon),random.randint(pocz,kon),)

print(sum(krotka)/len(krotka))