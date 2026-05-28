---
name: postep
description: Czyta i atomowo aktualizuje plik postep/student.json przez helper-skrypt `postep.py`. Każda modyfikacja przechodzi przez atomowy protokół (backup + walidacja + atomic mv) wykonywany przez skrypt — agent NIE składa JSON-a samodzielnie. Użyj na początku sesji (odczyt) i po każdej istotnej zmianie (zapis).
---

# Cel

Trzymać **jeden** plik z pełnym stanem ucznia (`postep/student.json`), z gwarancją że żadna operacja go nie uszkodzi — wszystkie zapisy idą przez deterministyczny skrypt Pythona, **nie przez ręczne składanie JSON-a przez agenta**.

# Zasada twarda — kluczowa

**Agent NIGDY nie wykonuje `Write` ani `Edit` na `postep/student.json` bezpośrednio.**

Wszystkie operacje przez:
```bash
python3 .claude/skills/postep/postep.py <komenda> [argumenty]
```

Skrypt sam wykonuje 7-krokowy protokół: read → migrate → backup → modify → write tmp → validate → atomic mv. Agent tylko **woła go z odpowiednimi argumentami**.

# Schemat student.json (schema_version 2)

```json
{
  "schema_version": 2,
  "imie": "Anna",
  "cel": "praca",
  "tempo_godz_tydz": "2-5",
  "rozpoczeto": "2026-05-28",
  "ostatnia_sesja": "2026-05-28",
  "liczba_sesji": 3,
  "aktualna_lekcja": "4.1",
  "srodowisko": {
    "system": "macOS",
    "python_cmd": "python3",
    "venv_activate": "source .venv/bin/activate",
    "shell": "zsh",
    "edytor": "VS Code"
  },
  "ukonczone_lekcje": [
    {"id": "1.1", "data": "2026-05-28", "trudnosc_subiektywna": 2}
  ],
  "ukonczone_cwiczenia": [
    {"lekcja": "1.1", "poziom": "warmup", "data": "2026-05-28"}
  ],
  "mocne_strony": ["czytanie traceback"],
  "do_powtorki": [
    {"temat": "rzutowanie typów", "lekcja": "2.1", "data_zauwazenia": "2026-05-29"}
  ],
  "notatki_tutora": ["Anna lubi konkretne przykłady z życia"]
}
```

**Migracja schematu** jest automatyczna w skrypcie:
- v0 (bez `schema_version`) → v1 (dopisuje pole)
- v1 → v2 (dopisuje puste `srodowisko`)

# Komendy skryptu

Wszystkie wykonują pełen protokół atomowy. **Zawsze sprawdź exit code** — niezerowy = nie ruszony stary plik.

## Inicjalizacja (po onboardingu)

```bash
python3 .claude/skills/postep/postep.py init \
  --imie "Anna" \
  --cel "hobby" \
  --tempo "2-5" \
  --system "macOS" \
  --python-cmd "python3" \
  --venv-activate "source .venv/bin/activate"
```

Tworzy nowy plik z polami z onboardingu + środowisko zapamiętane z `setup-python`. Domyślne pola (lekcje, ćwiczenia, mocne strony) puste, `liczba_sesji=1`, `aktualna_lekcja="1.1"`.

Błąd jeśli plik już istnieje (chronimy przed nadpisaniem).

## Odczyt

```bash
# Cały stan:
python3 .claude/skills/postep/postep.py read

# Konkretne pole (ścieżka kropkowa):
python3 .claude/skills/postep/postep.py read --field aktualna_lekcja
python3 .claude/skills/postep/postep.py read --field srodowisko.python_cmd
python3 .claude/skills/postep/postep.py read --field do_powtorki
```

## Ustawienie pola

```bash
python3 .claude/skills/postep/postep.py set --field aktualna_lekcja --value "4.2"
python3 .claude/skills/postep/postep.py set --field srodowisko.edytor --value "PyCharm"
```

## Dopisanie ukończonej lekcji

```bash
python3 .claude/skills/postep/postep.py add-lekcja --id "4.1" --trudnosc 3
```

`--trudnosc` to 1-5 (subiektywna ocena ucznia: "1 = banalne, 5 = bardzo trudne"). Pytaj ucznia po lekcji. Skrypt automatycznie aktualizuje `ostatnia_sesja`.

## Dopisanie ukończonego ćwiczenia

```bash
python3 .claude/skills/postep/postep.py add-cwiczenie --lekcja "4.1" --poziom warmup
# --poziom: warmup | main | star
```

## Mocne strony / do powtórki

```bash
python3 .claude/skills/postep/postep.py add-mocna-strona "samodzielne czytanie traceback"
python3 .claude/skills/postep/postep.py add-do-powtorki --temat "rzutowanie typów" --lekcja "2.1"
python3 .claude/skills/postep/postep.py remove-do-powtorki --temat "rzutowanie typów"
```

`add-mocna-strona` automatycznie trzyma max 7 najnowszych. Duplikat = pomijany.
`add-do-powtorki` nie dubluje tego samego tematu.

## Środowisko (system, komenda Pythona itp.)

```bash
python3 .claude/skills/postep/postep.py update-srodowisko \
  --system "Windows" \
  --python-cmd "py" \
  --venv-activate ".venv\\Scripts\\Activate.ps1"
```

