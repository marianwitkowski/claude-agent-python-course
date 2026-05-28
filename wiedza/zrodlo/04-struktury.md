## Blok 4: Struktury danych w Pythonie

Poniższy rozdział wprowadzi Cię w świat najbardziej podstawowych i zarazem bardzo potężnych narzędzi w Pythonie – **struktur danych**. Dowiesz się, jak gromadzić i organizować dane w listach, krotkach, słownikach i zbiorach. Poznasz podstawowe operacje na tych kolekcjach: dodawanie i usuwanie elementów, sortowanie, filtrowanie, a także nauczysz się tworzyć bardziej złożone struktury dzięki zagnieżdżaniu różnych typów. Na koniec utrwalisz wiedzę, realizując przykłady praktyczne, takie jak stworzenie prostego rejestru (książki adresowej) czy filtrowanie i sortowanie zbiorów danych.

---

### 1. Wprowadzenie do struktur danych

Struktury danych to sposoby na organizowanie i przechowywanie informacji w programie, tak aby ułatwić dostęp, modyfikacje i analizę. Wyobraź sobie, że masz do przetworzenia listę produktów, książkę adresową, tablicę wyników sportowych lub rejestr studentów. Zamiast przechowywać każdy element w osobnej zmiennej, możesz zgromadzić je wewnątrz jednej, logicznej struktury. Python udostępnia kilka wbudowanych typów, które są niezwykle wydajne i elastyczne, co pozwala stosunkowo łatwo operować na nawet dużych zbiorach danych.

W tym rozdziale poznamy cztery podstawowe typy kolekcji:

- **Lista (list)**  
- **Krotka (tuple)**  
- **Słownik (dict)**  
- **Zbiór (set)**

Każda z nich ma swoje charakterystyczne cechy oraz typowe zastosowania. Zrozumienie różnic i możliwości każdej struktury jest kluczem do efektywnego pisania kodu w Pythonie.

---

### 2. Listy – dynamiczne sekwencje danych

**Listy** to jedna z najczęściej używanych struktur danych w Pythonie. Można traktować je jako dynamiczne tablice o zmiennym rozmiarze. Listy:

- Pozwalają przechowywać wiele elementów (dowolnego typu) w jednej zmiennej.
- Można je modyfikować: dodawać, usuwać, zamieniać elementy, co czyni je bardzo elastycznymi.
- Ich elementy są uporządkowane i indeksowane począwszy od 0.

Przykładowa lista:

```python
produkty = ["mleko", "chleb", "jajka", "masło"]
print(produkty[0])   # "mleko"
print(produkty[2])   # "jajka"
```

Podstawowe operacje na listach:

- Dodawanie elementu na koniec: `produkty.append("ser")`
- Wstawianie elementu na konkretnej pozycji: `produkty.insert(1, "woda")`
- Usuwanie elementu po wartości: `produkty.remove("chleb")`
- Usuwanie elementu po indeksie: `del produkty[0]` lub `produkty.pop(0)`
- Sprawdzanie długości listy: `len(produkty)`

Możemy także wycinać fragmenty listy, korzystając z tzw. **slicing**:

```python
fruits = ["jabłko", "banan", "gruszka", "winogrono", "ananas"]
wycinek = fruits[1:4]  # ["banan", "gruszka", "winogrono"]
```

Slicing pozwala pobierać podlisty, zmieniać fragmenty list i efektywnie operować na ich częściach.

---

### 3. Krotki – niezmienialne sekwencje danych

**Krotki (tuple)** są podobne do list, ale posiadają jedną kluczową różnicę – są niezmienialne (immutable). Po utworzeniu krotki nie można zmienić żadnego z jej elementów. Nadają się świetnie do przechowywania danych, które nie powinny ulec modyfikacji w trakcie działania programu, zapewniając większe bezpieczeństwo i czasem lepszą wydajność.

Przykład krotki:

```python
dane_osoby = ("Jan", "Kowalski", 30)
print(dane_osoby[0])  # "Jan"
# dane_osoby[0] = "Adam"  # to spowoduje błąd, bo krotka jest niezmienialna
```

Choć nie możemy zmienić istniejącej krotki, nic nie stoi na przeszkodzie, aby tworzyć nowe krotki na bazie starych, łączyć je lub pobierać z nich fragmenty (slicing działa jak w listach):

```python
imiona = ("Ala", "Ola", "Ela")
imiona2 = imiona + ("Iza",)  # imiona2 = ("Ala", "Ola", "Ela", "Iza")
```

Krotki są często używane do przekazywania stałych zestawów danych, np. współrzędnych punktu (x, y), ustawień konfiguracyjnych lub wyników funkcji zwracającej wiele wartości.

---

### 4. Słowniki – dane w formie klucz-wartość

