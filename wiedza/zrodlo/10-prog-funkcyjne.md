### Blok 10: Podstawy programowania funkcyjnego i wyrażenia lambda

Poniższy rozdział wprowadza w podstawy programowania funkcyjnego w Pythonie, omawiając kluczowe koncepcje takie jak funkcje anonimowe (`lambda`), wbudowane funkcje `map`, `filter`, `reduce`, a także wyrażenia listowe (`list comprehensions`) i słownikowe (`dict comprehensions`). Zrozumienie tych narzędzi pozwoli na pisanie bardziej zwięzłego i czytelnego kodu, zwłaszcza w kontekście przetwarzania danych. W części praktycznej zobaczymy, jak zastosować te konstrukcje do efektywnego manipulowania listami i słownikami, porównując je z tradycyjnymi pętlami.

---
    
### 1. Wprowadzenie do programowania funkcyjnego

**Programowanie funkcyjne** to paradygmat programowania, który traktuje obliczenia jako ewaluację funkcji matematycznych i unika zmian stanu oraz danych mutowalnych. W Pythonie, choć jest to język wieloparadygmatowy, można skutecznie wykorzystywać techniki funkcyjne, co pozwala na pisanie bardziej zwięzłego, czytelnego i efektywnego kodu.

Główne cechy programowania funkcyjnego:

- **Funkcje jako obiekty pierwszej klasy:** Funkcje mogą być przekazywane jako argumenty, zwracane jako wartości i przypisywane do zmiennych.
- **Immutability (niemutowalność):** Preferowanie struktur danych, które nie zmieniają swojego stanu po utworzeniu.
- **Brak efektów ubocznych:** Funkcje nie powinny modyfikować zewnętrznego stanu.
- **Funkcje wyższego rzędu:** Funkcje, które przyjmują inne funkcje jako argumenty lub zwracają funkcje.

W Pythonie programowanie funkcyjne jest wspierane przez takie narzędzia jak `lambda`, `map`, `filter`, `reduce`, oraz wyrażenia listowe i słownikowe, które pozwalają na eleganckie przetwarzanie danych.

---
    
### 2. Funkcje anonimowe (`lambda`)

Funkcje anonimowe, znane jako `lambda`, to krótkie, jednowierszowe funkcje bez nazwy. Są użyteczne, gdy potrzebujemy funkcji na krótki czas, bez konieczności jej pełnego definiowania za pomocą `def`.

**Składnia funkcji `lambda`:**

```python
lambda argumenty: wyrażenie
```

**Przykład:**

```python
# Tradycyjna funkcja
def dodaj(a, b):
    return a + b

# Funkcja lambda
dodaj_lambda = lambda a, b: a + b

print(dodaj(3, 5))        # 8
print(dodaj_lambda(3, 5)) # 8
```

**Użycie funkcji `lambda` w kontekście funkcji wyższego rzędu:**

```python
# Funkcja sortująca listę słowników po kluczu 'wiek'
osoby = [
    {"imie": "Jan", "wiek": 25},
    {"imie": "Ala", "wiek": 30},
    {"imie": "Tomek", "wiek": 20}
]

osoby.sort(key=lambda osoba: osoba["wiek"])
print(osoby)
# Wynik: [{'imie': 'Tomek', 'wiek': 20}, {'imie': 'Jan', 'wiek': 25}, {'imie': 'Ala', 'wiek': 30}]
```

Funkcje `lambda` są szczególnie przydatne w miejscach, gdzie potrzebujemy małej funkcji jako argumentu, np. w `map`, `filter`, czy `sorted`.

---
    
### 3. Funkcje wbudowane: `map`, `filter`, `reduce`

Python oferuje kilka wbudowanych funkcji, które wspierają programowanie funkcyjne. Trzy z najważniejszych to `map`, `filter` oraz `reduce`. Funkcja `reduce` jest dostępna w module `functools`.

#### 3.1. `map`

Funkcja `map` stosuje daną funkcję do każdego elementu iterowalnego (np. listy) i zwraca iterator z wynikami.

**Składnia:**

```python
map(funkcja, iterowalne)
```

**Przykład:**

```python
# Podwajanie liczb w liście
liczby = [1, 2, 3, 4, 5]
podwojone = map(lambda x: x * 2, liczby)
print(list(podwojone)) # [2, 4, 6, 8, 10]
```

#### 3.2. `filter`

Funkcja `filter` stosuje daną funkcję logiczną (zwracającą `True` lub `False`) do każdego elementu iterowalnego i zwraca iterator z elementami, dla których funkcja zwróciła `True`.

**Składnia:**

```python
filter(funkcja_logiczna, iterowalne)
```

**Przykład:**

```python
# Filtracja liczb parzystych
liczby = [1, 2, 3, 4, 5, 6]
parzyste = filter(lambda x: x % 2 == 0, liczby)
print(list(parzyste)) # [2, 4, 6]
```

