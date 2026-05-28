---
name: postep
description: Czyta i atomowo aktualizuje plik postep/student.json — stan ucznia (ukończone lekcje, mocne strony, do powtórki, daty). Każdy zapis idzie przez protokół z backupem i walidacją JSON. Użyj na początku sesji (odczyt) i na końcu sesji / po każdej istotnej zmianie (zapis).
---

# Cel

Trzymać **jeden** plik z pełnym stanem ucznia, by sesje były ciągłe — uczeń wraca i tutor wie, gdzie skończyliśmy. **Bez ryzyka utraty stanu** przy nieudanym zapisie lub uszkodzeniu pliku.

# Plik: `postep/student.json`

## Schemat (schema_version 1)

```json
{
  "schema_version": 1,
  "imie": "Anna",
  "cel": "praca",
  "tempo_godz_tydz": "2-5",
  "rozpoczeto": "2026-05-28",
  "ostatnia_sesja": "2026-05-28",
  "liczba_sesji": 3,
  "aktualna_lekcja": "4.1",
  "ukonczone_lekcje": [
    {"id": "1.1", "data": "2026-05-28", "trudnosc_subiektywna": 1},
    {"id": "1.2", "data": "2026-05-28", "trudnosc_subiektywna": 2},
    {"id": "2.1", "data": "2026-05-29", "trudnosc_subiektywna": 3}
  ],
  "ukonczone_cwiczenia": [
    {"lekcja": "1.1", "poziom": "warmup", "data": "2026-05-28"},
    {"lekcja": "1.1", "poziom": "main",   "data": "2026-05-28"}
  ],
  "mocne_strony": [
    "czytanie traceback",
    "samodzielne dzielenie problemu na kroki"
  ],
  "do_powtorki": [
    {"temat": "rzutowanie typów", "lekcja": "2.1", "data_zauwazenia": "2026-05-29"}
  ],
  "notatki_tutora": [
    "Anna lubi konkretne przykłady z życia. Unikać abstrakcji typu 'foo/bar'."
  ]
}
```

**Pole `schema_version`** jest obowiązkowe. Jeśli odczytasz plik bez tego pola — traktuj jako schemat v0, **dopisz `"schema_version": 1`** przy najbliższym zapisie (migracja jest no-op, pola się nie zmieniły, tylko dodajemy znacznik).

## Pola — opis

| Pole                  | Typ                | Wymagane | Notatki                                              |
| --------------------- | ------------------ | -------- | ---------------------------------------------------- |
| `schema_version`      | int                | tak      | obecnie 1                                            |
| `imie`                | string             | tak      |                                                      |
| `cel`                 | string             | tak      | `praca`/`dane`/`hobby`/`szkoła`/`inne`              |
| `tempo_godz_tydz`     | string             | tak      | `<2`/`2-5`/`5-10`/`10+`                              |
| `rozpoczeto`          | string (YYYY-MM-DD)| tak      |                                                      |
| `ostatnia_sesja`      | string (YYYY-MM-DD)| tak      |                                                      |
| `liczba_sesji`        | int                | tak      |                                                      |
| `aktualna_lekcja`     | string             | tak      | np. `"4.1"` lub `"kurs ukończony"`                  |
| `ukonczone_lekcje`    | array              | tak      | może być `[]`                                        |
| `ukonczone_cwiczenia` | array              | tak      | może być `[]`                                        |
| `mocne_strony`        | array of string    | tak      | może być `[]`, max 5-7 najnowszych                  |
| `do_powtorki`         | array              | tak      | może być `[]`                                        |
| `notatki_tutora`      | array of string    | tak      | może być `[]`, prywatne dla agenta                  |

# Atomowy protokół zapisu — OBOWIĄZKOWY

**Każda modyfikacja `student.json` przechodzi przez ten 7-krokowy protokół.** Bez wyjątków.

```
Krok 1: READ
  cat postep/student.json → tekst

Krok 2: PARSE
  json.loads(tekst) → obiekt
  Jeśli ParseError → STOP, NIE ruszaj pliku, uruchom RECOVERY (patrz niżej)

Krok 3: BACKUP
  TIMESTAMP=$(date +%Y-%m-%d-%H-%M-%S)
  mkdir -p postep/backups
  cp postep/student.json postep/backups/student.${TIMESTAMP}.json

Krok 4: MODIFY (in-memory)
  Zmień tylko konkretne pola w obiekcie.
  NIGDY nie buduj całego JSON-a od zera — to ryzyko utraty pól, których nie znasz.

Krok 5: WRITE TMP
  Zapisz pełny obiekt do postep/student.json.tmp
  (z indent=2, ensure_ascii=False)

Krok 6: VALIDATE
  cat postep/student.json.tmp → tekst_nowy
  json.loads(tekst_nowy) → obiekt_nowy
  Sprawdź wymagane pola (lista wyżej). Jeśli któreś brakuje → STOP, usuń .tmp, NIE ruszaj oryginału.

Krok 7: ATOMIC SWAP
  mv postep/student.json.tmp → postep/student.json
  (mv jest atomowy w POSIX — albo plik jest stary, albo nowy, nigdy "w połowie")
```

**Konkretne komendy Bash do wykonania w jednym wywołaniu:**

```bash
set -e
TIMESTAMP=$(date +%Y-%m-%d-%H-%M-%S)
mkdir -p postep/backups
cp postep/student.json "postep/backups/student.${TIMESTAMP}.json"
# (agent wpisuje nowy JSON do student.json.tmp przez Write)
python3 -c "import json; json.load(open('postep/student.json.tmp', encoding='utf-8'))"
mv postep/student.json.tmp postep/student.json
echo "OK: zapisano, backup: postep/backups/student.${TIMESTAMP}.json"
```

