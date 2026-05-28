## Blok 5: Funkcje i modularność

Poniższy rozdział poświęcony jest jednemu z fundamentów dobrej praktyki programistycznej: funkcjom i modularności kodu. Funkcje pozwalają na efektywne organizowanie kodu, wielokrotne wykorzystanie tych samych fragmentów logiki oraz lepsze utrzymanie i rozszerzanie aplikacji. Poznasz zasady definiowania funkcji i zwracania z nich wartości, dowiesz się, jak działa mechanizm przekazywania argumentów, w tym argumentów domyślnych i nazwanych. Omówimy również, czym jest zakres zmiennych (lokalny vs globalny) oraz jak dzielić kod na mniejsze części, korzystając z modułów i importów. Na końcu przećwiczymy nowe umiejętności w praktyce.

---

### 1. Wprowadzenie do funkcji

Funkcja to wydzielony blok kodu, który wykonuje określone zadanie. Zazwyczaj funkcje przyjmują pewne dane wejściowe (argumenty), przetwarzają je i zwracają wynik. Podział programu na funkcje ułatwia jego czytelność, modyfikowalność i ponowne wykorzystanie fragmentów logiki bez konieczności pisania podobnych fragmentów kodu w wielu miejscach.

Zalety stosowania funkcji:

- **Czytelność:** Funkcje pozwalają na ukrycie złożoności. Zamiast czytać wiele linii kodu, aby zrozumieć, jak wykonywane jest dane zadanie, wystarczy zapoznać się z nazwą i dokumentacją funkcji.  
- **Ponowne wykorzystanie kodu:** Jeśli często powtarzasz podobne operacje (np. walidację danych), możesz zamknąć je w funkcji i wielokrotnie wywoływać.  
- **Utrzymanie i rozwój:** Łatwiej zlokalizować i poprawić błąd, jeśli jest zamknięty w funkcji. Łatwiej też rozbudować funkcjonalność, modyfikując lub dodając nowe funkcje.

---

### 2. Definiowanie funkcji i zwracanie wartości

Funkcje w Pythonie definiuje się za pomocą słowa kluczowego `def`, po którym następuje nazwa funkcji i lista argumentów w nawiasach, a następnie dwukropek. Wewnętrzny kod musi być wcięty. Aby zwrócić wartość z funkcji, używamy instrukcji `return`.

Przykład prostej funkcji:

```python
def dodaj(a, b):
    wynik = a + b
    return wynik
```

Powyższa funkcja `dodaj` przyjmuje dwa argumenty `a` i `b`, dodaje je, a następnie zwraca wynik. Po wywołaniu:

```python
suma = dodaj(3, 5)
print(suma)  # 8
```

Funkcja zwraca wartość 8, która trafia do zmiennej `suma`.

Jeśli funkcja nie użyje `return`, zwróci wartość `None` (brak wartości). Możemy jednak pisać funkcje, które nie zwracają rezultatu, a służą np. tylko do wyświetlania komunikatu lub modyfikowania danych "na zewnątrz".

---

### 3. Przekazywanie argumentów do funkcji

Funkcje mogą mieć zero, jeden lub wiele argumentów. Argumenty można przekazywać:

- Po pozycji, czyli w takiej kolejności, w jakiej występują w definicji funkcji.
- Po nazwie (argumenty nazwane), co pozwala na większą czytelność i elastyczność.

Przykładowo:

```python
def przedstaw_osobe(imie, wiek):
    print(f"Nazywam się {imie} i mam {wiek} lat.")

# wywołanie po pozycji
przedstaw_osobe("Jan", 30)

# wywołanie po nazwie
przedstaw_osobe(wiek=40, imie="Ala")
```

Pierwsze wywołanie przypisze `imie = "Jan"` i `wiek = 30` zgodnie z kolejnością. W drugim wywołaniu, dzięki użyciu nazw argumentów, kolejność nie ma znaczenia.

---

### 4. Argumenty domyślne

Możemy zdefiniować argumenty domyślne, które zostaną użyte, jeśli przy wywołaniu funkcji nie podamy wartości dla tego argumentu. Robimy to, przypisując wartość w definicji funkcji.

```python
def przedstaw_osobe(imie, wiek=18):
    print(f"Nazywam się {imie} i mam {wiek} lat.")

przedstaw_osobe("Jan")       # wiek = 18 (wartość domyślna)
przedstaw_osobe("Ala", 25)   # wiek = 25 (wartość podana)
```

Argumenty z wartościami domyślnymi muszą znajdować się na końcu listy argumentów, aby Python wiedział, które są opcjonalne.

---

### 5. Argumenty nazwane i ich zastosowania

Argumenty nazwane (keyword arguments) zwiększają czytelność kodu, zwłaszcza jeśli funkcja ma wiele argumentów o podobnym typie. Przykład:

