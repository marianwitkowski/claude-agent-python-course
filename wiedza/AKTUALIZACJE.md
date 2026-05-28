# Aktualizacje merytoryczne — co dodać do treści z `zrodlo/`

> **Po co ten plik?** Materiały w `wiedza/zrodlo/` pochodzą z grudnia 2024. Od tego czasu wyszło Python 3.13 (paź 2024) i Python 3.14 (paź 2025), zmieniły się rekomendowane narzędzia, część idiomów się odświeżyła. Ten plik to **aneks** — agent prowadząc lekcję czyta treść źródłową ORAZ odpowiednią sekcję stąd, by przekazać uczniowi aktualną wiedzę.

> **Jak czytać:** każda sekcja zaczyna się od `## [moduł NN]` lub `## [ogólne]`. Agent szuka pasującej sekcji przed prowadzeniem lekcji.

---

## [ogólne] Wersja Pythona w 2026

- **Stabilne:** Python 3.13 (LTS-podobne, większość firm), Python 3.14 (najnowsza, paź 2025)
- **EOL:** Python 3.8 (paź 2024), 3.9 (paź 2025) — **nie polecaj nikomu instalacji**
- **Minimalna rekomendowana:** Python 3.11 (3.12+ preferowane dla nowych projektów)
- **Komenda sprawdzenia:** `python3 --version`. Na nowych macOS-ach `python` częściej już wskazuje na Python 3, ale **bezpieczniej trzymać `python3`**.

---

## [moduł 01] Wprowadzenie i przygotowanie środowiska

### Zmiany w narzędziach (od 2024-12)

**IDE:**
- Repo poleca **PyCharm Community**. To wciąż OK, ale w 2026 **VS Code + rozszerzenie Python** ma większy mindshare wśród początkujących (lżejszy, darmowy w pełni, ekosystem AI).
- JetBrains od 2024 oferuje **PyCharm Community** za darmo z dodatkowymi funkcjami (wcześniej Pro było płatne).
- Alternatywy worth mentioning: **Zed**, **Cursor** (VS Code fork z AI).

**Package manager:**
- `pip` nadal działa, ale w 2025+ standardem staje się **`uv`** (od Astral, ~10-100× szybszy od pip). Polecaj go dla nowych projektów: `pip install uv` → potem `uv venv`, `uv pip install <paczka>`.
- `pipx` — do instalacji narzędzi CLI (jak `ruff`, `black`).

**Linter/formatter:**
- Repo nie wspomina, ale w 2026 standardem jest **`ruff`** (zastępuje `pylint`, `flake8`, `isort`, `black` w jednym narzędziu).
- Konfiguracja w `pyproject.toml`.

### "Pierwszy program"

Repo używa PyCharm jako pierwszego kroku. Dla **kompletnego początkującego** sokratejsko lepiej zacząć od:
1. **Tryb interaktywny `python3`** w terminalu — od razu widać efekt
2. **Plik `.py` w prostym edytorze** — uruchamiany z terminala
3. **Dopiero potem IDE** — kiedy uczeń wie, co robi terminal

### Lepsze tracebacki (3.11+, znacznie lepsze w 3.13)

Python 3.11+ pokazuje **karet (^^^^^) pod fragmentem linii** z błędem — to ogromna pomoc dla początkujących:
```
File "test.py", line 1
    print(2 + )
              ^
SyntaxError: invalid syntax
```
W 3.13 dodano **kolorowanie** tracebacków w terminalu. Pokaż to uczniowi — uspokaja patrzenie na błędy.

### Nowy REPL w 3.13

W Python 3.13 wbudowany REPL (`python3`) dostał:
- multi-line edit (strzałki w górę cofają cały blok, nie tylko linię)
- kolorowanie składni
- lepszą historię, paste mode (`F3`)
- `exit` bez nawiasów (działa też `quit`)

Dla początkującego — używanie REPL stało się dużo przyjemniejsze.

---

## [moduł 02] Podstawy języka — składnia i typy danych

### f-stringi w 3.12+ (PEP 701)

**Stare ograniczenie (przed 3.12):** nie można było zagnieżdżać tych samych cudzysłowów wewnątrz f-stringa.

**Teraz (3.12+):**
```python
imie = "Anna"
print(f"Cześć {imie if imie != "" else "nieznajomy"}!")  # działa
# Można nawet wielolinijkowe:
print(f"""
  Imię: {imie}
  Długość: {len(imie)}
""")
```

