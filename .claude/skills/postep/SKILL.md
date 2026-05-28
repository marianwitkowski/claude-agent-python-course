---
name: postep
description: Czyta i aktualizuje plik postep/student.json — stan ucznia (ukończone lekcje, mocne strony, do powtórki, daty). Tworzy plik przy onboardingu, aktualizuje po każdej lekcji i ćwiczeniu. Użyj na początku sesji (odczyt) i na końcu sesji (zapis).
---

# Cel

Trzymać **jeden** plik z pełnym stanem ucznia, by sesje były ciągłe — uczeń wraca i tutor wie, gdzie skończyliśmy.

# Plik: `postep/student.json`

## Schemat

```json
{
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

## Operacje

### Odczyt (start sesji)

Zawsze na początku rozmowy:

1. Próbuj odczytać `postep/student.json`.
2. Jeśli **plik nie istnieje** → uczeń jest nowy, agent uruchamia onboarding.
3. Jeśli istnieje → zwróć agentowi:
   - imię
   - `aktualna_lekcja`
   - 2-3 ostatnio ukończone lekcje (do przypomnienia kontekstu)
   - cokolwiek z `do_powtorki`
   - ile dni od `ostatnia_sesja` (jeśli >7, zaproponuj quiz odświeżający)

### Inicjalizacja (po onboardingu)

Po wywiadzie wstępnym i wygenerowaniu programu — utwórz plik z polami:
- `imie`, `cel`, `tempo_godz_tydz`, `rozpoczeto` (dzisiaj), `ostatnia_sesja` (dzisiaj)
- `liczba_sesji: 1`
- `aktualna_lekcja: "1.1"`
- pozostałe pola — puste listy / tablice

### Aktualizacja po ukończonej lekcji

1. Dodaj wpis do `ukonczone_lekcje` z dzisiejszą datą i `trudnosc_subiektywna` 1-5 (pytaj ucznia: "od 1 do 5, jak trudna była ta lekcja?")
2. Ustaw `aktualna_lekcja` na kolejną z `kurs/program.md`
3. Zaktualizuj `ostatnia_sesja` na dziś
4. Jeśli uczeń coś szczególnie dobrze zrobił → dopisz do `mocne_strony` (max 5-7 pozycji, najnowsze)
5. Jeśli uczeń się potknął na koncepcie → dopisz do `do_powtorki`

### Aktualizacja po ćwiczeniu

Dopisz wpis do `ukonczone_cwiczenia`:
```json
{"lekcja": "N.M", "poziom": "warmup|main|star", "data": "YYYY-MM-DD"}
```

### Powtórki ze słabych miejsc

Gdy uczeń zaliczy temat z `do_powtorki` (sprawdzasz w późniejszym ćwiczeniu, że już go umie) — usuń wpis z listy.

# Twarde zasady

- **Plik MUSI być poprawnym JSON-em** po każdej operacji. Walidacja: po zapisie odczytaj i sparsuj.
- **Nie nadpisuj całego pliku** bez powodu — czytaj, modyfikuj, zapisuj. To zabezpieczenie przed utratą danych.
- **Daty w formacie ISO** `YYYY-MM-DD`.
- **Nie wymyślaj danych.** Jeśli nie wiesz, ile lekcja trwała — nie zgaduj. Pytaj ucznia lub pomiń pole.
- **Notatki tutora** są prywatne — nie pokazuj ich uczniowi, jeśli sam nie zapyta.

# Przy >7 dniach przerwy

Jeśli `ostatnia_sesja` była ponad tydzień temu — zacznij od:

> "Cześć [imię]! Widzę, że ostatnio rozmawialiśmy [N] dni temu. Chcesz najpierw szybką powtórkę, czy lecimy dalej z lekcją [aktualna_lekcja]?"

Powtórka = 2-3 pytania ustne z ostatnio ukończonych lekcji. Bez kodu, bez stresu.
