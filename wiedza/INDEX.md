# Indeks bazy wiedzy — mapowanie modułów źródłowych na lekcje

> **Po co ten plik?** Materiały w `wiedza/zrodlo/` są podzielone na 12 **modułów wykładowych** (każdy = duża porcja tekstu). Dla kursu sokratejskiego potrzebujemy **mniejszych jednostek lekcyjnych** (30–60 min). Ten plik mówi: który fragment którego pliku źródłowego odpowiada której lekcji.

> **Jak agent z tego korzysta:**
> 1. Przy generowaniu programu (`program-kursu`) — bierze listę lekcji stąd
> 2. Przy prowadzeniu lekcji (`lekcja`) — **najpierw** sprawdza gotowy plik `wiedza/lekcje/NN.MM-*.md` (39 gotowych lekcji sokratejskich), **potem** sięga do `zrodlo/` + `AKTUALIZACJE.md`
> 3. Gdy uczeń pyta o konkretny temat — szuka tu pasującej lekcji

> **Status gotowych lekcji sokratejskich:** ✅ **39/39 gotowych** w `wiedza/lekcje/` (Moduły 1-12 kompletnie pokryte)

---

## Mapowanie modułów → lekcje

### Moduł 1 — Wprowadzenie i środowisko (źródło: `01-wprowadzenie.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 1.1     | Co to jest Python i do czego służy     | "Czym jest Python", "Krótki rys historyczny", "Zastosowania" | `[ogólne]`, `[moduł 01]`    |
| 1.2     | Pierwszy program — `print` w REPL i z pliku | "Pierwsze uruchomienie", "Hello World"                | `[moduł 01]` — nowy REPL    |
| 1.3     | Edytor i terminal — workflow ucznia   | "Instalacja PyCharm", "Struktura projektu"                 | `[moduł 01]` — VS Code/uv   |

### Moduł 2 — Podstawy języka (źródło: `02-podstawy.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 2.1     | Zmienne i typy proste (int, float, str, bool) | "Zmienne i typy danych", "Konwersje typów"          | `[moduł 02]`                |
| 2.2     | Operatory i wyrażenia                  | "Operacje arytmetyczne", "Priorytety operatorów"           | —                           |
| 2.3     | `print` i f-stringi                    | "Funkcja print()", "Formatowanie napisów (f-stringi)"      | `[moduł 02]` — f-string 3.12 |

### Moduł 3 — Decyzje i powtórzenia (źródło: `03-instrukcje.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 3.1     | `if`/`elif`/`else` i operatory logiczne | "Instrukcja if, elif, else"                               | —                           |
| 3.2     | Pętla `for` i `range`                  | "Pętla for"                                                | `[moduł 03]` — `enumerate`  |
| 3.3     | Pętla `while`, `break`, `continue`     | "Pętla while", "Praktyczne zastosowania"                   | —                           |

### Moduł 4 — Struktury danych (źródło: `04-struktury.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 4.1     | Listy — indeksowanie, slicing, metody  | "Listy", "Operacje na kolekcjach"                          | —                           |
| 4.2     | Krotki — kiedy zamiast listy           | "Krotki"                                                   | —                           |
| 4.3     | Słowniki — klucz/wartość, iteracja     | "Słowniki"                                                 | `[moduł 04]` — uporządkowane |
| 4.4     | Zbiory + zagnieżdżenia                 | "Zbiory (sets)", "Zagnieżdżone struktury"                  | —                           |

### Moduł 5 — Funkcje (źródło: `05-funkcje.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 5.1     | `def`, `return` i argumenty            | "Definiowanie funkcji", "Przekazywanie argumentów"         | —                           |
| 5.2     | Argumenty domyślne i nazwane           | "Argumenty domyślne", "Argumenty nazwane"                  | —                           |
| 5.3     | Scope (lokalny vs globalny), moduły    | "Zakres zmiennych", "Modularność, import"                  | `[moduł 05]` — type hints, dataclasses |

### Moduł 6 — Pliki i debugowanie (źródło: `06-pliki.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 6.1     | Czytanie i zapisywanie plików tekstowych | "Odczyt i zapis plików", "with open"                     | `[moduł 06]` — `pathlib`, `encoding="utf-8"` |
| 6.2     | Pierwsze `try`/`except` — pliki niezawodne | "Podstawy obsługi błędów"                              | —                           |
| 6.3     | Debugger — śledzenie kodu              | "Wykorzystanie debuggera"                                  | `[moduł 06]` — debugger w VS Code |

### Moduł 7 — Programowanie obiektowe (źródło: `07-oop.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 7.1     | Klasa i obiekt — czym to różni się od dict | "Klasy i obiekty", "__init__, atrybuty, metody"        | —                           |
| 7.2     | Dziedziczenie i polimorfizm            | "Dziedziczenie", "Polimorfizm"                             | —                           |
| 7.3     | Wzorce na prostym przykładzie + `@dataclass` | "Przykładowe wzorce projektowe"                      | `[moduł 07]` — dataclass, StrEnum |