Pokaż uczniowi: f-stringi są elastyczniejsze niż w starych tutorialach.

### `match`/`case` (3.10+) — wspomnij krótko

Repo używa łańcuchów `elif`. Od Python 3.10 jest **`match`** (jak `switch` w innych językach, ale silniejszy — pattern matching). Dla początkującego **wspomnij i odłóż** — najpierw `if/elif/else`, potem `match` jako "ciekawszy sposób":
```python
match dzien:
    case "pn" | "wt" | "śr" | "czw" | "pt":
        print("dzień roboczy")
    case "sob" | "niedz":
        print("weekend")
    case _:
        print("nieznany dzień")
```

### Operator walrus `:=` (3.8+, idiom)

W repo brak. Wspomnij gdy uczeń pisze:
```python
linia = input()
while linia != "stop":
    print(linia)
    linia = input()
```
Idiom z walrusem (krótszy, bez duplikacji):
```python
while (linia := input()) != "stop":
    print(linia)
```
Ale: **dla początkującego** najpierw klasyczna wersja, potem dopiero pokazujemy "skrót". Walrus to lukrowy idiom.

---

## [moduł 03] Instrukcje warunkowe i pętle

### `except` bez nawiasów (3.14, PEP 758)

Tylko wzmianka — nie używaj w lekcjach jako standardu.

### Bardziej Pythonowe pętle

Repo pewnie pokazuje `for i in range(len(lista))`. To **anty-idiom** w 2026:

```python
# zamiast:
for i in range(len(lista)):
    print(i, lista[i])

# pisz:
for i, element in enumerate(lista):
    print(i, element)

# i jeśli nie potrzebujesz indeksu:
for element in lista:
    print(element)
```

Pokaż uczniowi obie wersje, niech zobaczy różnicę w czytelności.

---

## [moduł 04] Struktury danych

### Type hints na kolekcjach — uproszczenie (3.9+, standard w 3.12)

Repo pewnie nie używa hintów (i dobrze — dla początkującego nadmiar). Ale jeśli się pojawiają:

```python
# stare (działa, ale przestarzałe):
from typing import List, Dict
def f(x: List[int]) -> Dict[str, int]: ...

# nowe (3.9+, standard od 3.12):
def f(x: list[int]) -> dict[str, int]: ...
```

### `set` literały i `frozenset` — bez zmian

Nadal: `{1, 2, 3}`, `set()` dla pustego, `frozenset(...)` dla niemutowalnego.

### Słowniki uporządkowane

Repo może mówić "słowniki nie są uporządkowane". **Od Python 3.7 są** — kolejność wstawiania jest gwarantowana przez specyfikację języka. To ważna poprawka, początkujący się tym łatwo myli.

---

## [moduł 05] Funkcje i modularność

### Pozycyjne i nazwane parametry (3.8+, standard)

Dla początkującego pomiń, ale wiedz że istnieje:
```python
def f(a, b, /, c, d, *, e, f):  # a,b pozycyjne tylko; e,f nazwane tylko
    ...
```

### Type hints na funkcjach

Dla początkującego — opcjonalnie wprowadź pod koniec modułu 5:
```python
def witaj(imie: str, glosno: bool = False) -> str:
    tekst = f"Cześć {imie}!"
    return tekst.upper() if glosno else tekst
```
Hinty są **opcjonalne**, nie wymuszane w runtime — ale pomagają IDE i czytelnikom.

### `dataclasses` — krótka wzmianka (przejście do OOP)

Od Python 3.7. Pomost między "klasy" a "po co mi to":
```python
from dataclasses import dataclass

@dataclass
class Punkt:
    x: float
    y: float

p = Punkt(3, 4)
print(p)  # Punkt(x=3, y=4) — gotowy __repr__
```
Dla początkującego po OOP (moduł 7) — dataclasses to wygodny upgrade.

---

## [moduł 06] Pliki i debugowanie

### `pathlib` zamiast `os.path` — od dawna preferowane

Repo prawdopodobnie pokazuje:
```python
import os
sciezka = os.path.join("dane", "plik.txt")
if os.path.exists(sciezka):
    with open(sciezka) as f: ...
```