#### 3.3. `reduce`

Funkcja `reduce` stosuje daną funkcję do pierwszych dwóch elementów iterowalnego, a następnie do wyniku i kolejnego elementu, aż do przetworzenia całej sekwencji. Jest dostępna w module `functools`.

**Składnia:**

```python
from functools import reduce
reduce(funkcja, iterowalne, [wartość_początkowa])
```

**Przykład:**

```python
from functools import reduce

# Sumowanie wszystkich liczb w liście
liczby = [1, 2, 3, 4, 5]
suma = reduce(lambda a, b: a + b, liczby)
print(suma) # 15

# Mnożenie wszystkich liczb w liście z wartością początkową 1
iloczyn = reduce(lambda a, b: a * b, liczby, 1)
print(iloczyn) # 120
```

Funkcje `map`, `filter` i `reduce` są potężnymi narzędziami do przetwarzania danych, umożliwiającymi pisanie bardziej deklaratywnego kodu bez konieczności używania tradycyjnych pętli.

---
    
### 4. List comprehensions i dict comprehensions

**List comprehensions** oraz **dict comprehensions** to zwięzłe sposoby tworzenia nowych list i słowników na podstawie istniejących iterowalnych obiektów, z opcjonalnym zastosowaniem filtrów i transformacji.

#### 4.1. List comprehensions

List comprehensions umożliwiają tworzenie nowych list w sposób bardziej czytelny i zwięzły niż tradycyjne pętle.

**Składnia:**

```python
nowa_lista = [wyrażenie for element in iterowalne [if warunek]]
```

**Przykład:**

```python
# Podwajanie liczb w liście
liczby = [1, 2, 3, 4, 5]
podwojone = [x * 2 for x in liczby]
print(podwojone) # [2, 4, 6, 8, 10]

# Filtracja liczb parzystych
parzyste = [x for x in liczby if x % 2 == 0]
print(parzyste) # [2, 4]
```

#### 4.2. Dict comprehensions

Podobnie jak list comprehensions, dict comprehensions pozwalają na tworzenie słowników w zwięzły sposób.

**Składnia:**

```python
nowy_slownik = {klucz: wartosc for element in iterowalne [if warunek]}
```

**Przykład:**

```python
# Tworzenie słownika z podwojonymi wartościami
liczby = [1, 2, 3, 4, 5]
slownik_podwojony = {x: x * 2 for x in liczby}
print(slownik_podwojony) # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

# Tworzenie słownika tylko z liczbami parzystymi
slownik_parzyste = {x: x ** 2 for x in liczby if x % 2 == 0}
print(slownik_parzyste) # {2: 4, 4: 16}
```

List i dict comprehensions są nie tylko bardziej zwięzłe, ale często również bardziej efektywne niż ich odpowiedniki z użyciem pętli.

---
    
### 5. Zastosowania funkcyjnych konstrukcji do przetwarzania danych

Programowanie funkcyjne w Pythonie jest szczególnie przydatne w kontekście przetwarzania i analizy danych, gdzie często operujemy na dużych zbiorach informacji. Funkcje `lambda`, `map`, `filter`, `reduce`, oraz comprehensions umożliwiają szybkie i czytelne manipulowanie danymi.

**Przykładowe zastosowania:**

- **Transformacja danych:** Przemiana jednych wartości w inne.
- **Filtrowanie danych:** Wybieranie tylko tych elementów, które spełniają określone kryteria.
- **Agregacja danych:** Sumowanie, mnożenie, czy inne operacje na zbiorach danych.
- **Tworzenie nowych struktur danych:** Generowanie list, słowników, zbiorów na podstawie istniejących danych.

**Przykład:**

Załóżmy, że mamy listę produktów, a każdy produkt jest reprezentowany jako słownik z nazwą i ceną. Chcemy:

1. Podnieść cenę każdego produktu o 10%.
2. Filtrujemy tylko te produkty, których cena jest większa niż 20 zł.
3. Obliczamy łączną wartość tych produktów.

**Tradycyjny sposób z pętlami:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 15},
    {"nazwa": "Produkt B", "cena": 25},
    {"nazwa": "Produkt C", "cena": 20},
    {"nazwa": "Produkt D", "cena": 30}
]

# Podniesienie ceny o 10%
for p in produkty:
    p["cena"] *= 1.1

# Filtrowanie produktów droższych niż 20 zł
drogie_produkty = []
for p in produkty:
    if p["cena"] > 20:
        drogie_produkty.append(p)

# Obliczenie łącznej wartości
suma = 0
for p in drogie_produkty:
    suma += p["cena"]

print(f"Łączna wartość drogich produktów: {suma:.2f} zł")
```

**Funkcyjny sposób:**

```python
from functools import reduce

