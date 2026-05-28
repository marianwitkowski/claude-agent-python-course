## Blok 2: Podstawy języka Python – składnia i typy danych

Poniższy rozdział poświęcony jest podstawom języka Python – składni i typom danych, które stanowią fundament dalszej nauki. Zapoznamy się z ideą zmiennych, podstawowymi typami danych (liczbami całkowitymi i zmiennoprzecinkowymi, napisami oraz wartościami logicznymi), nauczymy się konwersji między typami, poznamy dostępne operatory arytmetyczne i priorytety działań, a także zobaczymy, jak korzystać z funkcji `print()` do wyświetlania informacji i jak formatować tekst z użyciem f-stringów. Na koniec przećwiczymy zdobytą wiedzę w praktycznych przykładach, które pomogą utrwalić poznane zagadnienia.

---

### 1. Wprowadzenie do składni Pythona

Python słynie z czytelnej i zwięzłej składni. Zamiast klamrowych nawiasów `{}` do wyznaczania bloków kodu (jak w C++ czy Javie), Python wykorzystuje wcięcia (zwykle 4 spacje) do grupowania instrukcji. Dzięki temu kod jest przejrzysty i łatwiejszy w utrzymaniu. Już od pierwszych linijek kodu w Pythonie zauważymy prostotę, która wpływa na większą zrozumiałość programów, zwłaszcza dla osób początkujących.

---

### 2. Zmienne i typy danych

**Zmienne** to nazwy, pod którymi przechowujemy dane. W Pythonie typ zmiennej jest określany dynamicznie w momencie przypisania wartości. Nie musimy deklarować typu jawnie – interpreter automatycznie rozpozna, czy mamy do czynienia z liczbą, łańcuchem znaków, czy innym obiektem. Przykładowo:

```python
x = 10         # zmienna typu int
tekst = "Ala"  # zmienna typu str
```

**Podstawowe typy danych w Pythonie:**

1. **int (liczby całkowite)** – np. `0`, `42`, `-5`.  
2. **float (liczby zmiennoprzecinkowe)** – np. `3.14`, `-0.5`, `2.0`.  
   Każda liczba z kropką dziesiętną jest traktowana jako float.  
3. **str (napisy)** – ciągi znaków ujęte w cudzysłowy, np. `"Hello"`, `'Python'`.  
4. **bool (wartości logiczne)** – przyjmują wartości `True` lub `False`.  
   Służą do sprawdzania warunków (czy dana wartość jest większa od zera, czy napis nie jest pusty itp.).

Przykłady przypisań:

```python
a = 5        # int
b = 3.14     # float
c = "Cześć"  # str
d = True     # bool
```

---

### 3. Konwersje typów

Często pojawia się potrzeba zmiany typu danych. Możemy zamienić tekst na liczbę, jeśli string zawiera cyfry, lub liczbę na tekst, aby wyświetlić ją w zdaniu.

- `int("10")` → 10 (string na int)  
- `float("3.14")` → 3.14 (string na float)  
- `str(42)` → "42" (int na string)  
- `bool(0)` → False, `bool(1)` → True

Przykłady:

```python
x_str = "123"
x_int = int(x_str)     # x_int = 123 (int)
tekst = str(3.14)      # tekst = "3.14"
stan = bool("Python")  # stan = True, bo niepusty łańcuch to True
```

Należy pamiętać, że nie każdy napis da się przekonwertować na liczbę:

```python
int("abc")  # spowoduje błąd ValueError
```

---

### 4. Operacje arytmetyczne i przypisanie

Python udostępnia różne operatory arytmetyczne:

- Dodawanie: `+`  
- Odejmowanie: `-`  
- Mnożenie: `*`  
- Dzielenie: `/` (wynik zawsze float)  
- Dzielenie całkowite: `//` (zaokrągla w dół)  
- Reszta z dzielenia (modulo): `%`  
- Potęgowanie: `**`

Przykłady:

```python
x = 10
y = 3

print(x + y)    # 13
print(x - y)    # 7
print(x * y)    # 30
print(x / y)    # 3.3333...
print(x // y)   # 3
print(x % y)    # 1 (reszta z dzielenia 10 przez 3)
print(x ** y)   # 10^3 = 1000
```

**Operator przypisania `=`** służy do nadawania zmiennym wartości, a operatorów można używać w formie skróconej:

```python
x = 5
x += 2   # x = x + 2 → x = 7
x *= 3   # x = x * 3 → x = 21
```