W 2026 **standardem jest `pathlib`**:
```python
from pathlib import Path
sciezka = Path("dane") / "plik.txt"
if sciezka.exists():
    tekst = sciezka.read_text(encoding="utf-8")
```

Pokaż obie wersje, ale codziennie używaj `pathlib`. Metody `.read_text()` / `.write_text()` zastępują `open()` w 90% przypadków.

### Encoding — zawsze podawaj jawnie

```python
with open("plik.txt", encoding="utf-8") as f: ...
```
W repo mogą być przykłady bez `encoding=`. Na Windows domyślny encoding to **`cp1250`**, nie UTF-8 — i to powoduje błędy z polskimi znakami. **Zawsze `encoding="utf-8"`** dla plików tekstowych.

### `tomllib` (3.11+) — czytanie TOML w stdlib

Wcześniej trzeba było `pip install toml`. Teraz w stdlib:
```python
import tomllib
with open("pyproject.toml", "rb") as f:
    dane = tomllib.load(f)
```

---

## [moduł 07] Programowanie obiektowe

### `@dataclass` (powtórzenie z modułu 5)

Standard od Python 3.7. Pokaż jako alternatywę dla pełnego `__init__`.

### `enum` z `StrEnum` (3.11+)

Repo może nie ruszać enumów. Jeśli pojawi się — `StrEnum` to wygoda:
```python
from enum import StrEnum

class Status(StrEnum):
    AKTYWNY = "aktywny"
    NIEAKTYWNY = "nieaktywny"

print(Status.AKTYWNY == "aktywny")  # True
```

### Protocols zamiast ABC (typowanie strukturalne)

Dla zaawansowanych — wspomnij w module 7 lub 8:
```python
from typing import Protocol

class Drukowalny(Protocol):
    def drukuj(self) -> None: ...
```
Nie trzeba dziedziczyć, by spełniać protocol. To duck typing z type hints.

---

## [moduł 08] Wyjątki i testy

### `pytest` >> `unittest` w 2026

Repo skupia się na `unittest`. **Standardem w ekosystemie jest `pytest`** — krótsze, czytelniejsze, lepsze komunikaty błędów:

```python
# pytest:
def test_dodawanie():
    assert 2 + 2 == 4

# unittest (więcej szablonu):
import unittest
class TestDodawanie(unittest.TestCase):
    def test_dodawanie(self):
        self.assertEqual(2 + 2, 4)
```

Polecaj `pytest` jako podstawowe narzędzie. `unittest` znajomość — przydatna w starszych kodach.

### `ExceptionGroup` (3.11+, PEP 654)

Dla zaawansowanych. Wspomnij że istnieje, gdy uczeń pyta "co jeśli mam wiele błędów naraz?":
```python
raise ExceptionGroup("wiele rzeczy się popsuło", [ValueError("x"), TypeError("y")])

try:
    ...
except* ValueError as eg:
    ...
```

### Lepsze komunikaty błędów (3.12+)

Python coraz lepiej sugeruje, co użytkownik chciał napisać:
```
NameError: name 'lne' is not defined. Did you mean: 'len'?
```
Powiedz uczniowi: gdy widzisz "Did you mean...", zawsze sprawdź sugestię.

---

## [moduł 09] Standardowa biblioteka i zewnętrzne

### `requests` — czy nadal pierwszy wybór?

- `requests` (zewnętrzny) — nadal popularny, dojrzały.
- `httpx` — nowsza alternatywa, async-friendly, kompatybilne API.
- `urllib.request` (stdlib) — jest, ale nie polecaj początkującemu (brzydsze API).

Dla nowicjusza: zostań przy `requests`, ale wspomnij że `httpx` to opcja na przyszłość.

### `virtualenv` vs `venv` vs `uv`

- `virtualenv` — stara biblioteka, działa, ale **`venv` jest w stdlib** od Python 3.3.
- W 2026 polecaj: `python3 -m venv .venv && source .venv/bin/activate`
- Jeszcze szybciej: `uv venv` (od Astral) — tworzy `.venv` w ułamku sekundy.

### `pip` w 2026

`pip install <paczka>` nadal działa. Zalecenia:
- **Zawsze w venv**, nigdy systemowo (Python 3.12+ na macOS i Linuksie blokuje `pip install` na systemowym pythonie — komunikat `externally-managed-environment`)
- Lock file: `pip freeze > requirements.txt`, albo nowocześniej `uv pip compile`
- Konfiguracja projektu w `pyproject.toml` (PEP 621)

