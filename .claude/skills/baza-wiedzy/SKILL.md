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

## 0. Krok wstępny — weryfikacja spójności (każda komenda)

**ZAWSZE** na początku **dowolnej** komendy bazy wiedzy (`refresh`, `check`, `status`, `rollback`, podgląd plików) wywołaj funkcję `verify_state`. Wykrywa ślady przerwanych aktualizacji (SIGKILL, padło zasilanie, agent zatrzymany w połowie).

```bash
verify_state() {
  # Sygnał 1: brak wiedza/zrodlo + istnieje wiedza/zrodlo.backup-*
  # → poprzednia aktualizacja padła między mv-A (zrodlo → backup) i mv-B (zrodlo.new → zrodlo)
  if [ ! -d wiedza/zrodlo ]; then
    NEWEST_BACKUP=$(ls -dt wiedza/zrodlo.backup-* 2>/dev/null | head -1)
    if [ -n "$NEWEST_BACKUP" ]; then
      echo "SIGNAL_1:$NEWEST_BACKUP"
      return 1
    fi
  fi

  # Sygnał 2: istnieje wiedza/zrodlo.new (pozostały po nieudanym buildzie)
  if [ -d wiedza/zrodlo.new ]; then
    echo "SIGNAL_2:wiedza/zrodlo.new"
    return 2
  fi

  # Sygnał 3: VERSION.json brak (baza z czasu sprzed wersjonowania — info, nie błąd)
  if [ -d wiedza/zrodlo ] && [ ! -f wiedza/zrodlo/VERSION.json ]; then
    echo "SIGNAL_3:no_version"
    return 3
  fi

  return 0
}

VERIFY_CODE=0
verify_state || VERIFY_CODE=$?
```

### Kanoniczny wzorzec wywołania

**ZAWSZE** używaj `VERIFY_CODE=0; verify_state || VERIFY_CODE=$?` — niezależnie od kontekstu (pod `set -e` czy bez). Spójność i bezpieczeństwo. Nigdy `verify_state; VERIFY_CODE=$?` (pod `set -e` shell aborterę zanim agent odczyta kod).

Pełne użycie:

```bash
set -e
# ...inne komendy...

VERIFY_CODE=0
verify_state || VERIFY_CODE=$?    # `||` chroni przed set -e abort

case $VERIFY_CODE in
  1) # Sygnał 1: brak zrodlo + jest backup → zapytaj ucznia
     echo "Wykryto przerwaną aktualizację, pytam ucznia..."
     # ...handler kodu 1...
     ;;
  2) # Sygnał 2: zostawiony zrodlo.new → handle
     # ...handler kodu 2...
     ;;
  3) # Sygnał 3: brak VERSION.json → informuj, kontynuuj
     echo "ℹ️  Brak VERSION.json — kontynuuję bez wersjonowania"
     ;;
  0) ;;  # zdrowy stan, kontynuuj
esac
```

**Anty-wzorzec (NIGDY):**
```bash
verify_state              # pod set -e abort przy return 1/2/3
VERIFY_CODE=$?            # tu nie dojdzie
```

### Reakcja agenta na każdy sygnał

**Sygnał 1 (kod 1):** `wiedza/zrodlo/` zniknął, jest najnowszy backup → wysokie prawdopodobieństwo przerwanej aktualizacji.

Agent **zatrzymuje wszystkie inne operacje** i pyta ucznia:

> "⚠️ Wykryłem ślady przerwanej aktualizacji bazy wiedzy:
> - `wiedza/zrodlo/` nie istnieje
> - Jest backup: `[NEWEST_BACKUP]` (SHA: [z VERSION.json], data: [...])
>
> Prawdopodobnie poprzednia aktualizacja została przerwana (SIGKILL, padło zasilanie, agent się zatrzymał między dwoma mv).
>
> Co robimy?
> - **`przywróć`** → odzyskaj `wiedza/zrodlo/` z backupu (zalecane — bezpieczne, nic nie tracimy)
> - **`pomiń`** → zostawiam jak jest (nie znajdę materiałów do lekcji — kurs nie ruszy)
> - **`usuń backup`** → wyrzuć backup (NIE polecane — utrata danych)"

Po `przywróć`:
```bash
mv "$NEWEST_BACKUP" wiedza/zrodlo
echo "OK: przywrócono wiedza/zrodlo z $NEWEST_BACKUP"
```

**Sygnał 2 (kod 2):** `wiedza/zrodlo.new` pozostał z nieudanego buildu.

Agent informuje i proponuje:

> "ℹ️ Wykryłem `wiedza/zrodlo.new/` z poprzedniej, nieudanej próby aktualizacji. Co robimy?
> - **`przenieś do failed`** → mv na `wiedza/zrodlo.new.failed-[TS]` (bezpieczne — można przejrzeć)
> - **`pomiń`** → zostawiam jak jest (kolejna aktualizacja może to nadpisać)"