**Słowniki (dict)** to struktury danych, które pozwalają przechowywać pary klucz-wartość. W przeciwieństwie do list, nie mają ustalonego porządku indeksów numerycznych – zamiast tego każdy element jest dostępny przez klucz, który może być np. napisem, liczbą czy krotką.

Przykład słownika:

```python
osoba = {
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "wiek": 30
}

print(osoba["imie"])     # "Jan"
osoba["miasto"] = "Warszawa"  # dodawanie nowej pary klucz-wartość
```

Operacje na słowniku:

- Dodawanie/zmiana wartości: `osoba["wiek"] = 31`
- Usuwanie klucza: `del osoba["nazwisko"]`
- Pobieranie wartości z kontrolą błędów: `osoba.get("tel", "Brak danych")`
- Iteracja po kluczach: `for klucz in osoba: print(klucz, osoba[klucz])`
- Pobranie listy kluczy: `osoba.keys()`
- Pobranie listy wartości: `osoba.values()`
- Pobranie par klucz-wartość: `osoba.items()`

Słowniki są niezwykle elastyczne i świetnie nadają się do przechowywania danych w sposób bardziej opisowy niż same listy.

---

### 5. Zbiory (sets) – unikalne elementy bez określonego porządku

**Zbiory (set)** to struktury danych przechowujące unikalne elementy, bez powtórzeń i bez gwarancji jakiegokolwiek porządku. Są przydatne, kiedy chcemy szybko sprawdzić, czy dany element występuje w kolekcji, lub kiedy potrzebujemy przeprowadzić typowe operacje znane z matematyki na zbiorach: sumę, przecięcie czy różnicę.

Przykład zbioru:

```python
literki = {"a", "b", "c", "a"}
print(literki)  # {"a", "b", "c"} - duplikat "a" został usunięty
```

Operacje na zbiorach:

- Dodawanie elementu: `literki.add("d")`
- Usuwanie elementu: `literki.remove("b")` (jeśli nie ma "b", błąd) lub `literki.discard("b")` (bez błędu)
- Suma zbiorów: `zbior1 | zbior2`
- Przecięcie zbiorów: `zbior1 & zbior2`
- Różnica zbiorów: `zbior1 - zbior2`

Dzięki zbiorom szybko sprawdzisz, czy element jest w danym zestawie (operacja `x in zbior` jest bardzo efektywna), a także przeprowadzisz operacje porównywalne z działaniami na matematycznych zbiorach.

---

### 6. Operacje na kolekcjach: sortowanie, filtrowanie

Często wymagane jest uporządkowanie lub przefiltrowanie danych. W Pythonie mamy do tego świetne narzędzia.  

**Sortowanie:**

Listy można sortować za pomocą metody `sort()` (sortuje na miejscu) lub funkcji `sorted()` (zwraca nową listę):

```python
liczby = [5, 1, 4, 2, 3]
liczby.sort()
print(liczby)  # [1, 2, 3, 4, 5]

imiona = ["Ala", "Ola", "Ela"]
posortowane = sorted(imiona)
print(posortowane)  # ["Ala", "Ela", "Ola"]
```

Sortować możemy również słowniki (np. po kluczach) lub zbioru zamieniając je najpierw na listę.

**Filtrowanie:**

Możemy wykorzystać pętle i instrukcje warunkowe:

```python
liczby = [10, 5, 8, 12, 3]
wynik = []
for l in liczby:
    if l > 5:
        wynik.append(l)
print(wynik)  # [10, 8, 12]
```

Python udostępnia także wyrażenia listowe (list comprehensions) ułatwiające filtrację:

```python
wynik = [l for l in liczby if l > 5]
```

List comprehensions oraz podobne konstrukcje dla zbiorów, słowników pozwalają w jednym, czytelnym wyrażeniu tworzyć nowe kolekcje na podstawie istniejących, filtrując, modyfikując czy przekształcając elementy.

---

### 7. Zagnieżdżone struktury danych

Struktury danych w Pythonie można łatwo zagnieżdżać, tworząc w ten sposób bardziej złożone i hierarchiczne układy. Na przykład, możemy mieć listę słowników, gdzie każdy słownik reprezentuje jedną osobę, lub słownik, w którym wartościami są listy:

```python
ksiazka_adresowa = [
    {"imie": "Jan", "nazwisko": "Kowalski", "tel": "123456789"},
    {"imie": "Ala", "nazwisko": "Nowak", "tel": "987654321"}
]

# Dostęp do numeru telefonu drugiej osoby:
print(ksiazka_adresowa[1]["tel"])  # "987654321"
```

Innym przykładem jest słownik, który mapuje kategorie produktów do list tych produktów:

```python
produkty_sklep = {
    "warzywa": ["marchewka", "ziemniak", "pomidor"],
    "owoce": ["jabłko", "banan", "ananas"],
    "nabiał": ["mleko", "jogurt", "masło"]
}
```

