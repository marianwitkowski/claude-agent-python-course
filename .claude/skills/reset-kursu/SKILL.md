---
name: reset-kursu
description: Resetuje stan kursu (miękko lub w pełni), zawsze robi backup do `postep/archiwum/`. Miękki reset czyści tylko postęp i program — kod ucznia zostaje. Pełny reset usuwa wszystko poza skillami i instrukcją. Wymaga jawnego potwierdzenia od ucznia. Użyj gdy uczeń mówi "zresetuj kurs", "zacznij od nowa", "wyczyść postęp", "chcę nowy plan".
---

# Cel

Pozwolić uczniowi zacząć od nowa **bez utraty pracy** — backup robisz **zawsze**, nawet przy "pełnym" resecie. Dane nigdy nie giną, tylko schodzą z głównej ścieżki.

# Dwa tryby

| Tryb              | Co czyści                                            | Co zostawia                          | Kiedy              |
| ----------------- | ---------------------------------------------------- | ------------------------------------ | ------------------ |
| Miękki 🧽         | `postep/student.json`, `kurs/program.md`             | Cały Twój kod w `kurs/zadania/`, notatki w `kurs/lekcje/` | Chcesz nowy program kursu, ale zachować dotychczasowe ćwiczenia |
| Pełny 🔥          | Wszystko: postęp, program, notatki, kod ucznia       | Tylko `.claude/`, `README.md`, `kurs/JAK-PISAC-KOD.md` | Chcesz absolutnie świeży start |

**Domyślny tryb przy "zresetuj kurs" bez doprecyzowania: miękki.**

# Procedura — twardy protokół potwierdzenia

## Krok 1: rozpoznaj intencję

Gdy uczeń mówi cokolwiek w stylu "zresetuj kurs", **NIE rób nic od razu**. Najpierw zadaj 2 pytania:

1. **"Czemu chcesz zresetować?"** — to ważne, bo czasem rozwiązanie jest inne (np. uczeń chce zmienić cel kursu, a wystarczy edytować `program.md`)
2. **"Miękki czy pełny reset?"** — pokaż tabelę z powyżej

Możliwe alternatywy, które warto zaproponować zamiast resetu:
- Chcesz zmienić cel/tempo → edytujemy `program.md`, nie resetujemy
- Chcesz powtórzyć temat → quiz "słabe punkty", nie reset
- Chcesz wyczyścić listę `do_powtorki` → operacja na `student.json`, nie reset

## Krok 2: pokaż, co konkretnie zniknie

Przed wykonaniem reset, **wypisz dokładnie** ścieżki plików, które zostaną przeniesione do backupu. Przykład:

```
Zostaną przeniesione do backupu postep/archiwum/2026-05-28-14-30/:
  - postep/student.json (12 ukończonych lekcji)
  - kurs/program.md
  [pełny reset]:
  - kurs/lekcje/ (8 plików)
  - kurs/zadania/ (5 katalogów, ~14 plików .py)
```

## Krok 3: poproś o jawne potwierdzenie

Uczeń musi napisać **literalnie**:
- dla miękkiego: `tak, miękki reset`
- dla pełnego: `tak, pełny reset`

Inne potwierdzenia ("ok", "tak", "rób") — **odmawiasz** i prosisz o pełną frazę. To zabezpieczenie przed przypadkowym kliknięciem.

## Krok 4: wykonaj reset

### Stwórz katalog backupu

```bash
TIMESTAMP=$(date +%Y-%m-%d-%H-%M)
mkdir -p postep/archiwum/$TIMESTAMP
```

### Miękki reset

```bash
# Przenieś pliki postępu i program
mv postep/student.json postep/archiwum/$TIMESTAMP/ 2>/dev/null
mv kurs/program.md postep/archiwum/$TIMESTAMP/ 2>/dev/null
```

### Pełny reset

```bash
# Najpierw backup wszystkiego, co usuwasz
mv postep/student.json postep/archiwum/$TIMESTAMP/ 2>/dev/null
mv kurs/program.md postep/archiwum/$TIMESTAMP/ 2>/dev/null
[ -d kurs/lekcje ] && mv kurs/lekcje postep/archiwum/$TIMESTAMP/lekcje
[ -d kurs/zadania ] && mv kurs/zadania postep/archiwum/$TIMESTAMP/zadania

# Odtwórz puste katalogi
mkdir -p kurs/lekcje kurs/zadania
```

**Nigdy nie używaj `rm -rf`.** Używaj wyłącznie `mv` do `postep/archiwum/`. To gwarancja, że nawet po "pełnym" resecie dane fizycznie są na dysku.

### Zapisz manifest backupu

W `postep/archiwum/$TIMESTAMP/MANIFEST.md` zapisz:

```markdown
# Backup z dnia 2026-05-28 14:30

**Tryb resetu:** miękki | pełny
**Powód podany przez ucznia:** [krótki cytat]
**Stan przed resetem:**
- Ukończonych lekcji: 12
- Aktualna lekcja w momencie resetu: 4.2
- Liczba sesji: 7

**Co jest w tym katalogu:**
- student.json
- program.md
- (przy pełnym: lekcje/, zadania/)

Aby przywrócić: skopiuj pliki z tego katalogu z powrotem do kurs/ i postep/.
```

## Krok 5: potwierdź i zaproś do nowego startu

Po wykonaniu napisz uczniowi:

> "Gotowe. Stary stan jest w `postep/archiwum/2026-05-28-14-30/` — jakbyś chciał wrócić, daj znać. Zaczynamy od nowa? Napisz **'ucz mnie Pythona'**, przejdziemy przez onboarding."

# Przywracanie z backupu

Jeśli uczeń po resecie powie "cofnij" / "wróć do poprzedniego stanu":

1. Pokaż listę katalogów w `postep/archiwum/` (najnowszy na górze)
2. Zapytaj, który backup przywrócić
3. Skopiuj pliki **z powrotem** do `kurs/` i `postep/` — **nie usuwaj** katalogu archiwum
4. Potwierdź odczytem `student.json` (skill: postep)

# Sprzątanie starych backupów

**NIE rób tego automatycznie.** Jeśli uczeń zauważy, że ma 30 katalogów w `archiwum/`, zaproponuj: "Chcesz, żebym usunął backupy starsze niż 30 dni?" — i wtedy (po potwierdzeniu) usuń.

# Twarde zasady

- **Backup zawsze**, nawet przy pełnym resecie. Dane nigdy nie giną od razu.
- **Tylko `mv`, nigdy `rm -rf`.** Nawet `rm plik` jest zakazane bez wcześniejszego `mv` do archiwum.
- **Dwie pytania + jawne potwierdzenie** zanim wykonasz reset. Nie ma "szybkiej ścieżki".
- **Nie resetuj `.claude/`** — to konfiguracja agenta, nie stan ucznia.
- **Nie resetuj `kurs/JAK-PISAC-KOD.md`** — to instrukcja, nie generowany content.
- **Po resecie zawsze pokaż ścieżkę backupu** — uczeń musi wiedzieć, gdzie poszły jego rzeczy.