## Cleanup backupów (przy okazji zapisu, opcjonalne)

Co kilka zapisów (lub co tydzień) — usuń backupy starsze niż **30 dni** LUB gdy jest więcej niż **50 sztuk**:

```bash
find postep/backups -name "student.*.json" -mtime +30 -delete
# lub limit liczbowy:
ls -t postep/backups/student.*.json | tail -n +51 | xargs rm -f
```

**Nie kasuj automatycznie bez ostrzeżenia ucznia**, chyba że jest >50 backupów (wtedy info: "wyczyszczono X starych backupów").

# Recovery — gdy student.json jest uszkodzony

Jeśli **Krok 2 (parse)** zwrócił błąd:

1. **NIE NADPISUJ** uszkodzonego pliku (może być wartościowy do diagnostyki)
2. Zmień nazwę: `mv postep/student.json postep/student.broken.${TIMESTAMP}.json`
3. Znajdź najnowszy działający backup:
   ```bash
   ls -t postep/backups/student.*.json | head -1
   ```
4. Sparsuj go — jeśli się parsuje, **zapytaj ucznia**:
   > "Twój plik student.json się uszkodził. Mam działający backup z [data]. Stan: ukończonych lekcji X, aktualna lekcja Y. Przywrócić? [tak/nie]"
5. Po `tak` → `cp <backup> postep/student.json`
6. Po `nie` → uruchom onboarding (traktuj jako nowego ucznia), uszkodzony plik zostaje dla diagnostyki

Jeśli **nie ma żadnych backupów** (np. plik tworzony pierwszy raz, ale parse się nie udał):
- Pokaż uczniowi treść uszkodzonego pliku
- Zapytaj czy chce ręcznie naprawić, czy zacząć od nowa

# Operacje

## Odczyt (start sesji)

1. `cat postep/student.json` → jeśli plik nie istnieje, uczeń jest nowy → onboarding
2. `json.loads(...)` → jeśli błąd → procedura **Recovery** (wyżej)
3. Sprawdź `schema_version`:
   - Brak pola → migracja v0→v1: dopisz `"schema_version": 1` przy następnym zapisie
   - `schema_version: 1` → OK
   - Wyższa wersja → STOP, ostrzeż ucznia (nowsza wersja agenta tworzyła ten plik)
4. Zwróć agentowi:
   - imię
   - `aktualna_lekcja`
   - 2-3 ostatnio ukończone lekcje
   - `do_powtorki`
   - ile dni od `ostatnia_sesja` (jeśli >7 → quiz odświeżający)

## Inicjalizacja (po onboardingu)

Stwórz nowy plik przez atomowy protokół (READ jest pominięty, bo plik nie istnieje):

```json
{
  "schema_version": 1,
  "imie": "<imię>",
  "cel": "<cel>",
  "tempo_godz_tydz": "<tempo>",
  "rozpoczeto": "<dziś>",
  "ostatnia_sesja": "<dziś>",
  "liczba_sesji": 1,
  "aktualna_lekcja": "1.1",
  "ukonczone_lekcje": [],
  "ukonczone_cwiczenia": [],
  "mocne_strony": [],
  "do_powtorki": [],
  "notatki_tutora": []
}
```

## Aktualizacja po ukończonej lekcji

Modyfikacja w pamięci (Krok 4), potem zapis przez protokół:

1. `ukonczone_lekcje.append({"id": "X.Y", "data": "<dziś>", "trudnosc_subiektywna": <1-5>})`
2. `aktualna_lekcja = "<następna>"` (z `kurs/program.md`)
3. `ostatnia_sesja = "<dziś>"`
4. `liczba_sesji += 1` (jeśli to nowa sesja)
5. Opcjonalnie: dopisz do `mocne_strony` / `do_powtorki`

## Aktualizacja po ćwiczeniu

`ukonczone_cwiczenia.append({"lekcja": "N.M", "poziom": "warmup|main|star", "data": "<dziś>"})`

## Powtórki ze słabych miejsc

Gdy uczeń zaliczy temat z `do_powtorki` → usuń wpis z listy (filter).

# Twarde zasady

- **Każdy zapis przez 7-krokowy protokół.** Bez wyjątków, nawet "małych zmian".
- **Backup PRZED każdą modyfikacją** (Krok 3), nie tylko przy resecie.
- **Atomowy `mv`**, NIGDY bezpośredni `Write` na `student.json`.
- **Walidacja JSON po zapisie do .tmp** — jeśli `.tmp` się nie parsuje, NIE ruszaj oryginału.
- **Daty w ISO** `YYYY-MM-DD`.
- **Nie buduj JSON od zera** — czytaj cały obiekt, modyfikuj pola, zapisz cały obiekt. To chroni przed utratą pól, których jeszcze nie znasz (np. dodanych w przyszłej wersji schema).
- **Nie wymyślaj danych.** Jeśli nie wiesz — pytaj ucznia.
- **Notatki tutora** są prywatne — nie pokazuj uczniowi, jeśli sam nie zapyta.

# Przy >7 dniach przerwy

Jeśli `ostatnia_sesja` była ponad tydzień temu:

> "Cześć [imię]! Widzę, że ostatnio rozmawialiśmy [N] dni temu. Chcesz najpierw szybką powtórkę (skill: quiz), czy lecimy dalej z lekcją [aktualna_lekcja]?"

Powtórka = 2-3 pytania ustne z ostatnio ukończonych lekcji. Bez kodu, bez stresu.