produkty = [
    {"nazwa": "Produkt A", "cena": 15},
    {"nazwa": "Produkt B", "cena": 25},
    {"nazwa": "Produkt C", "cena": 20},
    {"nazwa": "Produkt D", "cena": 30}
]

# Podniesienie ceny o 10%
podniesione = list(map(lambda p: {"nazwa": p["nazwa"], "cena": p["cena"] * 1.1}, produkty))

# Filtrowanie produktów droższych niż 20 zł
drogie_produkty = list(filter(lambda p: p["cena"] > 20, podniesione))

# Obliczenie łącznej wartości
suma = reduce(lambda acc, p: acc + p["cena"], drogie_produkty, 0)

print(f"Łączna wartość drogich produktów: {suma:.2f} zł")
```

Ten drugi sposób jest bardziej zwięzły i deklaratywny, co ułatwia czytanie i zrozumienie kodu, zwłaszcza gdy operujemy na dużych zbiorach danych.

---
    
### 6. Praktyka: Przetwarzanie list i słowników z wykorzystaniem `lambda`, `map`, `filter`

W tej sekcji przećwiczymy zastosowanie funkcji anonimowych oraz funkcji `map` i `filter` do przetwarzania list i słowników, porównując je z tradycyjnymi pętlami.

#### 6.1. Przykład 1: Podniesienie cen produktów o 10%

**Tradycyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 15},
    {"nazwa": "Produkt B", "cena": 25},
    {"nazwa": "Produkt C", "cena": 20}
]

for p in produkty:
    p["cena"] *= 1.1

print(produkty)
# Wynik: [{'nazwa': 'Produkt A', 'cena': 16.5}, {'nazwa': 'Produkt B', 'cena': 27.5}, {'nazwa': 'Produkt C', 'cena': 22.0}]
```

**Funkcyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 15},
    {"nazwa": "Produkt B", "cena": 25},
    {"nazwa": "Produkt C", "cena": 20}
]

podniesione = list(map(lambda p: {"nazwa": p["nazwa"], "cena": p["cena"] * 1.1}, produkty))
print(podniesione)
# Wynik: [{'nazwa': 'Produkt A', 'cena': 16.5}, {'nazwa': 'Produkt B', 'cena': 27.5}, {'nazwa': 'Produkt C', 'cena': 22.0}]
```

#### 6.2. Przykład 2: Filtracja produktów droższych niż 20 zł

**Tradycyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 16.5},
    {"nazwa": "Produkt B", "cena": 27.5},
    {"nazwa": "Produkt C", "cena": 22.0}
]

drogie_produkty = []
for p in produkty:
    if p["cena"] > 20:
        drogie_produkty.append(p)

print(drogie_produkty)
# Wynik: [{'nazwa': 'Produkt B', 'cena': 27.5}, {'nazwa': 'Produkt C', 'cena': 22.0}]
```

**Funkcyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 16.5},
    {"nazwa": "Produkt B", "cena": 27.5},
    {"nazwa": "Produkt C", "cena": 22.0}
]

drogie_produkty = list(filter(lambda p: p["cena"] > 20, produkty))
print(drogie_produkty)
# Wynik: [{'nazwa': 'Produkt B', 'cena': 27.5}, {'nazwa': 'Produkt C', 'cena': 22.0}]
```

#### 6.3. Przykład 3: Obliczenie łącznej wartości drogich produktów

**Tradycyjny sposób:**

```python
drogie_produkty = [
    {"nazwa": "Produkt B", "cena": 27.5},
    {"nazwa": "Produkt C", "cena": 22.0}
]

suma = 0
for p in drogie_produkty:
    suma += p["cena"]

print(f"Łączna wartość drogich produktów: {suma:.2f} zł")
# Wynik: Łączna wartość drogich produktów: 49.50 zł
```

**Funkcyjny sposób:**

```python
from functools import reduce

drogie_produkty = [
    {"nazwa": "Produkt B", "cena": 27.5},
    {"nazwa": "Produkt C", "cena": 22.0}
]

suma = reduce(lambda acc, p: acc + p["cena"], drogie_produkty, 0)
print(f"Łączna wartość drogich produktów: {suma:.2f} zł")
# Wynik: Łączna wartość drogich produktów: 49.50 zł
```

#### 6.4. Przykład 4: Tworzenie słownika nazw produktów i ich cen

**Tradycyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 16.5},
    {"nazwa": "Produkt B", "cena": 27.5},
    {"nazwa": "Produkt C", "cena": 22.0}
]

slownik_produktow = {}
for p in produkty:
    slownik_produktow[p["nazwa"]] = p["cena"]

print(slownik_produktow)
# Wynik: {'Produkt A': 16.5, 'Produkt B': 27.5, 'Produkt C': 22.0}
```

