## Blok 6: Praca z plikami i wprowadzenie do debugowania

Poniższy rozdział poświęcony jest obsłudze plików w Pythonie, podstawowym zagadnieniom związanym z obsługą błędów oraz wprowadzeniu do debugowania kodu, ze szczególnym uwzględnieniem narzędzi dostępnych w PyCharm. Te umiejętności są kluczowe dla bardziej dojrzałego programisty: umożliwiają efektywne przetwarzanie danych zewnętrznych (np. z plików tekstowych), reagowanie na nieprzewidziane sytuacje podczas działania programu oraz skuteczne diagnozowanie problemów z wykorzystaniem debuggera. W części praktycznej napiszemy skrypt do analizy danych z pliku tekstowego i prześledzimy jego działanie krok po kroku, korzystając z punktów kontrolnych (breakpointów) w PyCharm.

---

### 1. Wprowadzenie do pracy z plikami w Pythonie

Wiele aplikacji potrzebuje wczytywać dane z zewnętrznych źródeł, takich jak pliki tekstowe, pliki CSV, czy inne formaty. Praca z plikami to umiejętność, która otwiera dostęp do szerszego kontekstu danych: można analizować logi, konfigurować aplikacje na podstawie plików konfiguracyjnych czy zapisywać wyniki obliczeń do raportów. Python udostępnia proste i czytelne mechanizmy do odczytu, zapisu i modyfikacji plików, co znacznie ułatwia te zadania.

Podstawowy schemat pracy z plikiem w Pythonie wygląda tak:

1. Otwieramy plik za pomocą funkcji `open()`.
2. Wykonujemy operacje odczytu lub zapisu.
3. Zamykamy plik lub używamy konstrukcji `with` w celu automatycznego zamknięcia.

---

### 2. Odczyt i zapis plików tekstowych

Najprostsze i najczęstsze zastosowanie to praca z plikami tekstowymi. Funkcja `open()` przyjmuje m.in. dwa kluczowe parametry: nazwę pliku oraz tryb, w jakim chcemy ten plik otworzyć. Podstawowe tryby to:

- `"r"` – odczyt (read)
- `"w"` – zapis (write, tworzy nowy plik lub nadpisuje istniejący)
- `"a"` – dopisywanie (append, dopisuje dane na końcu istniejącego pliku)
- `"r+"` – odczyt i zapis

Przykład odczytu całej zawartości pliku:

```python
with open("dane.txt", "r", encoding="utf-8") as plik:
    zawartosc = plik.read()
    print(zawartosc)
```

`with` to konstrukcja, która gwarantuje, że plik zostanie zamknięty nawet jeśli w trakcie operacji wystąpi błąd. Parametr `encoding="utf-8"` jest rekomendowany, aby uniknąć problemów z polskimi znakami.

Aby odczytać plik linijka po linijce można użyć:

```python
with open("dane.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        print(linia.strip())
```

Metoda `strip()` usuwa znaki nowe linii i odstępy z końca linii.

Zapis do pliku polega na otwarciu go w trybie `"w"` lub `"a"` i użyciu metody `write()`:

```python
with open("wyniki.txt", "w", encoding="utf-8") as plik:
    plik.write("To jest przykładowy tekst.\n")
    plik.write("Zapisujemy kolejną linię.\n")
```

Jeśli `wyniki.txt` istniał wcześniej, zostanie nadpisany. Gdybyśmy użyli `"a"`, to nowy tekst zostałby dopisany do istniejącej zawartości.

---

### 3. Praca z dużymi plikami i częściowy odczyt danych

Czasami plik może być bardzo duży i nie chcemy wczytywać go w całości do pamięci. Możemy wtedy korzystać z odczytu liniowego (jak w przykładzie z pętlą `for`) lub używać metody `readline()`:

```python
with open("duzy_pliki.txt", "r", encoding="utf-8") as plik:
    linia = plik.readline()
    while linia:
        # Przetwarzamy linię
        linia = plik.readline()
```

Możemy też odczytywać dane porcjami, np. po kilkaset bajtów, używając `read(n)`:

```python
with open("duzy_plik.txt", "r", encoding="utf-8") as plik:
    fragment = plik.read(1024)  # czytamy 1024 bajty
    while fragment:
        # przetwarzamy fragment danych
        fragment = plik.read(1024)
```

Takie podejście pozwala obsługiwać naprawdę duże pliki, minimalizując zużycie pamięci.

---

### 4. Podstawy obsługi błędów (try-except)

W trakcie pracy z plikami (i każdymi innymi zasobami) mogą wystąpić błędy, np. plik nie istnieje, brak uprawnień do zapisu, czy błąd formatowania danych. Program musi sobie z tym poradzić, a nie po prostu zakończyć działanie błędem.

Do obsługi błędów w Pythonie służy konstrukcja `try-except`:

