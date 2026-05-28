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
├── INDEX.md                      # mapowanie 12 modułów źródłowych → 39 lekcji sokratejskich
└── lekcje/                       # generowane lekcje (sokratejskie wersje z notatkami tutora)
    ├── 01.01-pierwszy-print.md
    ├── 01.02-czytanie-bledow.md
    └── ...
```

**Reguła:** `zrodlo/` to czysty mirror — nie edytujemy tu. Zmiany merytoryczne lądują w `AKTUALIZACJE.md` (delta) lub w `lekcje/*.md` (już przerobione na sokratejskie).

# Operacje

## 1. Odśwież bazę (pobierz najnowszą wersję)

**Protokół 9-krokowy** z walidacją, podglądem diff i rollbackiem. Nigdy nie ruszamy `wiedza/zrodlo/`, dopóki **wszystko** w `/tmp/` nie przejdzie walidacji.

Po komendzie `odśwież bazę wiedzy`:

### Krok 1: pobierz SHA i metadata ze zdalnego repo

```bash
SHA=$(curl -s 'https://api.github.com/repos/marianwitkowski/python-kurs-podstawowy/commits/main' \
  | grep -m1 '"sha"' | head -1 | cut -d'"' -f4)
DATE=$(curl -s "https://api.github.com/repos/marianwitkowski/python-kurs-podstawowy/commits/${SHA}" \
  | grep -m1 '"date"' | cut -d'"' -f4)
echo "Remote SHA: ${SHA}, date: ${DATE}"
```

Jeśli `SHA` jest pusty → STOP (brak sieci, API down, rate limit). Nie ruszaj nic.

### Krok 2: porównaj z lokalnym `VERSION.json`

```bash
if [ -f wiedza/zrodlo/VERSION.json ]; then
  LOCAL_SHA=$(python3 -c "import json; print(json.load(open('wiedza/zrodlo/VERSION.json'))['sha'])")
  echo "Local SHA:  ${LOCAL_SHA}"
fi
```

- **Jeśli `SHA == LOCAL_SHA`** → "Baza już aktualna (commit ${SHA:0:7} z ${DATE}). Nic do roboty." STOP.
- **Jeśli różne lub brak `VERSION.json`** → kontynuuj.

### Krok 3: pobierz pliki do katalogu tymczasowego

```bash
TMP="/tmp/python-kurs-update-${SHA:0:7}"
rm -rf "${TMP}" && mkdir -p "${TMP}"

FILES="01-wprowadzenie 02-podstawy 03-instrukcje 04-struktury 05-funkcje \
       06-pliki 07-oop 08-wyjatki-testy 09-stdlib 10-prog-funkcyjne \
       11-projekt 12-podsumowanie README"

ALL_OK=true
for f in $FILES; do
  URL="https://raw.githubusercontent.com/marianwitkowski/python-kurs-podstawowy/${SHA}/${f}.md"
  HTTP=$(curl -sL -w "%{http_code}" -o "${TMP}/${f}.md" "$URL")
  if [ "$HTTP" != "200" ]; then
    echo "FAIL ${f}.md (HTTP ${HTTP})"
    ALL_OK=false
  fi
done

$ALL_OK || { echo "STOP: nie wszystkie pliki pobrały się"; rm -rf "${TMP}"; exit 1; }
```

Pobieramy z **konkretnego SHA** (nie z `main`) — gwarantuje, że jeśli pobieranie zajmie kilka sekund a w międzyczasie ktoś commitnie do main, dostaniemy spójny snapshot.

### Krok 4: walidacja każdego pliku

Dla każdego pobranego pliku:

```bash
for f in $FILES; do
  PATH_TMP="${TMP}/${f}.md"
  SIZE=$(wc -c < "$PATH_TMP")
  FIRST_CHARS=$(head -c 200 "$PATH_TMP")

  # 1. rozmiar > 500 bajtów (nie pusta strona błędu / 404)
  [ "$SIZE" -lt 500 ] && { echo "FAIL ${f}.md: za mały (${SIZE} B)"; ALL_OK=false; continue; }

  # 2. nie zaczyna się od "<!DOCTYPE" lub "<html" (nie HTML zamiast markdown)
  echo "$FIRST_CHARS" | grep -qi "<!DOCTYPE\|<html" && { echo "FAIL ${f}.md: HTML zamiast .md"; ALL_OK=false; continue; }

  # 3. zawiera markdown (# nagłówek lub --- frontmatter)
  echo "$FIRST_CHARS" | grep -qE "^#|^---" || { echo "FAIL ${f}.md: nie wygląda jak markdown"; ALL_OK=false; continue; }

  echo "OK   ${f}.md (${SIZE} B)"
done

$ALL_OK || { echo "STOP: walidacja nie przeszła"; rm -rf "${TMP}"; exit 1; }
```

### Krok 5: pokaż diff uczniowi (PRZED nadpisaniem)

```bash
echo ""
echo "=== Zmiany ==="
for f in $FILES; do
  LOCAL="wiedza/zrodlo/${f}.md"
  REMOTE="${TMP}/${f}.md"
  if [ ! -f "$LOCAL" ]; then
    echo "NEW    ${f}.md ($(wc -c < $REMOTE) B)"
  elif ! cmp -s "$LOCAL" "$REMOTE"; then
    OLD=$(wc -c < "$LOCAL")
    NEW=$(wc -c < "$REMOTE")
    DIFF_LINES=$(diff "$LOCAL" "$REMOTE" | wc -l)
    echo "MOD    ${f}.md (${OLD} → ${NEW} B, ${DIFF_LINES} linii diff)"
  fi
done
```

Pokaż również:
- Lokalny SHA (jeśli istniał) vs nowy SHA
- Data nowego commita
- Liczba zmienionych plików

### Krok 6: poproś o potwierdzenie

> "Pobrałem 13 plików z commita ${SHA:0:7} (${DATE}). Powyżej widzisz, które się zmieniły. Zaktualizować lokalną bazę? Wymagana jawna odpowiedź: **tak, zaktualizuj**."

Inna odpowiedź → STOP, `rm -rf ${TMP}`, koniec.

### Krok 7: backup obecnej `zrodlo/`

```bash
TIMESTAMP=$(date +%Y-%m-%d-%H-%M-%S)
BACKUP="wiedza/zrodlo.backup-${TIMESTAMP}"
[ -d wiedza/zrodlo ] && cp -r wiedza/zrodlo "$BACKUP"
echo "Backup: $BACKUP"
```

### Krok 8: atomowy swap (z możliwością rollback)

```bash
set -e
ROLLBACK() {
  echo "BŁĄD — przywracam stan poprzedni"
  rm -rf wiedza/zrodlo
  mv "$BACKUP" wiedza/zrodlo
  exit 1
}
trap ROLLBACK ERR

# Skopiuj wszystkie pliki z /tmp do zrodlo/
mkdir -p wiedza/zrodlo
cp "${TMP}"/*.md wiedza/zrodlo/

# Zapisz VERSION.json
python3 -c "
import json
from datetime import datetime, timezone
data = {
    'sha': '${SHA}',
    'commit_date': '${DATE}',
    'pobrane': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'plikow': 13,
    'zrodlo': 'https://github.com/marianwitkowski/python-kurs-podstawowy'
}
with open('wiedza/zrodlo/VERSION.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
"

trap - ERR
echo "OK: zaktualizowano do ${SHA:0:7}"
echo "Backup: ${BACKUP}"
echo "Wyczyść backup gdy upewnisz się że nowa wersja działa: rm -rf ${BACKUP}"
```

### Krok 9: powiadomienie

Powiedz uczniowi:
- Zaktualizowano do SHA `${SHA:0:7}` (data commita: ${DATE})
- Backup: `wiedza/zrodlo.backup-${TIMESTAMP}/`
- Wyczyszczono `/tmp/...`
- Przypomnienie: "Jeśli widoczne były zmiany merytoryczne, warto przejrzeć `wiedza/AKTUALIZACJE.md` (czy nasze delty nadal trafne) i ewentualnie zaktualizować notatki w `wiedza/lekcje/`."

### Awaryjne — manualny rollback

Jeśli po aktualizacji okaże się, że coś nie działa:

```bash
rm -rf wiedza/zrodlo
mv wiedza/zrodlo.backup-${TIMESTAMP} wiedza/zrodlo
```

Lub komenda dla agenta: `przywróć poprzednią wersję bazy wiedzy` → użyje najnowszego `zrodlo.backup-*`.

## 2. Stan bazy wiedzy

Gdy uczeń mówi "pokaż stan bazy" / "co jest w bazie":

Najpierw odczytaj `wiedza/zrodlo/VERSION.json` (jeśli istnieje):
```bash
[ -f wiedza/zrodlo/VERSION.json ] && cat wiedza/zrodlo/VERSION.json
```

Wypisz uczniowi:
- **Lokalny SHA** (z VERSION.json) i data commita
- **Data ostatniego pobrania** (z VERSION.json `pobrane`)
- Liczba plików w `wiedza/zrodlo/` (powinno być 13)
- Data ostatniego commita w **zdalnym** repo (z GitHub API) — porównaj z lokalnym
- Liczba wygenerowanych lekcji w `wiedza/lekcje/` (powinno być 39 + szablon = 40)
- Lista backupów `wiedza/zrodlo.backup-*` z datami
- Czy `AKTUALIZACJE.md` istnieje

Jeśli `VERSION.json` **nie istnieje** → baza pochodzi z pierwszego pobrania (przed wprowadzeniem VERSION.json). Zaproponuj odświeżenie, by zapisać aktualny SHA.

## 3. Sprawdź różnice ze zdalnym repo (dry-run)

Gdy uczeń mówi "sprawdź czy baza aktualna" / "diff bazy":

Wykonaj **kroki 1-5** z protokołu "Odśwież bazę" (pobranie SHA, walidacja, diff), **ale BEZ Kroku 7-8** (bez backupu, bez nadpisywania). Po pokazaniu diffu zapytaj: "Czy chcesz teraz wykonać aktualizację? (tak/nie)".

To "dry-run" — tylko informacja, nic nie modyfikuje.

## 4. Przywróć poprzednią wersję bazy

Gdy uczeń mówi "przywróć poprzednią bazę wiedzy" / "rollback bazy":

1. Wylistuj backupy: `ls -dt wiedza/zrodlo.backup-*`
2. Pokaż uczniowi listę z datami
3. Po wyborze (lub jeśli jest tylko jeden, automatycznie):
   ```bash
   rm -rf wiedza/zrodlo
   mv wiedza/zrodlo.backup-${WYBRANY} wiedza/zrodlo
   ```
4. Potwierdź: "Przywrócono z `${WYBRANY}`. SHA: <z VERSION.json>"

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
- **Pobieranie tylko z konkretnego SHA**, nie z `main` — gwarancja spójności snapshotu.
- **Pobieranie ZAWSZE najpierw do `/tmp/`** i walidacja przed dotknięciem `wiedza/zrodlo/`.
- **Walidacja każdego pliku:** rozmiar >500B, nie HTML, zaczyna się od `#` lub `---`.
- **Backup przed nadpisaniem** — `wiedza/zrodlo.backup-${TIMESTAMP}/`. Backup ZAWSZE, niezależnie od wielkości zmian.
- **Rollback automatyczny** przy błędzie w trakcie kopiowania (przez `trap ERR`).
- **`VERSION.json`** trzymany w `wiedza/zrodlo/VERSION.json` z SHA + datami. **Commituj do gita** — pokazuje innym, z jakiego stanu pochodzi baza.
- **Nie usuwaj `AKTUALIZACJE.md`** przy odświeżeniu — to nasz aneks merytoryczny.
- **Nie wykrywaj zmian automatycznie** — odświeżenie wymaga jawnej komendy ucznia/autora.
- **Nie czyść backupów automatycznie** — uczeń sam decyduje, kiedy je usunąć (`rm -rf wiedza/zrodlo.backup-*` po upewnieniu się, że nowa wersja działa).