Po `przenieś do failed`:
```bash
TIMESTAMP=$(python3 -c "from datetime import datetime; print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'))")
mv wiedza/zrodlo.new "wiedza/zrodlo.new.failed-${TIMESTAMP}"
```

**Sygnał 3 (kod 3):** Brak `VERSION.json`. Baza pochodzi z pierwszego pobrania (przed wprowadzeniem wersjonowania).

Agent **kontynuuje** żądaną operację, ale dopisuje informacyjnie:

> "ℹ️ Baza nie ma `VERSION.json` (pochodzi sprzed wersjonowania). Zalecane: `odśwież bazę wiedzy`, by wpisać aktualny SHA."

**Kod 0:** Stan spójny — agent kontynuuje bez powiadomień.

### Twarda reguła

**Żadna komenda bazy wiedzy nie wykonuje się bez wcześniejszego `verify_state`.** Jeśli zapomniałeś — uczeń może dostać niespójne wyniki (np. `pokaż stan bazy` zwróci dane z backupu, którego nie zauważyłeś).

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

### Kroki 7-9: ATOMOWY blok build + swap z automatycznym rollback

**Kluczowe:** Wszystkie operacje modyfikujące `wiedza/zrodlo/` muszą iść w **jednym bloku bash** z `set -e; trap rollback ERR`. To gwarantuje, że jeśli cokolwiek padnie (mv, kopiowanie, walidacja, sieć) — rollback wykona się automatycznie, bez zależności od tego, czy agent zdąży zareagować.

Wykonaj jako **pojedynczy** `bash -c "..."` lub w jednym wywołaniu shell:

```bash
set -e
TIMESTAMP=$(python3 -c "from datetime import datetime; print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'))")
NEW_DIR="wiedza/zrodlo.new"
BACKUP="wiedza/zrodlo.backup-${TIMESTAMP}"

# Funkcja rollback wywoływana automatycznie przy każdym błędzie
rollback() {
  local exit_code=$?
  echo ""
  echo "==================== BŁĄD — wykonuję automatyczny rollback ===================="

  # Sytuacja 1: backup utworzony, ale zrodlo nie ma na miejsce (padło między mv-A i mv-B)
  if [ ! -d wiedza/zrodlo ] && [ -d "$BACKUP" ]; then
    mv "$BACKUP" wiedza/zrodlo
    echo "ROLLBACK A: przywrócono wiedza/zrodlo z backupu"
  fi

  # Sytuacja 2: zrodlo.new istnieje (nieudany build) — przenieś do failed
  if [ -d "$NEW_DIR" ]; then
    mv "$NEW_DIR" "${NEW_DIR}.failed-${TIMESTAMP}"
    echo "ROLLBACK B: nieudany zrodlo.new przeniesiony do ${NEW_DIR}.failed-${TIMESTAMP}"
  fi

  echo "Stan po rollback:"
  ls -d wiedza/zrodlo* 2>/dev/null || echo "  (brak wiedza/zrodlo*)"
  echo "================================================================================"
  exit $exit_code
}
trap rollback ERR

# --- Krok 7: build zrodlo.new równolegle ---

# Jeśli stary zrodlo.new pozostał z poprzedniej awarii — zarchiwizuj (NIE kasuj)
if [ -d "$NEW_DIR" ]; then
  mv "$NEW_DIR" "${NEW_DIR}.stale-${TIMESTAMP}"
  echo "INFO: stary zrodlo.new przeniesiony do ${NEW_DIR}.stale-${TIMESTAMP}"
fi

mkdir -p "$NEW_DIR"
cp "${TMP}"/*.md "$NEW_DIR"/

# --- Krok 8: VERSION.json + walidacja ---

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
with open('${NEW_DIR}/VERSION.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
"

# Walidacja: dokładnie 13 plików .md w zrodlo.new (rzuca błąd → trap → rollback)
FILES_COUNT=$(ls "$NEW_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')
[ "$FILES_COUNT" = "13" ] || { echo "BŁĄD walidacji: oczekiwane 13 plików, znalezione $FILES_COUNT"; exit 1; }

# Walidacja: VERSION.json parsuje się
python3 -c "import json; json.load(open('${NEW_DIR}/VERSION.json'))"

# --- Krok 9: atomowy swap przez 2x mv ---
# Każdy mv jest atomowy w POSIX. Jeśli drugi mv padnie, trap rollback przywróci backup.

if [ -d wiedza/zrodlo ]; then
  mv wiedza/zrodlo "$BACKUP"      # mv-A: jeśli padnie tu, nie zostawiamy uszkodzeń
fi
mv "$NEW_DIR" wiedza/zrodlo         # mv-B: jeśli padnie tu, trap wykryje brak zrodlo + obecność backup

# --- Sukces — wyłącz trap i powiadom ---
trap - ERR
echo "OK: zaktualizowano wiedza/zrodlo/ do SHA ${SHA:0:7}"
echo "Backup poprzedniej wersji: ${BACKUP}"
echo "(Backup zostaje. Aby zarchiwizować po sprawdzeniu: mv ${BACKUP} wiedza/_old/)"
```

