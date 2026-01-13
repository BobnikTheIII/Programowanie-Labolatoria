# Adam Techman 73285
# Wstęp do programowania: Labolatorium 7

import pandas as pd

# 1

print("Zadanie 1")

dane = pd.read_csv("demografia.csv", na_values=['.'], decimal=".")

print(dane)



# 2

print("Zadanie 2")

max_przyrost = dane["2022"].idxmax(skipna=True)

print(f"Kraj z najwiekszym pryrostem naturalnym w 2022 to: {dane.loc[max_przyrost,"KRAJE"]}")



# 3

print("Zadanie 3")

dane_bez_krajow = dane.drop(columns=["KRAJE"])

dane_max_przyrost = dane_bez_krajow.max().max()

dane_rok_max_przyrost = dane_bez_krajow.max().idxmax()

dane_idx_max_przyrost = dane_bez_krajow[dane_rok_max_przyrost].idxmax()

dane_kraj_max_przyrost = dane.loc[dane_idx_max_przyrost,"KRAJE"]

print(f"Kraj z największym przyrostem naturalnym: {dane_kraj_max_przyrost}")



# 4

print("Zadanie 4")

data = {
    'ID': [1, 2, 3, 4, 5],
    'Imie': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
}

dane = pd.DataFrame(data)

print(" Oryginalna Ramka Danych ")
print(dane)
print("\n" + "="*40 + "\n")

wysoka_pensja = dane[dane['Pensja'] > 5000]
print(" a) Pracownicy z pensją > 5000 PLN ")
print(wysoka_pensja)

posortowani_wiek = dane.sort_values(by='Wiek')
print("\n b) Pracownicy posortowani według wieku ")
print(posortowani_wiek)

srednia_pensja = dane.groupby('Stanowisko')['Pensja'].mean().reset_index()
print("\n c) Średnia pensja na stanowisko ")
print(srednia_pensja)

dane_zmiany = {
    'ID': [2, 4],
    'Nowe_Stanowisko': ['Senior Programista', 'Team Leader']
}
dane_zmiany = pd.DataFrame(dane_zmiany)

dane_polaczona = pd.merge(dane, dane_zmiany, on='ID', how='left')

print("\n d) Ramka połączona z informacjami o awansach ")
print(dane_polaczona)

nazwa_pliku = 'pracownicy.csv'
dane.to_csv('pracownicy.csv', index=False)

try:
    dane_wczytana = pd.read_csv('pracownicy.csv')
    print("Wczytano dane poprawnie.")
except FileNotFoundError:
    print("Błąd: Plik nie został znaleziony.")



# 5

print("Zadanie 5")


data = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imie': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}

dane = pd.DataFrame(data)

oceny_dobre = dane[dane['Ocena'] > 4]
print(" a) Studenci z oceną > 4 ")
print(oceny_dobre)

dane_sort_wiek = dane.sort_values(by='Wiek')
print("\n b) Posortowani według wieku ")
print(dane_sort_wiek)

grupy_wiek = dane.groupby('Ocena')['Wiek'].mean().reset_index()
print("\n c) Średnia wieku dla poszczególnych ocen ")
print(grupy_wiek)

dane_poprawa = {
    'Nr_albumu': [2, 5],
    'Ocena_Poprawa': [3.5, 3.0]
}
dane_poprawa = pd.DataFrame(dane_poprawa)

dane_polaczona = pd.merge(dane, dane_poprawa, on='Nr_albumu', how='left')

print("\n d) Ramka połączona z wynikami poprawy ")
print(dane_polaczona)

nazwa_pliku = 'studenci.csv'
dane_polaczona.to_csv(nazwa_pliku, index=False, encoding='utf-8')
print(f"\n e) Zapisano dane do pliku: {nazwa_pliku} ")

try:
    dane_wczytana = pd.read_csv(nazwa_pliku, encoding='utf-8')
    print("\n f) Poprawnie wczytano dane z pliku ")
    print(dane_wczytana.head())
except FileNotFoundError:
    print("Błąd: Plik nie został znaleziony.")

nowy_student = pd.DataFrame({
    'Nr_albumu': [6],
    'Imie': ['Piotr'],
    'Nazwisko': ['Lewandowski'],
    'Ocena': [4.0],
    'Wiek': [22],
    'Ocena_Poprawa': [None]
})

dane_polaczona = pd.concat([dane_polaczona, nowy_student], ignore_index=True)
print("\n g) DataFrame po dodaniu nowego studenta ")
print(dane_polaczona.tail())

unikalne_oceny = dane['Ocena'].unique()
print("\n h) Unikalne oceny (z pierwszego terminu) ")
print(unikalne_oceny)

liczba_iatek = dane[dane['Ocena'] == 5.0].shape[0]
print(f"\n i) Liczba studentów z oceną 5.0: {liczba_iatek} ")