**Funkcyjny sposób z użyciem dict comprehensions:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 16.5},
    {"nazwa": "Produkt B", "cena": 27.5},
    {"nazwa": "Produkt C", "cena": 22.0}
]

slownik_produktow = {p["nazwa"]: p["cena"] for p in produkty}
print(slownik_produktow)
# Wynik: {'Produkt A': 16.5, 'Produkt B': 27.5, 'Produkt C': 22.0}
```

---
    
### 7. Praktyka: Skrócenie kodu w stosunku do tradycyjnych pętli

W tej sekcji zobaczymy, jak zastosowanie technik funkcyjnych pozwala na skrócenie i uproszczenie kodu, jednocześnie zwiększając jego czytelność.

#### 7.1. Przykład: Tworzenie listy kwadratów liczb parzystych

**Tradycyjny sposób:**

```python
liczby = [1, 2, 3, 4, 5, 6]
kwadraty_parzystych = []
for x in liczby:
    if x % 2 == 0:
        kwadraty_parzystych.append(x ** 2)
print(kwadraty_parzystych)
# Wynik: [4, 16, 36]
```

**Funkcyjny sposób z użyciem list comprehensions:**

```python
liczby = [1, 2, 3, 4, 5, 6]
kwadraty_parzystych = [x ** 2 for x in liczby if x % 2 == 0]
print(kwadraty_parzystych)
# Wynik: [4, 16, 36]
```

**Funkcyjny sposób z użyciem `filter` i `map`:**

```python
liczby = [1, 2, 3, 4, 5, 6]
parzyste = filter(lambda x: x % 2 == 0, liczby)
kwadraty_parzystych = list(map(lambda x: x ** 2, parzyste))
print(kwadraty_parzystych)
# Wynik: [4, 16, 36]
```

Jak widać, funkcyjne podejścia pozwalają na zwięzłe i deklaratywne wyrażenie zamierzonej logiki.

#### 7.2. Przykład: Tworzenie listy nazw produktów z cenami powyżej 20 zł

**Tradycyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 16.5},
    {"nazwa": "Produkt B", "cena": 27.5},
    {"nazwa": "Produkt C", "cena": 22.0},
    {"nazwa": "Produkt D", "cena": 19.0}
]

nazwy_drogich = []
for p in produkty:
    if p["cena"] > 20:
        nazwy_drogich.append(p["nazwa"])

print(nazwy_drogich)
# Wynik: ['Produkt B', 'Produkt C']
```

**Funkcyjny sposób z użyciem list comprehensions:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 16.5},
    {"nazwa": "Produkt B", "cena": 27.5},
    {"nazwa": "Produkt C", "cena": 22.0},
    {"nazwa": "Produkt D", "cena": 19.0}
]

nazwy_drogich = [p["nazwa"] for p in produkty if p["cena"] > 20]
print(nazwy_drogich)
# Wynik: ['Produkt B', 'Produkt C']
```

**Funkcyjny sposób z użyciem `filter` i `map`:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 16.5},
    {"nazwa": "Produkt B", "cena": 27.5},
    {"nazwa": "Produkt C", "cena": 22.0},
    {"nazwa": "Produkt D", "cena": 19.0}
]

drogie_produkty = filter(lambda p: p["cena"] > 20, produkty)
nazwy_drogich = list(map(lambda p: p["nazwa"], drogie_produkty))
print(nazwy_drogich)
# Wynik: ['Produkt B', 'Produkt C']
```

---
    
### 8. Praktyka: Przetwarzanie danych z wykorzystaniem `lambda`, `map`, `filter` oraz comprehensions

W tej części przećwiczymy stworzenie skryptów, które będą wykorzystywać poznane techniki do przetwarzania danych. Przykładowo, stworzymy skrypt, który pobiera dane o produktach, przetwarza je, filtruje i wyświetla wyniki.

#### 8.1. Zadanie 1: Podniesienie cen produktów i filtrowanie

**Opis:**

Mamy listę produktów z nazwami i cenami. Chcemy podnieść cenę każdego produktu o 15%, a następnie wyfiltrować tylko te produkty, których cena przekracza 25 zł.

**Tradycyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 20},
    {"nazwa": "Produkt B", "cena": 25},
    {"nazwa": "Produkt C", "cena": 30},
    {"nazwa": "Produkt D", "cena": 15}
]

# Podniesienie cen
for p in produkty:
    p["cena"] *= 1.15

# Filtrowanie
drogie_produkty = []
for p in produkty:
    if p["cena"] > 25:
        drogie_produkty.append(p)