Dzięki zagnieżdżaniu możemy reprezentować w Pythonie złożone dane w bardzo naturalny sposób, np. hierarchiczne struktury organizacyjne, ustawienia zagnieżdżone w sekcjach, czy dane JSON pochodzące z API.

---

### 8. Praktyka: Tworzenie prostego rejestru (książki adresowej)

Skorzystajmy z poznanych struktur danych i operacji, aby stworzyć prosty rejestr kontaktów (książkę adresową). Będziemy przechowywać listę słowników, gdzie każdy słownik zawiera informacje o jednej osobie.

Przykładowy kod:

```python
ksiazka = []

# Dodawanie kontaktów
ksiazka.append({"imie": "Jan", "nazwisko": "Kowalski", "tel": "123456789"})
ksiazka.append({"imie": "Ala", "nazwisko": "Nowak", "tel": "987654321"})
ksiazka.append({"imie": "Tomasz", "nazwisko": "Zawadzki", "tel": "555555555"})

# Wyszukanie kontaktu po nazwisku
szukane_nazwisko = "Nowak"
for kontakt in ksiazka:
    if kontakt["nazwisko"] == szukane_nazwisko:
        print(f"Znaleziono kontakt: {kontakt}")
        break
else:
    print("Nie znaleziono kontaktu o podanym nazwisku.")

# Usuwanie kontaktu
do_usuniecia = "Zawadzki"
ksiazka = [k for k in ksiazka if k["nazwisko"] != do_usuniecia]

print("Aktualna książka adresowa:", ksiazka)
```

W powyższym przykładzie:

- Tworzymy listę słowników, z których każdy reprezentuje jeden wpis w książce adresowej.
- Iterujemy po liście, aby wyszukać kontakt według nazwiska.
- Usuwamy kontakt, korzystając z filtrowania przy pomocy wyrażenia listowego.

W ten sposób pokazujemy, jak łączyć wiedzę o pętlach, warunkach i strukturach danych w celu stworzenia prostego, ale praktycznego narzędzia.

---

### 9. Praktyka: Filtrowanie i sortowanie danych

Załóżmy, że mamy listę słowników, z których każdy opisuje produkt ze sklepu: zawiera jego nazwę i cenę. Chcemy utworzyć nową listę zawierającą tylko te produkty, których cena przekracza pewien próg, a następnie posortować ją według ceny.

```python
produkty = [
    {"nazwa": "mleko", "cena": 3.20},
    {"nazwa": "chleb", "cena": 2.50},
    {"nazwa": "jajka", "cena": 5.00},
    {"nazwa": "masło", "cena": 4.50},
]

# Filtrowanie - produkty droższe niż 3 zł
drogi_asortyment = [p for p in produkty if p["cena"] > 3.00]

# Sortowanie produktów po cenie
drogi_asortyment.sort(key=lambda p: p["cena"])

print("Drogie produkty (posortowane rosnąco po cenie):")
for p in drogi_asortyment:
    print(f"{p['nazwa']}: {p['cena']} zł")
```

Co się tu dzieje?

- Tworzymy nową listę `drogi_asortyment` zawierającą tylko te słowniki, dla których cena przekracza 3 zł.
- Sortujemy tę listę, podając jako klucz sortujący (`key`) funkcję anonimową (lambda), która zwraca cenę produktu.
- Wyświetlamy wynik.

Dzięki temu łączymy kilka ważnych elementów: struktury danych (listy i słowniki), wyrażenia listowe do filtrowania oraz metodę `sort()` z kluczem do porządkowania wyników.

---

### 10. Podsumowanie i dalsze kroki

W tym rozdziale nauczyłeś się:

- Czym są i jak działają podstawowe wbudowane struktury danych w Pythonie: listy, krotki, słowniki i zbiory.
- Jak dodawać, usuwać, modyfikować elementy, a także jak filtrować i sortować kolekcje.
- Jak tworzyć bardziej złożone, zagnieżdżone struktury, dzięki którym możesz reprezentować złożone dane w prosty i przejrzysty sposób.
- Jak wykorzystać zdobytą wiedzę w praktycznych przykładach, takich jak tworzenie książki adresowej czy filtrowanie i sortowanie produktów.

Opanowanie tych zagadnień jest kluczowe, ponieważ struktury danych stanowią fundament większości operacji w programowaniu. Dobra znajomość dostępnych typów kolekcji i umiejętność doboru odpowiedniej struktury do konkretnego zadania to podstawa skutecznego i efektywnego tworzenia oprogramowania. W kolejnych blokach rozbudujemy tę wiedzę o funkcje, moduły i inne zaawansowane techniki, które umożliwią tworzenie złożonych, wielofunkcyjnych aplikacji. Eksperymentuj z różnymi strukturami, porównuj ich wydajność, ucz się korzystać z wbudowanych narzędzi do przetwarzania danych – to praktyka uczyni z Ciebie sprawnego i wydajnego programistę Pythona.

----

© 2024 Marian Witkowski