```python
try:
    with open("dane.txt", "r", encoding="utf-8") as plik:
        zawartosc = plik.read()
        print(zawartosc)
except FileNotFoundError:
    print("Plik nie został znaleziony!")
except PermissionError:
    print("Brak uprawnień do odczytu pliku!")
except Exception as e:
    print("Wystąpił nieoczekiwany błąd:", e)
```

Blok `try` zawiera kod, który może zgłosić wyjątek. Jeśli wystąpi błąd, interpreter poszuka pasującego bloku `except`. Można wymienić konkretne typy wyjątków, aby różne błędy obsłużyć w różny sposób. `Exception` to ogólny wyjątek łapiący większość błędów. Zmienna `e` pozwala wyświetlić informację o wystąpieniu konkretnego błędu.

---

### 5. Zalety kontrolowanej obsługi błędów

Kontrolowana obsługa błędów umożliwia tworzenie bardziej odpornych programów:

- Jeśli plik nie istnieje, można poinformować użytkownika i poprosić o inną nazwę pliku.
- Jeśli pojawi się nieznany błąd, można wyświetlić komunikat i bezpiecznie zamknąć program.
- Bloki `try-except` można łączyć z `finally`, aby wykonać kod czyszczący zasoby, bez względu na to, czy wystąpił wyjątek.

Przykład `finally`:

```python
plik = None
try:
    plik = open("dane.txt", "r", encoding="utf-8")
    zawartosc = plik.read()
except FileNotFoundError:
    print("Brak pliku.")
finally:
    if plik is not None:
        plik.close()
```

Dzięki `finally` plik zostanie zamknięty nawet, gdy dojdzie do błędu podczas czytania.

W praktyce używanie konstrukcji `with` jest preferowane, bo automatycznie zamyka plik, eliminując konieczność stosowania `finally` do tego celu.

---

### 6. Debugowanie – czym jest i dlaczego jest ważne?

Debugowanie to proces wyszukiwania i naprawiania błędów w kodzie. Nawet doświadczonym programistom zdarza się popełniać błędy, a złożone programy trudno zrozumieć na pierwszy rzut oka. Narzędzia takie jak debugger pozwalają uruchomić kod krok po kroku, sprawdzić aktualne wartości zmiennych, prześledzić przepływ wykonania programu i zlokalizować, gdzie dokładnie pojawiają się problemy.

Dobre praktyki debugowania:

- Dodawanie breakpointów w miejscach, gdzie chcemy zatrzymać wykonanie i sprawdzić stan programu.
- Sprawdzanie wartości zmiennych, aby zrozumieć, czy są takie, jakich oczekujemy.
- Krokowe wykonywanie instrukcji, aby zobaczyć, w którym momencie pojawia się niepoprawne zachowanie.

---

### 7. Debugowanie w PyCharm – podstawy

PyCharm oferuje wbudowany debugger, który ułatwia diagnozowanie problemów:

1. **Breakpoint** – punkt przerwania: ustawiamy go klikając w obszarze z numerami linii (zwykle po lewej stronie edytora). Gdy program dojdzie do tej linii, zatrzyma się i pozwoli nam zbadać stan.
2. **Przyciski sterujące wykonaniem** – w trybie debugowania mamy przyciski do pojedynczego kroku w przód (Step Over), wchodzenia do funkcji (Step Into), wyjścia z funkcji (Step Out) i kontynuowania do następnego breakpointu (Resume).
3. **Okno wartości zmiennych** – pokazuje aktualne wartości zmiennych lokalnych i globalnych w danym miejscu kodu.
4. **Konsola debuggera** – możemy w niej wpisywać wyrażenia Pythonowe i sprawdzać wartości za pomocą tzw. "watch expressions" lub zmieniać wartości zmiennych w locie.

Dzięki tym narzędziom w prosty sposób można znaleźć miejsce w kodzie, w którym wartości różnią się od oczekiwanych, lub zrozumieć dlaczego pętla nigdy się nie kończy.

---

### 8. Przykład: Analityka danych z pliku i debugowanie

Wyobraźmy sobie, że mamy plik tekstowy `dane.txt` zawierający liczby – każda w osobnej linii:

```
10
5
8
12
3
```

Chcemy napisać skrypt, który odczyta te liczby, obliczy ich sumę i średnią, a następnie wypisze wynik. Następnie przejdziemy do debugowania, aby podejrzeć proces działania krok po kroku.

**Kod przykładowy (analityka.py):**