print(drogie_produkty)
# Wynik: [{'nazwa': 'Produkt B', 'cena': 28.75}, {'nazwa': 'Produkt C', 'cena': 34.5}]
```

**Funkcyjny sposób z użyciem comprehensions:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 20},
    {"nazwa": "Produkt B", "cena": 25},
    {"nazwa": "Produkt C", "cena": 30},
    {"nazwa": "Produkt D", "cena": 15}
]

# Podniesienie cen i filtrowanie
drogie_produkty = [
    {"nazwa": p["nazwa"], "cena": p["cena"] * 1.15}
    for p in produkty
    if p["cena"] * 1.15 > 25
]

print(drogie_produkty)
# Wynik: [{'nazwa': 'Produkt B', 'cena': 28.75}, {'nazwa': 'Produkt C', 'cena': 34.5}]
```

**Funkcyjny sposób z użyciem `map` i `filter`:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 20},
    {"nazwa": "Produkt B", "cena": 25},
    {"nazwa": "Produkt C", "cena": 30},
    {"nazwa": "Produkt D", "cena": 15}
]

# Podniesienie cen
podniesione = map(lambda p: {"nazwa": p["nazwa"], "cena": p["cena"] * 1.15}, produkty)

# Filtrowanie
drogie_produkty = list(filter(lambda p: p["cena"] > 25, podniesione))

print(drogie_produkty)
# Wynik: [{'nazwa': 'Produkt B', 'cena': 28.75}, {'nazwa': 'Produkt C', 'cena': 34.5}]
```

#### 8.2. Zadanie 2: Tworzenie słownika z nazwami produktów i ich cenami podniesionymi o 20%

**Opis:**

Mamy listę produktów, a chcemy stworzyć słownik, w którym kluczami będą nazwy produktów, a wartościami ich ceny podniesione o 20%.

**Tradycyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 50},
    {"nazwa": "Produkt B", "cena": 75},
    {"nazwa": "Produkt C", "cena": 100}
]

slownik_cen = {}
for p in produkty:
    slownik_cen[p["nazwa"]] = p["cena"] * 1.2

print(slownik_cen)
# Wynik: {'Produkt A': 60.0, 'Produkt B': 90.0, 'Produkt C': 120.0}
```

**Funkcyjny sposób z użyciem dict comprehensions:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 50},
    {"nazwa": "Produkt B", "cena": 75},
    {"nazwa": "Produkt C", "cena": 100}
]

slownik_cen = {p["nazwa"]: p["cena"] * 1.2 for p in produkty}
print(slownik_cen)
# Wynik: {'Produkt A': 60.0, 'Produkt B': 90.0, 'Produkt C': 120.0}
```

**Funkcyjny sposób z użyciem `map`:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 50},
    {"nazwa": "Produkt B", "cena": 75},
    {"nazwa": "Produkt C", "cena": 100}
]

slownik_cen = dict(map(lambda p: (p["nazwa"], p["cena"] * 1.2), produkty))
print(slownik_cen)
# Wynik: {'Produkt A': 60.0, 'Produkt B': 90.0, 'Produkt C': 120.0}
```

#### 8.3. Zadanie 3: Obliczanie średniej ceny produktów

**Opis:**

Chcemy obliczyć średnią cenę produktów w liście.

**Tradycyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 60.0},
    {"nazwa": "Produkt B", "cena": 90.0},
    {"nazwa": "Produkt C", "cena": 120.0}
]

suma = 0
for p in produkty:
    suma += p["cena"]
srednia = suma / len(produkty)
print(f"Średnia cena produktów: {srednia:.2f} zł")
# Wynik: Średnia cena produktów: 90.00 zł
```

**Funkcyjny sposób z użyciem `map` i `reduce`:**

```python
from functools import reduce

produkty = [
    {"nazwa": "Produkt A", "cena": 60.0},
    {"nazwa": "Produkt B", "cena": 90.0},
    {"nazwa": "Produkt C", "cena": 120.0}
]

ceny = list(map(lambda p: p["cena"], produkty))
suma = reduce(lambda a, b: a + b, ceny, 0)
srednia = suma / len(ceny)
print(f"Średnia cena produktów: {srednia:.2f} zł")
# Wynik: Średnia cena produktów: 90.00 zł
```

**Funkcyjny sposób z użyciem `sum` i generator expressions:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 60.0},
    {"nazwa": "Produkt B", "cena": 90.0},
    {"nazwa": "Produkt C", "cena": 120.0}
]

suma = sum(p["cena"] for p in produkty)
srednia = suma / len(produkty)
print(f"Średnia cena produktów: {srednia:.2f} zł")
# Wynik: Średnia cena produktów: 90.00 zł
```

Warto zauważyć, że użycie generator expressions wraz z wbudowaną funkcją `sum` jest najbardziej czytelnym i efektywnym sposobem w tym przypadku.

---
    
### 9. Praktyka: Skrócenie kodu względem tradycyjnych pętli

W tej sekcji zobaczymy, jak przekształcić tradycyjny kod z pętlami na bardziej zwięzły i deklaratywny kod funkcyjny, wykorzystując `lambda`, `map`, `filter` oraz comprehensions.

#### 9.1. Zadanie 4: Tworzenie listy długości nazw produktów