**Co się stanie w różnych scenariuszach awarii:**

| Co padło                                | Co robi `trap rollback`                                |
| --------------------------------------- | ------------------------------------------------------ |
| `cp` plików z `/tmp` do `zrodlo.new`    | `zrodlo` nietknięty, `zrodlo.new` → `failed-<TS>`     |
| Walidacja (FILES_COUNT ≠ 13)            | jw.                                                    |
| `python3 -c` zapisujący VERSION.json    | jw.                                                    |
| mv-A (`zrodlo → backup`)                | rzadkie, `mv` rzadko pada; backup nie istnieje → trap zostawia `zrodlo` nietknięty + `zrodlo.new` → failed |
| mv-B (`zrodlo.new → zrodlo`)            | `zrodlo` nie istnieje, backup istnieje → trap robi `backup → zrodlo`. `zrodlo.new` (jeśli pozostał) → `failed-<TS>` |
| SIGKILL / out-of-memory między mv-A i mv-B | trap nie odpali (proces zabity); ale następne uruchomienie protokołu zobaczy `BACKUP` + brak `zrodlo` i wykona „Awaryjny manualny rollback" (sekcja niżej) |

### Krok 10: cleanup /tmp

`/tmp/` może być usunięty (system i tak go czyści, ale dla porządku):
```bash
rm -rf "${TMP}"
```

To **jedyne** dozwolone `rm -rf` w tym protokole — `/tmp/` jest publicznie ulotne.

### Krok 11: powiadomienie

Powiedz uczniowi:
- Zaktualizowano do SHA `${SHA:0:7}` (data commita: ${DATE})
- Backup: `wiedza/zrodlo.backup-${TIMESTAMP}/`
- Wyczyszczono `/tmp/...`
- Przypomnienie: "Jeśli widoczne były zmiany merytoryczne, warto przejrzeć `wiedza/AKTUALIZACJE.md` (czy nasze delty nadal trafne) i ewentualnie zaktualizować notatki w `wiedza/lekcje/`."

### Awaryjne — manualny rollback (bez `rm -rf`)

Jeśli po aktualizacji okaże się, że coś nie działa:

```bash
TIMESTAMP=$(python3 -c "from datetime import datetime; print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'))")
# Przenieś obecną (nieudaną) wersję do failed/, NIE kasuj:
mv wiedza/zrodlo "wiedza/zrodlo.failed-${TIMESTAMP}"
# Przywróć backup:
mv wiedza/zrodlo.backup-<TIMESTAMP_BACKUPU> wiedza/zrodlo
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
2. Pokaż uczniowi listę z datami + SHA (z każdego `VERSION.json` w backupie, jeśli jest)
3. Po wyborze:
   ```bash
   TIMESTAMP=$(python3 -c "from datetime import datetime; print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'))")
   # Obecną wersję przenieś do failed/, NIE kasuj:
   mv wiedza/zrodlo "wiedza/zrodlo.failed-${TIMESTAMP}"
   # Przywróć wybrany backup:
   mv "wiedza/zrodlo.backup-${WYBRANY}" wiedza/zrodlo
   ```
4. Potwierdź: "Przywrócono z `zrodlo.backup-${WYBRANY}` (SHA: <z VERSION.json>). Poprzednia wersja zachowana w `zrodlo.failed-${TIMESTAMP}/` (możesz usunąć ręcznie po sprawdzeniu)."

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
- **Buduj `wiedza/zrodlo.new/` równolegle**, walidacja, dopiero potem swap. Nigdy nie modyfikuj `zrodlo/` "po fragmencie".
- **Atomowy swap przez `mv`** — najpierw `zrodlo → zrodlo.backup-<TS>`, potem `zrodlo.new → zrodlo`. Bez `rm -rf` na `wiedza/zrodlo/`.
- **Mirror właściwy** — przez `zrodlo.new` zachowujemy semantykę mirror'a: jeśli zdalne repo usunęło plik, lokalny też.
- **Rollback automatyczny** — jeśli swap padnie między mv-A i mv-B, agent przywraca z backupu.
- **Nieudane operacje archiwizuj** — `*.failed-<TS>/`, NIE `rm -rf`.
- **`VERSION.json`** trzymany w `wiedza/zrodlo/VERSION.json` z SHA + datami. **Commituj do gita** — pokazuje innym, z jakiego stanu pochodzi baza.
- **Nie usuwaj `AKTUALIZACJE.md`** przy odświeżeniu — to nasz aneks merytoryczny.
- **Nie wykrywaj zmian automatycznie** — odświeżenie wymaga jawnej komendy ucznia/autora.
- **Nie czyść backupów automatycznie** — uczeń sam decyduje, kiedy je usunąć. Zalecana ścieżka: po sprawdzeniu nowej wersji `mv wiedza/zrodlo.backup-* wiedza/_old/` zamiast `rm -rf`.