```python
def zamowienie(produkt, ilosc, adres_dostawy):
    print(f"Produkt: {produkt}, ilość: {ilosc}, dostawa: {adres_dostawy}")

# Bez argumentów nazwanych
zamowienie("komputer", 2, "Warszawa")

# Z argumentami nazwanymi
zamowienie(produkt="komputer", ilosc=2, adres_dostawy="Warszawa")
```

Druga forma jest bardziej czytelna, bo od razu widzimy, które wartości przypisujemy do których parametrów.

---

### 6. Zakres zmiennych: lokalne vs globalne

Zmienne definiowane wewnątrz funkcji są domyślnie **lokalne** dla tej funkcji. Oznacza to, że nie są widoczne na zewnątrz, w innych częściach programu. Zmienne globalne to te, które są dostępne w całym programie, np. zdefiniowane poza funkcjami, w głównym zakresie (tzw. global scope).

Przykład:

```python
x = 10  # zmienna globalna

def pokaz_x():
    x = 5  # zmienna lokalna zasłaniająca globalną
    print("Wewnątrz funkcji x =", x)

pokaz_x()
print("Poza funkcją x =", x)
```

Wynikiem będzie:
```
Wewnątrz funkcji x = 5
Poza funkcją x = 10
```

We wnętrzu funkcji przypisanie `x = 5` stworzy lokalną zmienną `x`, nie modyfikując globalnej `x`.

Jeśli chcemy odwołać się do zmiennej globalnej wewnątrz funkcji, możemy użyć słowa kluczowego `global`:

```python
x = 10

def zmien_global_x():
    global x
    x = 20

zmien_global_x()
print(x)  # 20
```

Jednak stosowanie `global` jest zazwyczaj odradzane, ponieważ utrudnia zrozumienie i utrzymanie kodu. Lepiej przekazywać wartości jako argumenty i zwracać je z funkcji.

---

### 7. Modularność kodu

Modularność oznacza dzielenie kodu na mniejsze, logiczne części (moduły), które można łatwo ponownie wykorzystać, testować i utrzymywać. Zamiast pisać cały kod w jednym pliku, warto dzielić go na oddzielne moduły tematyczne. Python wspiera modularność poprzez pliki `.py` traktowane jako moduły.

Załóżmy, że mamy projekt o następującej strukturze:

```
projekt/
|-- main.py
|-- utils.py
```

Plik `utils.py` może zawierać funkcje pomocnicze, a `main.py` – główną logikę programu. Możemy wykorzystać funkcje z `utils.py` w `main.py` poprzez zaimportowanie modułu:

```python
# utils.py
def dodaj(a, b):
    return a + b

def przywitaj():
    print("Witaj w programie!")
```

```python
# main.py
import utils

utils.przywitaj()
wynik = utils.dodaj(2, 3)
print("Wynik dodawania:", wynik)
```

Po uruchomieniu `python main.py` zobaczymy:

```
Witaj w programie!
Wynik dodawania: 5
```

Dzięki temu kod jest podzielony na mniejsze części, co ułatwia pracę w zespole, testowanie i rozwijanie projektu.

---

### 8. Importowanie funkcji i modułów

Python oferuje różne sposoby importowania modułów i funkcji:

- `import nazwa_modulu` – importuje cały moduł. Funkcje wywołujemy jako `modul.funkcja()`.
- `from nazwa_modulu import funkcja` – importuje konkretną funkcję z modułu. Możemy wtedy wywoływać ją bez poprzedzania nazwą modułu.
- `from nazwa_modulu import funkcja as f` – importuje funkcję pod aliasem, co bywa przydatne, gdy nazwy są długie lub kolidują z innymi nazwami.
- `import nazwa_modulu as alias` – import modułu pod aliasem.

Przykłady:

```python
import utils
utils.przywitaj()

from utils import dodaj
print(dodaj(10, 20))

from utils import dodaj as d
print(d(5, 5))
```

Stosowanie aliasów może poprawić czytelność, jeśli nazwy są zbyt długie lub wielokrotnie używane.

---

### 9. Organizacja projektu w mniejsze moduły

Przy większych projektach warto dzielić kod na moduły według przeznaczenia. Przykładowa struktura może wyglądać tak:

```
projekt/
|-- main.py
|-- calculations.py
|-- io_utils.py
|-- data/
    |-- sample_data.py
```

- `calculations.py` może zawierać funkcje związane z obliczeniami.
- `io_utils.py` funkcje do wejścia/wyjścia danych (np. odczyt plików).
- `data/` to katalog na dane, a `sample_data.py` może zawierać np. stałe z przykładowymi danymi lub funkcje do ich generowania.
- `main.py` korzysta z powyższych modułów, łącząc je w jedną spójną aplikację.