**Opis:**

Mamy listę produktów, a każdy produkt ma nazwę. Chcemy stworzyć listę zawierającą długości tych nazw.

**Tradycyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A"},
    {"nazwa": "Produkt B"},
    {"nazwa": "Produkt C"},
    {"nazwa": "Produkt D"}
]

dlugosci = []
for p in produkty:
    dlugosci.append(len(p["nazwa"]))

print(dlugosci)
# Wynik: [9, 9, 9, 9]
```

**Funkcyjny sposób z użyciem `map`:**

```python
produkty = [
    {"nazwa": "Produkt A"},
    {"nazwa": "Produkt B"},
    {"nazwa": "Produkt C"},
    {"nazwa": "Produkt D"}
]

dlugosci = list(map(lambda p: len(p["nazwa"]), produkty))
print(dlugosci)
# Wynik: [9, 9, 9, 9]
```

**Funkcyjny sposób z użyciem list comprehensions:**

```python
produkty = [
    {"nazwa": "Produkt A"},
    {"nazwa": "Produkt B"},
    {"nazwa": "Produkt C"},
    {"nazwa": "Produkt D"}
]

dlugosci = [len(p["nazwa"]) for p in produkty]
print(dlugosci)
# Wynik: [9, 9, 9, 9]
```

#### 9.2. Zadanie 5: Tworzenie listy nazw produktów w formacie wielkich liter

**Opis:**

Chcemy stworzyć listę nazw produktów, przekształconych na wielkie litery.

**Tradycyjny sposób:**

```python
produkty = [
    {"nazwa": "produkt a"},
    {"nazwa": "produkt b"},
    {"nazwa": "produkt c"},
    {"nazwa": "produkt d"}
]

nazwy_wielkie = []
for p in produkty:
    nazwy_wielkie.append(p["nazwa"].upper())

print(nazwy_wielkie)
# Wynik: ['PRODUKT A', 'PRODUKT B', 'PRODUKT C', 'PRODUKT D']
```

**Funkcyjny sposób z użyciem `map` i `lambda`:**

```python
produkty = [
    {"nazwa": "produkt a"},
    {"nazwa": "produkt b"},
    {"nazwa": "produkt c"},
    {"nazwa": "produkt d"}
]

nazwy_wielkie = list(map(lambda p: p["nazwa"].upper(), produkty))
print(nazwy_wielkie)
# Wynik: ['PRODUKT A', 'PRODUKT B', 'PRODUKT C', 'PRODUKT D']
```

**Funkcyjny sposób z użyciem list comprehensions:**

```python
produkty = [
    {"nazwa": "produkt a"},
    {"nazwa": "produkt b"},
    {"nazwa": "produkt c"},
    {"nazwa": "produkt d"}
]

nazwy_wielkie = [p["nazwa"].upper() for p in produkty]
print(nazwy_wielkie)
# Wynik: ['PRODUKT A', 'PRODUKT B', 'PRODUKT C', 'PRODUKT D']
```

---
    
### 10. Praktyka: Implementacja i zarządzanie listą produktów

W tej części stworzymy prosty system zarządzania listą produktów, wykorzystując programowanie funkcyjne do przetwarzania danych. Stworzymy funkcje do dodawania produktów, filtrowania, sortowania i obliczania statystyk.

#### 10.1. Definicja funkcji pomocniczych

```python
from functools import reduce

# Funkcja do dodawania procentu do ceny
def dodaj_procent(p, procent):
    p["cena"] *= (1 + procent / 100)
    return p

# Funkcja do filtrowania produktów po minimalnej cenie
def filtruj_po_cenie(p, min_cena):
    return p["cena"] > min_cena

# Funkcja do obliczania łącznej wartości produktów
def suma_cen(produkty):
    return reduce(lambda acc, p: acc + p["cena"], produkty, 0)
```

#### 10.2. Zarządzanie listą produktów

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 20},
    {"nazwa": "Produkt B", "cena": 35},
    {"nazwa": "Produkt C", "cena": 15},
    {"nazwa": "Produkt D", "cena": 40}
]

# Podniesienie cen o 10%
podniesione = list(map(lambda p: dodaj_procent(p, 10), produkty))

# Filtrowanie produktów droższych niż 25 zł
drogie_produkty = list(filter(lambda p: filtruj_po_cenie(p, 25), podniesione))

# Obliczanie łącznej wartości drogich produktów
suma = suma_cen(drogie_produkty)

print("Drogie produkty:", drogie_produkty)
print(f"Łączna wartość drogich produktów: {suma:.2f} zł")
```

**Wynik:**

```
Drogie produkty: [{'nazwa': 'Produkt B', 'cena': 38.5}, {'nazwa': 'Produkt D', 'cena': 44.0}]
Łączna wartość drogich produktów: 82.50 zł
```