---

## [moduł 10] Programowanie funkcyjne i lambda

### `reduce` — `functools.reduce`

Repo prawdopodobnie OK. Tylko: w Python 3, `reduce` **nie jest** w builtins — trzeba `from functools import reduce`. Częsta pułapka dla osób z Python 2.

### Generator expressions vs list comprehensions

Idiom: jeśli wynik tylko iterujemy raz, **gen-exp** (`(x*2 for x in dane)`) jest tańszy niż lista. List compr. tworzy całość w pamięci.

### `itertools` warto pokazać

Standardowa biblioteka `itertools` to złoto dla pętli:
- `chain(*listy)` — łączenie wielu iterowalnych
- `groupby()` — grupowanie kolejnych
- `accumulate()` — sumy częściowe
- `combinations()`, `permutations()` — kombinatoryka

Wspomnij w 09 lub 10.

---

## [moduł 11] Projekt końcowy

### Współczesny szablon projektu

Repo może promować strukturę z 2024. Aktualizacja:

```
projekt/
├── pyproject.toml          # zamiast setup.py/requirements.txt
├── README.md
├── .venv/                  # virtualenv (gitignored)
├── src/projekt/
│   ├── __init__.py
│   └── main.py
└── tests/
    └── test_main.py
```

Narzędzia w `pyproject.toml`:
```toml
[project]
name = "moj-projekt"
version = "0.1.0"
dependencies = ["requests"]

[tool.ruff]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### Scraping w 2026

Repo może proponować `requests` + `BeautifulSoup`. To nadal OK. Nowsze opcje:
- **`httpx`** zamiast `requests` (async-friendly)
- **`selectolax`** zamiast `BeautifulSoup` (znacznie szybsze)
- **`playwright`** zamiast `selenium` (do JS-heavy stron)
- Pamiętaj o `robots.txt` i rate-limiting

### Git i GitHub — wzmianka

Repo wspomina "opcjonalnie Git". W 2026 **to nie jest opcjonalne** dla projektu końcowego — initial commit + push do GitHuba powinien być standardem. Krótka instrukcja `git init`, `git add`, `git commit`, `git push` to dobre zakończenie projektu.

---

## [moduł 12] Podsumowanie i dalsze kroki

### Frameworks — aktualne stany (2026)

- **Backend:** Django (5.x), Flask, **FastAPI** (jeśli API/async)
- **Data science:** NumPy, pandas, **Polars** (szybsza alternatywa dla pandas)
- **ML/AI:** PyTorch (dominacja), TensorFlow (mniej), **transformers** (HuggingFace)
- **Automatyzacja:** `playwright`, `prefect`, **`uv` + `ruff`** w pipeline'ach
- **Notebook:** Jupyter, **marimo** (nowsza alternatywa, reaktywne notebooki)

### Społeczność po polsku

- Discord: PyCoders Poland, OldCamp
- Konferencje: PyCon PL (rokrocznie), PyData Warsaw
- Słowianie w open source: wymień **Astral** (uv, ruff) jako warty śledzenia

### Wskazówki do dalszej nauki — uzupełnienie

Po module 12 z repo dorzuć:
- **AI-assisted coding:** GitHub Copilot, Claude Code, Cursor — naucz się z nich korzystać świadomie (czytać, nie kopiować)
- **Code review:** czytanie cudzego kodu na GitHubie to potężna szkoła
- **Open source:** pierwszy PR do dowolnego projektu (literówka w README się liczy!)

---

## [meta] Zasady stosowania aktualizacji

Gdy agent prowadzi lekcję:

1. **Najpierw** sprawdza odpowiedni rozdział `wiedza/zrodlo/NN-...md`
2. **Następnie** szuka tu sekcji `[moduł NN]` lub `[ogólne]` z dodatkami
3. **Treść z `zrodlo/` ma pierwszeństwo** jako podstawa, ale agent zastępuje przestarzałe fragmenty (np. `os.path` → `pathlib`) wg tego pliku
4. **Wspomina o nowościach** (np. lepsze tracebacki, walrus, match) — ale **nie wprowadza ich zamiast podstaw**. Najpierw klasyczny sposób, potem nowoczesny jako "skrót/lepszy idiom"
5. **Edycje tego pliku** — uczeń/autor może edytować swobodnie. Plik nie jest mirrorem.