Po takim podziale zmiana logiki obliczeń wymaga modyfikacji tylko `calculations.py`, a operacje na danych można zmienić, nie dotykając logiki w `main.py`. Taki podział sprzyja skalowaniu projektu i pracy zespołowej – każdy członek zespołu może skupić się na swojej części.

---

### 10. Praktyka: Pisanie funkcji ułatwiających ponowne wykorzystanie kodu

Wyobraźmy sobie, że tworzymy aplikację do analizy ocen studentów. Chcemy napisać funkcje, które:

1. Obliczają średnią z listy ocen.
2. Filtrują studentów, którzy zdali (średnia ocena powyżej 3.0).

```python
# grades_utils.py

def srednia(oceny):
    """Zwraca średnią arytmetyczną ocen z listy."""
    if not oceny:
        return 0
    return sum(oceny) / len(oceny)

def zdali(studenci):
    """
    Przyjmuje listę krotek (imie, [oceny]).
    Zwraca listę imion studentów, których średnia > 3.0
    """
    wyniki = []
    for imie, oceny in studenci:
        if srednia(oceny) > 3.0:
            wyniki.append(imie)
    return wyniki
```

Teraz, niezależnie od miejsca w projekcie, możemy zaimportować `grades_utils` i użyć tych funkcji:

```python
# main.py
import grades_utils

studenci = [
    ("Jan", [5, 4, 3]),
    ("Ala", [2, 2, 3]),
    ("Tomek", [3, 3, 4]),
]

print("Zdali:", grades_utils.zdali(studenci))
# Zdali: ['Jan', 'Tomek']
```

Funkcje `srednia` i `zdali` mogą być teraz ponownie użyte w innych projektach związanych z ocenami, wystarczy je skopiować lub zaimportować.

---

### 11. Praktyka: Strukturyzacja projektu w mniejsze moduły

Załóżmy, że tworzymy mały projekt – program do zarządzania listą zadań (tzw. to-do list). Nasza struktura:

```
todo_app/
|-- main.py
|-- todo.py
|-- utils.py
```

- `todo.py` będzie zawierać funkcje do zarządzania listą zadań (dodawanie, usuwanie, wyświetlanie).
- `utils.py` będzie zawierać funkcje pomocnicze, np. do walidacji danych lub formatowania wyjścia.
- `main.py` będzie głównym plikiem, który korzysta z funkcji dostępnych w pozostałych modułach.

Przykład `todo.py`:

```python
# todo.py

tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)

def show_tasks():
    return tasks
```

Przykład `utils.py`:

```python
# utils.py

def print_tasks(tasks):
    print("Lista zadań:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
```

`main.py`:

```python
# main.py
import todo
import utils

todo.add_task("Kupić mleko")
todo.add_task("Zrobić pranie")
todo.add_task("Nauczyć się Pythona")

utils.print_tasks(todo.show_tasks())

todo.remove_task("Zrobić pranie")
utils.print_tasks(todo.show_tasks())
```

Po uruchomieniu `python main.py`:

```
Lista zadań:
1. Kupić mleko
2. Zrobić pranie
3. Nauczyć się Pythona

Lista zadań:
1. Kupić mleko
2. Nauczyć się Pythona
```

Taki podział znacznie ułatwia rozwój i utrzymanie projektu. Gdy będziesz chciał dodać nowe funkcje, np. zapisywanie zadań do pliku, możesz dodać nowy moduł `storage.py`, a `main.py` tylko zaimportuje i wykorzysta nową funkcję.

---

### 12. Podsumowanie i dalsze kroki

W tym rozdziale nauczyłeś się:

- Definiować funkcje i zwracać z nich wartości.
- Przekazywać argumenty do funkcji, w tym stosować argumenty domyślne i nazwane.
- Rozumieć znaczenie lokalnego i globalnego zakresu zmiennych.
- Dzielić kod na moduły i importować je, aby uzyskać modularną strukturę projektu.

Zdobyte umiejętności są niezwykle ważne w codziennej pracy programisty. Od teraz możesz:

- Pisać przejrzysty, uporządkowany kod, dzieląc go na logiczne części.
- Wielokrotnie wykorzystywać raz zdefiniowane funkcje.
- Zarządzać złożonymi projektami, dzieląc je na moduły, co znacznie ułatwia skalowanie, testowanie i współpracę w zespole.

W kolejnych rozdziałach skupimy się na bardziej zaawansowanych zagadnieniach, takich jak obiektowość, testowanie, obsługa wyjątków czy korzystanie ze standardowej biblioteki Pythona. Jednak solidne opanowanie funkcji i modularności jest fundamentem do zrozumienia i efektywnego wykorzystywania tych bardziej złożonych koncepcji. Nie bój się eksperymentować – im częściej będziesz pisał funkcje i dzielił kod na moduły, tym bardziej naturalna stanie się dla Ciebie ta praktyka.

----

© 2024 Marian Witkowski