#### 10.3. Alternatywny sposób z użyciem comprehensions

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 20},
    {"nazwa": "Produkt B", "cena": 35},
    {"nazwa": "Produkt C", "cena": 15},
    {"nazwa": "Produkt D", "cena": 40}
]

# Podniesienie cen o 10%
podniesione = [{"nazwa": p["nazwa"], "cena": p["cena"] * 1.1} for p in produkty]

# Filtrowanie produktów droższych niż 25 zł
drogie_produkty = [p for p in podniesione if p["cena"] > 25]

# Obliczanie łącznej wartości drogich produktów
suma = sum(p["cena"] for p in drogie_produkty)

print("Drogie produkty:", drogie_produkty)
print(f"Łączna wartość drogich produktów: {suma:.2f} zł")
```

**Wynik:**

```
Drogie produkty: [{'nazwa': 'Produkt B', 'cena': 38.5}, {'nazwa': 'Produkt D', 'cena': 44.0}]
Łączna wartość drogich produktów: 82.50 zł
```

---
    
### 11. Praktyka: Tworzenie prostego parsera danych

W tej części stworzymy skrypt, który pobiera dane z pliku tekstowego, przetwarza je, a następnie zapisuje wyniki do nowego pliku. Wykorzystamy funkcje `lambda`, `map`, `filter` oraz list comprehensions do przetwarzania danych.

#### 11.1. Założenia

Mamy plik `produkty.txt` z danymi produktów w formacie:

```
Produkt A;20
Produkt B;35
Produkt C;15
Produkt D;40
Produkt E;25
```

Chcemy:

1. Odczytać dane z pliku.
2. Podnieść cenę każdego produktu o 10%.
3. Filtrować tylko te produkty, których cena po podniesieniu przekracza 25 zł.
4. Zapisz przetworzone dane do nowego pliku `drogie_produkty.txt`.

#### 11.2. Implementacja

**Skrypt:**

```python
# przetwarzanie_produktow.py

def odczytaj_produkty(nazwa_pliku):
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        linie = plik.readlines()
    produkty = [line.strip().split(";") for line in linie if line.strip()]
    return [{"nazwa": p[0], "cena": float(p[1])} for p in produkty]

def podnies_ceny(produkty, procent):
    return list(map(lambda p: {"nazwa": p["nazwa"], "cena": p["cena"] * (1 + procent / 100)}, produkty))

def filtruj_produkty(produkty, min_cena):
    return list(filter(lambda p: p["cena"] > min_cena, produkty))

def zapisz_produkty(produkty, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        for p in produkty:
            plik.write(f"{p['nazwa']};{p['cena']:.2f}\n")

def main():
    input_file = "produkty.txt"
    output_file = "drogie_produkty.txt"
    
    # Odczyt danych
    produkty = odczytaj_produkty(input_file)
    
    # Podniesienie cen o 10%
    produkty_podniesione = podnies_ceny(produkty, 10)
    
    # Filtrowanie produktów droższych niż 25 zł
    drogie_produkty = filtruj_produkty(produkty_podniesione, 25)
    
    # Zapis wyników
    zapisz_produkty(drogie_produkty, output_file)
    
    print(f"Przetworzone dane zapisano w pliku {output_file}")

if __name__ == "__main__":
    main()
```

**Wynik:**

Po uruchomieniu skryptu, plik `drogie_produkty.txt` będzie zawierał:

```
Produkt B;38.50
Produkt D;44.00
Produkt E;27.50
```

#### 11.3. Alternatywna implementacja z użyciem comprehensions

**Skrypt:**

```python
# przetwarzanie_produktow_comprehensions.py

def odczytaj_produkty(nazwa_pliku):
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        produkty = [
            {"nazwa": line.split(";")[0], "cena": float(line.split(";")[1])}
            for line in plik
            if line.strip()
        ]
    return produkty

def main():
    input_file = "produkty.txt"
    output_file = "drogie_produkty.txt"
    
    # Odczyt danych
    produkty = odczytaj_produkty(input_file)
    
    # Podniesienie cen o 10% i filtrowanie
    drogie_produkty = [
        {"nazwa": p["nazwa"], "cena": p["cena"] * 1.1}
        for p in produkty
        if p["cena"] * 1.1 > 25
    ]
    
    # Zapis wyników
    with open(output_file, "w", encoding="utf-8") as plik:
        for p in drogie_produkty:
            plik.write(f"{p['nazwa']};{p['cena']:.2f}\n")
    
    print(f"Przetworzone dane zapisano w pliku {output_file}")

if __name__ == "__main__":
    main()
```

**Wynik:**

Plik `drogie_produkty.txt` będzie zawierał te same dane co w poprzednim przykładzie.

---
    
### 10.4. Zadanie 6: Tworzenie listy produktów z rabatem

**Opis:**

Mamy listę produktów, a każdy produkt ma nazwę i cenę. Chcemy stworzyć nową listę produktów, w której każdemu produktowi zostanie przyznany rabat w wysokości 20%.

**Tradycyjny sposób:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 50},
    {"nazwa": "Produkt B", "cena": 80},
    {"nazwa": "Produkt C", "cena": 120}
]

produkty_z_rabatem = []
for p in produkty:
    p_z_rabatem = {"nazwa": p["nazwa"], "cena": p["cena"] * 0.8}
    produkty_z_rabatem.append(p_z_rabatem)

print(produkty_z_rabatem)
# Wynik: [{'nazwa': 'Produkt A', 'cena': 40.0}, {'nazwa': 'Produkt B', 'cena': 64.0}, {'nazwa': 'Produkt C', 'cena': 96.0}]
```

**Funkcyjny sposób z użyciem `map` i `lambda`:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 50},
    {"nazwa": "Produkt B", "cena": 80},
    {"nazwa": "Produkt C", "cena": 120}
]

