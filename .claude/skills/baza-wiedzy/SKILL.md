---
name: baza-wiedzy
description: Zarządza lokalną bazą wiedzy kursu (katalog `wiedza/`) — pobiera świeże wersje plików z repo źródłowego `marianwitkowski/python-kurs-podstawowy`, pokazuje stan bazy, pozwala porównać lokalną wersję ze zdalną. Użyj gdy uczeń/autor mówi "odśwież bazę wiedzy", "pobierz najnowszą wersję materiałów", "sprawdź czy baza jest aktualna", "pokaż stan bazy wiedzy".
---

# Cel

Trzymać lokalną kopię materiałów źródłowych w `wiedza/zrodlo/` aktualną z repo `marianwitkowski/python-kurs-podstawowy`, ale **nigdy nie aktualizować bez świadomej decyzji ucznia/autora** — żeby nie nadpisać lokalnych edycji.

# Architektura bazy wiedzy

```
wiedza/
├── zrodlo/                       # 1:1 kopia repo (NIE edytuj ręcznie)
│   ├── 01-wprowadzenie.md
│   ├── 02-podstawy.md
│   ├── ...
│   ├── 12-podsumowanie.md
│   └── README.md
├── AKTUALIZACJE.md               # delta: nowości Pythona 3.12-3.14, idiomy, narzędzia
├── INDEX.md                      # mapowanie 12 modułów źródłowych → ~25 lekcji sokratejskich
└── lekcje/                       # generowane lekcje (sokratejskie wersje z notatkami tutora)
    ├── 01.01-pierwszy-print.md
    ├── 01.02-czytanie-bledow.md
    └── ...
```

**Reguła:** `zrodlo/` to czysty mirror — nie edytujemy tu. Zmiany merytoryczne lądują w `AKTUALIZACJE.md` (delta) lub w `lekcje/*.md` (już przerobione na sokratejskie).

# Operacje

## 1. Odśwież bazę (pobierz najnowszą wersję)

Gdy uczeń/autor mówi "odśwież bazę wiedzy":

1. **Zapytaj o potwierdzenie:**
   > "Pobiorę aktualne wersje 12 plików .md z repo. Jeśli edytowałeś coś ręcznie w `wiedza/zrodlo/`, te zmiany zostaną nadpisane (kopię zapasową zrobię w `wiedza/zrodlo.backup-YYYY-MM-DD/`). Kontynuować?"
2. Po `tak` → backup + pobranie:

```bash
TIMESTAMP=$(date +%Y-%m-%d-%H-%M)
[ -d wiedza/zrodlo ] && cp -r wiedza/zrodlo "wiedza/zrodlo.backup-$TIMESTAMP"

cd wiedza/zrodlo
for f in 01-wprowadzenie 02-podstawy 03-instrukcje 04-struktury 05-funkcje \
         06-pliki 07-oop 08-wyjatki-testy 09-stdlib 10-prog-funkcyjne \
         11-projekt 12-podsumowanie README; do
  curl -sL "https://raw.githubusercontent.com/marianwitkowski/python-kurs-podstawowy/main/${f}.md" \
    -o "${f}.md" && echo "OK ${f}.md"
done
```

3. Pokaż uczniowi:
   - rozmiar/linie każdego pliku przed i po
   - datę ostatniego commita w repo (z GitHub API)
   - przypomnienie: "Jeśli coś istotnego się zmieniło, warto przejrzeć `wiedza/AKTUALIZACJE.md` i ewentualnie zaktualizować notatki w `wiedza/lekcje/`."

## 2. Stan bazy wiedzy

Gdy uczeń mówi "pokaż stan bazy" / "co jest w bazie":

Wypisz:
- Liczba plików w `wiedza/zrodlo/` i ich daty modyfikacji
- Data ostatniego pobrania (z najnowszego `zrodlo.backup-*` LUB z `mtime` plików)
- Data ostatniego commita w repo źródłowym (GitHub API)
- Liczba wygenerowanych lekcji w `wiedza/lekcje/`
- Czy `AKTUALIZACJE.md` istnieje i kiedy ostatnio aktualizowane

## 3. Sprawdź różnice ze zdalnym repo

Gdy uczeń mówi "sprawdź czy baza aktualna" / "diff bazy":

1. Pobierz **do tymczasowego katalogu** `/tmp/python-kurs-check-$$/`
2. Porównaj `diff -r wiedza/zrodlo /tmp/python-kurs-check-$$/`
3. Pokaż listę plików, które się różnią (bez treści diff — może być długie)
4. Zaproponuj `odśwież bazę wiedzy` jeśli są różnice

## 4. Pokaż konkretny plik źródłowy

Gdy agent (np. skill `lekcja`) potrzebuje treści dla danego konceptu:

1. Sprawdź `wiedza/INDEX.md` — który plik źródłowy + sekcja odpowiada lekcji
2. Przeczytaj odpowiedni fragment `wiedza/zrodlo/NN-...md`
3. **Sprawdź `wiedza/AKTUALIZACJE.md`** — czy ten temat ma jakąś aktualizację/notatkę o nowoczesnym idiomie

## 5. Lista źródłowych modułów

```
01-wprowadzenie       — Python: czym jest, instalacja, IDE, pierwszy program
02-podstawy           — zmienne, typy (int/float/str/bool), operatory, f-stringi
03-instrukcje         — if/elif/else, for, while, break/continue
04-struktury          — listy, krotki, słowniki, zbiory, zagnieżdżenia
05-funkcje            — def, return, argumenty, scope, moduły
06-pliki              — open/with, czytanie/zapisywanie, try-except, debugger
07-oop                — klasy, __init__, dziedziczenie, polimorfizm, wzorce
08-wyjatki-testy      — raise, custom exceptions, unittest, TDD
09-stdlib             — os, math, datetime, requests, virtualenv, pip
10-prog-funkcyjne     — lambda, map/filter/reduce, comprehensions
11-projekt            — projekt końcowy (scraping/API/analiza)
12-podsumowanie       — PEP8, dalsze kroki, ekosystem (74KB, ostrożnie!)
```

# Repo źródłowe — szczegóły

- **URL:** https://github.com/marianwitkowski/python-kurs-podstawowy
- **Główna gałąź:** `main`
- **Format plików raw:** `https://raw.githubusercontent.com/marianwitkowski/python-kurs-podstawowy/main/{plik}.md`
- **Sprawdzenie ostatniego commita:**
  ```
  curl -s 'https://api.github.com/repos/marianwitkowski/python-kurs-podstawowy/commits?per_page=1' | grep '"date"' | head -1
  ```

# Twarde zasady

- **`wiedza/zrodlo/` jest mirror'em — nie edytuj ręcznie.** Wszystkie aktualizacje merytoryczne idą do `AKTUALIZACJE.md` (jeśli to delta) albo do `wiedza/lekcje/` (jeśli to przerób na sokratejską formę).
- **Zawsze rób backup** przed nadpisaniem `zrodlo/`.
- **Nie usuwaj `AKTUALIZACJE.md`** przy odświeżeniu — to nasz aneks merytoryczny.
- **Nie wykrywaj zmian automatycznie** — odświeżenie wymaga jawnej komendy ucznia/autora.