Można podać dowolny podzbiór pól — tylko one zostaną zmienione. Reszta nietknięta.

## Notatki tutora (prywatne dla agenta)

```bash
python3 .claude/skills/postep/postep.py add-notatka "Anna woli konkretne przykłady z życia"
```

Max 20 najnowszych. **Nie pokazuj uczniowi** jeśli sam nie zapyta.

## Zakończenie sesji

```bash
python3 .claude/skills/postep/postep.py end-session
```

Aktualizuje `ostatnia_sesja=dziś` i `liczba_sesji+=1`. Wywołuj **raz** na koniec każdej sesji rozmowy.

## Recovery (gdy student.json uszkodzony)

```bash
python3 .claude/skills/postep/postep.py recovery
```

Skrypt szuka najnowszego **działającego** backupu w `postep/backups/`, przenosi uszkodzony do `postep/student.broken.<TS>.json` (NIE kasuje), kopiuje backup na miejsce. Wypisuje krótkie podsumowanie przywróconego stanu.

# Procedura sesji

## Start sesji

1. **Odczyt:**
   ```bash
   python3 .claude/skills/postep/postep.py read
   ```
2. Jeśli błąd "plik nie istnieje" → uczeń nowy, uruchom onboarding.
3. Jeśli błąd "JSON nie parsuje się" → uruchom `recovery` (zapytaj ucznia najpierw).
4. W normalnym przypadku — zwróć agentowi:
   - `imie`, `aktualna_lekcja`
   - 2-3 ostatnie wpisy z `ukonczone_lekcje`
   - `do_powtorki` (jeśli niepusta)
   - liczbę dni od `ostatnia_sesja` (jeśli >7 → quiz odświeżający)
   - `srodowisko.python_cmd` i `srodowisko.venv_activate` (do używania w lekcji!)

## Onboarding (pierwsza sesja)

Po wywiadzie + skill `setup-python` (który zna system i komendę Pythona):

```bash
python3 .claude/skills/postep/postep.py init \
  --imie <imię_z_wywiadu> \
  --cel <cel> \
  --tempo <tempo> \
  --system <z_setup-python> \
  --python-cmd <z_setup-python> \
  --venv-activate <z_setup-python>
```

## Po każdej ukończonej lekcji

1. Pytaj ucznia: "Od 1 do 5, jak trudna była ta lekcja?"
2. `add-lekcja --id <X.Y> --trudnosc <N>`
3. `set --field aktualna_lekcja --value <następna_z_INDEX.md>`
4. Opcjonalnie: `add-mocna-strona` lub `add-do-powtorki` jeśli było coś specjalnego.

## Po każdym ukończonym ćwiczeniu

```bash
python3 .claude/skills/postep/postep.py add-cwiczenie --lekcja <X.Y> --poziom <P>
```

## Koniec sesji rozmowy

```bash
python3 .claude/skills/postep/postep.py end-session
```

# Backupy

Skrypt automatycznie tworzy backup do `postep/backups/student.{ISO_timestamp}.json` przed każdą modyfikacją.

**Nie kasuj backupów automatycznie.** Jeśli `postep/backups/` rośnie (>50 plików), powiadom ucznia:

> "Masz 53 backupy `student.json`. Najstarszy: 2026-01-15. Chcesz przenieść te starsze niż 30 dni do `postep/backups/_old/`?"

Po `tak`:
```bash
mkdir -p postep/backups/_old
# Lista plików starszych niż 30 dni i ręczny mv (NIE find -delete!)
```

# Przy >7 dniach przerwy

```bash
LAST=$(python3 .claude/skills/postep/postep.py read --field ostatnia_sesja | tr -d '"')
# Porównaj z dzisiejszą datą; jeśli >7 dni:
```

Powiedz uczniowi:
> "Cześć [imię]! Widzę, że ostatnio rozmawialiśmy [N] dni temu. Chcesz najpierw szybką powtórkę (skill: quiz), czy lecimy dalej z lekcją [aktualna_lekcja]?"

# Twarde zasady

- **NIGDY** bezpośredni `Write` / `Edit` na `student.json`. ZAWSZE przez skrypt.
- **NIGDY** nie buduj nowego JSON-a "z pamięci" — skrypt czyta, modyfikuje konkretne pola, zapisuje. To chroni przed utratą pól dodanych w przyszłej wersji schematu.
- **Backup ZAWSZE** — skrypt robi sam, ale jeśli musisz coś ręcznie (np. odczyt jako JSON do analizy) — pamiętaj, że to nie modyfikacja.
- **Nie wymyślaj danych.** Nie wiesz wartości → pytaj ucznia.
- **`notatki_tutora` są prywatne** — agent ich nie pokazuje uczniowi bez prośby.
- **Daty** zawsze ISO `YYYY-MM-DD` — skrypt robi to za Ciebie.

# Test poprawności (opcjonalny, dla autora)

Ze świeżego katalogu można przetestować skrypt:
```bash
cd /tmp && rm -rf testowy && mkdir -p testowy/postep testowy/wiedza
cp .claude/skills/postep/postep.py /tmp/testowy/
cd /tmp/testowy
python3 postep.py init --imie Test --cel hobby --tempo "2-5"
python3 postep.py add-lekcja --id 1.1 --trudnosc 2
python3 postep.py read
```