### Moduł 8 — Wyjątki i testy (źródło: `08-wyjatki-testy.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 8.1     | Wyjątki — `raise`, hierarchia, własne klasy | "Rzucanie i obsługa wyjątków", "Własne wyjątki"        | `[moduł 08]` — lepsze tracebacki |
| 8.2     | Testy jednostkowe — `pytest` (i `unittest` historycznie) | "Testy jednostkowe, unittest"             | `[moduł 08]` — pytest preferowany |
| 8.3     | TDD — pisz test pierwszy               | "Rola testów", "Podstawy TDD"                              | —                           |

### Moduł 9 — Standardowa i zewnętrzna biblioteka (źródło: `09-stdlib.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 9.1     | `os`, `math`, `datetime` — przegląd stdlib | "Standardowa biblioteka"                                | `[moduł 09]` — `pathlib`, `tomllib` |
| 9.2     | `venv` i `pip` — zarządzanie pakietami | "virtualenv", "pip i PyPI"                                 | `[moduł 09]` — `uv`, `pyproject.toml` |
| 9.3     | `requests` — pobieranie danych z sieci | "requests, dane z API"                                     | `[moduł 09]` — `httpx` alternatywa |

### Moduł 10 — Programowanie funkcyjne i lambda (źródło: `10-prog-funkcyjne.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 10.1    | `lambda` i funkcje wyższego rzędu      | "Funkcje anonimowe (lambda)"                               | —                           |
| 10.2    | `map`, `filter`, `reduce`              | "Funkcje wbudowane: map, filter, reduce"                   | `[moduł 10]` — `functools.reduce` |
| 10.3    | List/dict/set comprehensions           | "List comprehensions", "Dict comprehensions"               | `[moduł 10]` — generator expr |
| 10.4    | `itertools` — magiczne pętle           | (dopisać, źródło może nie ruszać)                          | `[moduł 10]` — chain, groupby |

### Moduł 11 — Projekt końcowy (źródło: `11-projekt.md`)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 11.1    | Wybór projektu i specyfikacja          | "Zaprojektowanie projektu"                                 | —                           |
| 11.2    | Implementacja — krok po kroku          | "Realizacja projektu, organizacja kodu"                    | `[moduł 11]` — `pyproject.toml` |
| 11.3    | Testy, błędy, dokumentacja             | "Testy, obsługa błędów, dokumentacja"                      | —                           |
| 11.4    | Git, README, deploy (opcjonalnie)      | "Wykorzystanie Git"                                        | `[moduł 11]` — `git` jako standard |

### Moduł 12 — Podsumowanie i dalsze kroki (źródło: `12-podsumowanie.md`, **74KB — czytaj selektywnie**)

| Lekcja  | Temat                                  | Źródło (sekcje)                                            | Aktualizacja                |
| ------- | -------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| 12.1    | PEP 8 i czystość kodu                  | "Najlepsze praktyki w Pythonie, PEP8"                      | `[moduł 12]` — `ruff` zamiast pylint |
| 12.2    | Mapa ekosystemu — frameworks, data, ML | "Frameworks (Django, Flask), data science, automatyzacja"  | `[moduł 12]` — Polars, FastAPI, AI |
| 12.3    | Gdzie szukać dalej + AI-assisted coding | "Gdzie szukać pomocy, dokumentacja, społeczność"          | `[moduł 12]` — Copilot, Claude Code |

---

## Podsumowanie liczbowe

- **Modułów źródłowych:** 12
- **Lekcji sokratejskich:** 39 (średnio 3 na moduł, niektóre po 4)
- **Łączny czas (estymata):** 35–55 h (lekcja = 30–90 min zależnie od trudności)
- **Tempo:**
  - <2h/tydz → ~30 tygodni
  - 2–5h/tydz → ~10–15 tygodni
  - 5+h/tydz → ~6–10 tygodni

---

## Jak skill `program-kursu` buduje plan dla ucznia

1. Czyta ten plik (`INDEX.md`)
2. Dostosowuje do **celu ucznia** (praca / hobby / dane / szkoła):
   - **praca/dane** → moduł 9 ma rozszerzenie o `requests`/CSV; moduł 11 projekt pod CSV/API
   - **hobby/gra** → moduł 11 projekt jako gra tekstowa, moduł 10 minimal
   - **szkoła** → moduł 11 projekt matematyczny, moduł 10 standardowy
3. Dostosowuje do **tempa** (modyfikuje gęstość lekcji na tydzień)
4. Generuje `kurs/program.md` z tabelą 39 lekcji + datami orientacyjnymi
5. Można potem edytować — to plan, nie kontrakt