---

### 5. Priorytety operatorów

Podobnie jak w matematyce, pewne operacje mają wyższy priorytet wykonania niż inne. Kolejność jest zbliżona do standardowej notacji matematycznej:

1. `**` (potęgowanie)
2. `*`, `/`, `//`, `%`  
3. `+`, `-`

Jeżeli chcemy zmienić kolejność obliczeń, używamy nawiasów:

```python
wynik = 2 + 3 * 4     # Najpierw 3*4=12, potem 2+12=14
wynik2 = (2 + 3) * 4   # Najpierw 2+3=5, potem 5*4=20
```

---

### 6. Funkcja `print()` i formatowanie napisów (f-stringi)

Funkcja `print()` pozwala nam wyświetlić dane na ekranie:

```python
print("Hello World!")
print(42)
print("Wynik:", 3.14)
```

Aby elegancko wstawiać wartości zmiennych do tekstu, wykorzystujemy **f-stringi**. Wystarczy poprzedzić napis literą `f` i umieścić nazwę zmiennej w klamrach `{}`:

```python
name = "Jan"
age = 30
print(f"Nazywam się {name} i mam {age} lat.")
# Nazywam się Jan i mam 30 lat.
```

Możemy także formatować liczby:

```python
pi = 3.14159265
print(f"Liczba pi zaokrąglona do dwóch miejsc po przecinku: {pi:.2f}")
# Liczba pi zaokrąglona do dwóch miejsc po przecinku: 3.14
```

F-stringi są czytelne i wygodne, dzięki czemu szybko stały się standardowym sposobem formatowania tekstów w Pythonie.

---

### Praktyka

W tej sekcji utrwalisz poznane zagadnienia, pisząc proste skrypty wykonujące obliczenia i formatujące wyjście.

**Zadanie 1: Obliczenia podstawowe**  
Napisz skrypt, który:  
1. Przypisze do zmiennej `a` wartość całkowitą 15, a do zmiennej `b` wartość zmiennoprzecinkową 4.2.  
2. Obliczy ich sumę, różnicę, iloczyn i iloraz (zwykły i całkowity).  
3. Wyświetli wyniki na ekranie korzystając z `print()`.

Przykładowe rozwiązanie:

```python
a = 15
b = 4.2

suma = a + b
roznica = a - b
iloczyn = a * b
iloraz = a / b
iloraz_cal = a // b

print("Suma:", suma)
print("Różnica:", roznica)
print("Iloczyn:", iloczyn)
print("Iloraz:", iloraz)
print("Iloraz całkowity:", iloraz_cal)
```

**Zadanie 2: Konwersja typów i formatowanie**  
Załóżmy, że otrzymujesz dane o cenie produktu jako łańcuch znaków:  
```python
cena_str = "199.99"
```
Twoim zadaniem jest:  
1. Przekonwertować `cena_str` na typ float.  
2. Wyświetlić komunikat o treści:  
   ```
   Cena produktu wynosi: 199.99 zł
   ```
   używając f-stringa.

Przykładowe rozwiązanie:

```python
cena_str = "199.99"
cena = float(cena_str)
print(f"Cena produktu wynosi: {cena:.2f} zł")
```

**Zadanie 3: Łączenie tekstu i danych**  
Utwórz zmienne `imie = "Ala"` i `wiek = 10`. Następnie za pomocą f-stringa wyświetl komunikat:  
```
Cześć, mam na imię Ala i mam 10 lat.
```

Rozwiązanie:

```python
imie = "Ala"
wiek = 10
print(f"Cześć, mam na imię {imie} i mam {wiek} lat.")
```

---

### Podsumowanie

W tym rozdziale poznałeś:

- Koncepcję zmiennych i ich typowanie w Pythonie.
- Podstawowe typy danych: int, float, str, bool.
- Sposoby konwersji między typami danych.
- Operatory arytmetyczne i priorytety działań.
- Funkcję `print()` oraz formatowanie napisów za pomocą f-stringów.

Dzięki tym umiejętnościom możesz już tworzyć proste skrypty obliczeniowe, przetwarzać dane wejściowe i wyświetlać wyniki w czytelny sposób. W kolejnych rozdziałach zgłębimy instrukcje warunkowe, pętle oraz bardziej złożone struktury danych, które pozwolą budować coraz bardziej funkcjonalne programy.

----

© 2024 Marian Witkowski