produkty_z_rabatem = list(map(lambda p: {"nazwa": p["nazwa"], "cena": p["cena"] * 0.8}, produkty))
print(produkty_z_rabatem)
# Wynik: [{'nazwa': 'Produkt A', 'cena': 40.0}, {'nazwa': 'Produkt B', 'cena': 64.0}, {'nazwa': 'Produkt C', 'cena': 96.0}]
```

**Funkcyjny sposób z użyciem list comprehensions:**

```python
produkty = [
    {"nazwa": "Produkt A", "cena": 50},
    {"nazwa": "Produkt B", "cena": 80},
    {"nazwa": "Produkt C", "cena": 120}
]

produkty_z_rabatem = [{"nazwa": p["nazwa"], "cena": p["cena"] * 0.8} for p in produkty]
print(produkty_z_rabatem)
# Wynik: [{'nazwa': 'Produkt A', 'cena': 40.0}, {'nazwa': 'Produkt B', 'cena': 64.0}, {'nazwa': 'Produkt C', 'cena': 96.0}]
```

---
    
### 12. Podsumowanie i dalsze kroki

W tym rozdziale zgłębiliśmy podstawy programowania funkcyjnego w Pythonie, poznając funkcje anonimowe (`lambda`), wbudowane funkcje `map`, `filter`, `reduce`, a także wyrażenia listowe (`list comprehensions`) i słownikowe (`dict comprehensions`). Zobaczyliśmy, jak te narzędzia umożliwiają zwięzłe i czytelne przetwarzanie danych, porównując je z tradycyjnymi pętlami.

Kluczowe punkty:

- **Funkcje `lambda`** pozwalają na definiowanie małych, jednowierszowych funkcji bez konieczności ich pełnego definiowania.
- **Funkcje `map`, `filter`, `reduce`** umożliwiają stosowanie funkcji do elementów iterowalnych, filtrowanie oraz agregację danych w sposób deklaratywny.
- **List i dict comprehensions** to potężne narzędzia do tworzenia nowych struktur danych na podstawie istniejących, z możliwością dodawania warunków i transformacji.
- **Programowanie funkcyjne** w Pythonie pozwala na pisanie bardziej zwięzłego, czytelnego i efektywnego kodu, szczególnie w kontekście przetwarzania danych.

Dzięki tym umiejętnościom możesz efektywnie manipulować danymi, tworzyć złożone transformacje i utrzymywać wysoki poziom czytelności swojego kodu. W miarę zdobywania doświadczenia warto eksperymentować z różnymi technikami, porównując je z tradycyjnymi metodami, aby znaleźć najbardziej optymalne rozwiązania dla swoich problemów programistycznych.

**Dalsze kroki:**

- **Praktyka:** Kontynuuj tworzenie i modyfikowanie skryptów, stosując poznane techniki. Próby implementacji własnych projektów pomogą utrwalić wiedzę.
- **Rozszerzenie wiedzy:** Poznaj bardziej zaawansowane aspekty programowania funkcyjnego, takie jak funkcje wyższego rzędu, funkcje rekurencyjne czy dekoratory.
- **Integracja z innymi paradygmatami:** Zobacz, jak programowanie funkcyjne współgra z innymi paradygmatami w Pythonie, takimi jak obiektowość, co pozwala na tworzenie jeszcze bardziej elastycznego i modularnego kodu.
- **Eksperymentowanie:** Używaj różnych narzędzi i bibliotek, które wspierają programowanie funkcyjne, takich jak `itertools`, `functools`, czy biblioteki zewnętrzne jak `toolz` czy `fn`.

Opanowanie programowania funkcyjnego w Pythonie zwiększy Twoją efektywność jako programisty, umożliwiając tworzenie bardziej zwięzłych, czytelnych i skalowalnych aplikacji.

----

© 2024 Marian Witkowski
