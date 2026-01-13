# Adam Techman 73285
# Wstęp do programowania: Labolatorium 8

# 1

import matplotlib.pyplot as plt
import numpy as np
import random as rnd

print("Zadanie 1")

kategorie = ['Art. spożywcze', 'Elektronika', 'Odzież', 'Art. meblowe']
wartosci = [10, 20, 15, 25]
plt.bar(kategorie, wartosci)
plt.title('Sprzedaż produktów wedle kategorii')
plt.xlabel('Kategoria')
plt.ylabel('Liczba sprzedanych produktów')
plt.show()



# 2

print("Zadanie 2")

kategorie = ['Art. spożywcze', 'Elektronika', 'Odzież', 'Art. meblowe']
wartosci = [10, 20, 15, 25]
plt.title('Procent sprzedaży produktów wedle kategorii')
plt.pie(wartosci, labels=kategorie,autopct='%1.f%%', startangle=90,colors=['skyblue', 'lightgreen','lightcoral', 'gold'])
plt.show()



# 3

print("Zadanie 3")

x = [1, 2, 3, 4, 5]
y = [7, 16, 37, 61, 72]
plt.scatter(x, y)
plt.title('Prędkość pojazdu w czasie')
plt.xlabel('Czas [s]')
plt.ylabel('Prędkość pojazdu [km/h]')
plt.show()



# 4

print("Zadanie 4")

binarium = np.array([128,64,32,16,8,4,2,1])
wagi = np.array([7,6,5,4,3,2,1,0])

liczba_bin = np.array([1,0,1,1,1,0,1,1])

# print(binarium, wagi, liczba_bin)

def wartosc_liczby_bin():
    wartoscBIN = 0
    for i in range(len(liczba_bin)):
        wartoscBIN = wartoscBIN + (liczba_bin[i] * binarium[i])
    print(f"Wartosc losowej liczby bninarnej to {wartoscBIN}")

wartosc_liczby_bin()



# 5

print("Zadanie 5")

macierz5 = np.random.randint(0, 100, size=(5, 5))

print("Wygenerowana macierz:")
print(macierz5)
print("-" * 30)

m_max = macierz5.max()
m_min = macierz5.min()

print(f"Największy element w całej macierzy: {m_max}")
print(f"Najmniejszy element w całej macierzy: {m_min}")
print("-" * 30)

r_max = macierz5.max(axis=1)

k_max = macierz5.max(axis=0)

print(f"Największe elementy w wierszach: {r_max}")
print(f"Największe elementy w kolumnach: {k_max}")
print("-" * 30)

r_suma = macierz5.sum(axis=1)

print(f"Suma wartości w wierszach: {r_suma}")


# 6

print("Zadanie 6")

A = np.array([[0,0,0],[0,0,0],[1,1,1]])
B = np.array([[0,0,0],[0,1,0],[0,1,0]])
C = np.array([[0,0,0],[1,1,1],[1,1,1]])
D = np.array([[1,0,1],[1,0,1],[0,0,0]])
E = np.array([[0,0,0],[0,1,1],[0,1,1]])


print(A,"\n\n",B,"\n\n",C,"\n\n",D,"\n\n",E)

# 7

print("Zadanie 7")

macierz5 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
# funkcja poniżej jest kawałkiem naprawdę profesionalnego kodu. Proszę o docenienie jej złożoności.
def zamiana_granic(m):
    rand1 = 0
    rand2 = 0
    zmiennik = 0

    if m[0][0] == 0:
        zmiennik = 1

    for _ in range(9999):
        rand1 = rnd.randint(0,4)
        rand2 = rnd.randint(0,1)*4
        m[rand1][rand2] = zmiennik
        m[rand2][rand1] = zmiennik

    return m

print(macierz5)

macierz5 = zamiana_granic(macierz5)

print(macierz5)

# 8

print("Zadanie 8")

macierz = np.random.randint(0, 101, size=(5, 5))

print("Wylosowana macierz:")
print(macierz)
print("-" * 30)

w_sub20 = macierz[macierz > 20]

print(f"Elementy > 20: {w_sub20}")

licz = len(w_sub20)
print(f"Liczba elementów większych niż 20: {licz}")

macierz_mean = macierz.mean()
print(f"Średnia wartości całej tablicy: {macierz_mean:.2f}")