```python
def wczytaj_liczby_z_pliku(nazwa_pliku):
    liczby = []
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        for linia in plik:
            linia = linia.strip()
            if linia:
                # Spróbujmy przekonwertować linię na int
                liczba = int(linia)
                liczby.append(liczba)
    return liczby

def oblicz_statystyki(liczby):
    if not liczby:
        raise ValueError("Lista liczb jest pusta. Nie można obliczyć statystyk.")
    suma = sum(liczby)
    srednia = suma / len(liczby)
    return suma, srednia

def main():
    try:
        nazwa_pliku = "dane.txt"
        dane = wczytaj_liczby_z_pliku(nazwa_pliku)
        suma, srednia = oblicz_statystyki(dane)
        print(f"Suma: {suma}, Średnia: {srednia:.2f}")
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie został znaleziony.")
    except ValueError as e:
        print("Błąd:", e)

if __name__ == "__main__":
    main()
```

Ten skrypt:

- Odczytuje liczby z pliku `dane.txt`.
- Oblicza sumę i średnią.
- Obsługuje sytuację, w której plik nie istnieje, oraz gdy brak danych.
- Wyświetla wyniki.

---

### 9. Uruchamianie i debugowanie w PyCharm

Aby zdebugować ten skrypt w PyCharm:

1. Otwórz projekt z tym plikiem `analityka.py`.
2. Ustaw breakpoint w linii np. `dane = wczytaj_liczby_z_pliku(nazwa_pliku)`.
3. Uruchom program w trybie debugowania, klikając na ikonę „debug” (zielony robaczek lub opcyjnie: Run > Debug).
4. Gdy wykonanie programu zatrzyma się na breakpoint, przejrzyj wartości zmiennych w zakładce "Variables".
5. Możesz wykonać pojedynczy krok do przodu (Step Over) i obserwować, jak zmienia się zawartość zmiennych.
6. Jeśli zauważysz, że `dane` nie wyglądają, jak powinny, możesz sprawdzić dlaczego. Może plik ma inne dane niż oczekiwane? Możesz też dodać kolejne breakpointy wewnątrz funkcji `wczytaj_liczby_z_pliku`, aby obserwować, jak iteruje po liniach pliku.

Przykładowo, jeśli w pliku dane.txt umieścisz puste linie lub niedozwolone znaki, możesz zauważyć błąd `ValueError` przy konwersji na int. Dodając breakpoint w miejscu konwersji, zobaczysz, co faktycznie stoi w `linia`.

---

### 10. Interaktywne diagnozowanie problemów

W trybie debugowania możesz również edytować wartości zmiennych w locie (chociaż to nie zawsze jest najlepszy pomysł w produkcyjnym kodzie, ale może pomóc testować różne scenariusze). Możesz używać konsoli debuggera, aby wywołać funkcje z aktualnego kontekstu, sprawdzić typy zmiennych lub wykonać proste obliczenia.

Dzięki temu, zamiast zgadywać, dlaczego wynik jest nieprawidłowy, możesz zobaczyć dokładnie, co dzieje się w środku programu.

---

### 11. Inne strategie debugowania

Oprócz używania debuggera, w praktyce stosuje się też inne metody:

- Wstawianie tymczasowych `print()` do kodu, aby zobaczyć wartości zmiennych. Jest to mało eleganckie, ale często szybkie i skuteczne. Później można usunąć te instrukcje.
- Logowanie zdarzeń i błędów za pomocą modułu `logging`, aby mieć wgląd w działanie programu bez przerywania go.
- Pisanie testów jednostkowych, aby wychwycić błędy na wczesnym etapie, zamiast debugować gotowy i skomplikowany fragment kodu.

Prawdziwa siła debugera polega na tym, że pozwala pracować z żywym programem, obserwując jego stan w czasie rzeczywistym.

---

### 12. Podsumowanie i dalsze kroki

W tym rozdziale nauczyłeś się:

- Jak odczytywać i zapisywać pliki tekstowe w Pythonie.
- Jak radzić sobie z błędami przy pomocy konstrukcji `try-except`, co zwiększa odporność programu na nieprzewidziane sytuacje.
- Jak korzystać z debuggera w PyCharm, aby krok po kroku prześledzić działanie programu, badać wartości zmiennych i lokalizować problemy.

Te umiejętności są niezwykle ważne w praktyce programistycznej. Praca z danymi z plików jest powszechna w niemal każdym projekcie, a kontrola nad błędami pozwala budować oprogramowanie bardziej odporne na problemy. Debugger natomiast skraca czas spędzony na szukaniu błędów do minimum i daje wgląd w to, jak naprawdę działa Twój kod.

W kolejnych blokach poszerzymy wiedzę o bardziej złożone aspekty programowania, takie jak obiektowość, testowanie czy korzystanie z popularnych bibliotek. Wszystkie te umiejętności łączą się w spójną całość, pozwalając Ci tworzyć coraz bardziej zaawansowane, stabilne i wydajne programy. Kontynuuj praktykę z plikami, testuj różne scenariusze błędów i regularnie korzystaj z debuggera – to wpłynie pozytywnie na Twoje zrozumienie i efektywność jako programisty.

----

© 2024 Marian Witkowski
