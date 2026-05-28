# Kurs Pythona z tutorem Claude

Interaktywny kurs podstaw Pythona dla **kompletnie początkujących**, prowadzony przez agenta Claude Code metodą **sokratejską** — uczeń sam dochodzi do rozwiązań przez pytania naprowadzające.

## Dla kogo

- Osoby, które **nigdy nie programowały**
- Chcące uczyć się w swoim tempie, z prowadzącym, który nie podaje gotowców
- Mające zainstalowane lub gotowe zainstalować Claude Code

## Jak zacząć

> 🚀 **Szybki start:** zobacz **[QUICKSTART.md](QUICKSTART.md)** — przewodnik krok po kroku z przykładami.

W katalogu kursu uruchom Claude Code i napisz:

```
ucz mnie Pythona
```

albo

```
zacznij lekcję
```

Agent `python-tutor` przeprowadzi Cię przez:
1. Sprawdzenie środowiska (Python, edytor)
2. Krótki wywiad (cel, dostępny czas)
3. Wygenerowanie programu kursu dopasowanego do Ciebie
4. Pierwszą lekcję

## Struktura projektu

```
.
├── .claude/
│   ├── agents/python-tutor.md          # główny agent
│   └── skills/                         # specjalistyczne umiejętności
│       ├── setup-python/               # sprawdzenie środowiska
│       ├── program-kursu/              # generator programu
│       ├── lekcja/                     # prowadzenie lekcji
│       ├── cwiczenie/                  # generator ćwiczeń
│       ├── review-kodu/                # sokratejski review
│       ├── quiz/                       # quizy powtórkowe między lekcjami
│       ├── reset-kursu/                # reset miękki/pełny z backupem
│       ├── pomoc/                      # lista komend w czacie
│       ├── baza-wiedzy/                # pobieranie/odświeżanie z repo źródłowego
│       └── postep/                     # śledzenie postępu
├── wiedza/                             # lokalna baza wiedzy
│   ├── zrodlo/                         # 1:1 z github.com/marianwitkowski/python-kurs-podstawowy
│   ├── AKTUALIZACJE.md                 # delta: Python 3.12-3.14, idiomy, narzędzia 2026
│   ├── INDEX.md                        # mapowanie 12 modułów → 39 lekcji sokratejskich
│   └── lekcje/                         # 39 gotowych lekcji sokratejskich + SZABLON-LEKCJI.md
├── kurs/
│   ├── JAK-PISAC-KOD.md                # ⬅ przeczytaj na początku: workflow ćwiczeń
│   ├── program.md                      # Twój program kursu (powstanie po onboardingu)
│   ├── lekcje/                         # notatki z każdej lekcji
│   └── zadania/                        # Twój kod do ćwiczeń
└── postep/
    ├── student.json                    # Twój stan: ukończone lekcje, mocne strony, do powtórki
    └── archiwum/                       # backupy po resetach (nigdy nie kasowane automatycznie)
```

## Zanim zaczniesz pierwszą lekcję

Przeczytaj **[`kurs/JAK-PISAC-KOD.md`](kurs/JAK-PISAC-KOD.md)** — 5 minut, ale wyjaśnia:
- gdzie zapisywać kod (`kurs/zadania/NN-temat/...py`)
- jak uruchamiać pliki w terminalu (`python3 plik.py`)
- jak czytać komunikaty błędów (traceback)
- cały workflow ćwiczenia od początku do końca
- najczęstsze pułapki początkujących

## Filozofia

- **Sokratejsko, nie wykładowo.** Agent zadaje pytania zamiast wyjaśniać. To wolniejsze, ale głębsze.
- **Nie uruchamiamy kodu za Ciebie.** Sam piszesz, sam uruchamiasz w terminalu, sam czytasz output. To część nauki.
- **Postęp jest Twój.** Wszystko w `postep/student.json` — możesz przeglądać, edytować, eksportować.
- **Twoje tempo.** Czas trwania lekcji to wskazówka, nie deadline. Możesz wrócić za tydzień, agent będzie wiedział, gdzie skończyliście.

## Lista komend

Komendy wpisujesz w Claude Code — to są **frazy w języku naturalnym**, nie formalne komendy. Agent rozpozna intencję, nawet jeśli sformułujesz to nieco inaczej. Poniżej kanoniczne wersje.

### 🚀 Start i kontynuacja

| Komenda                          | Co zrobi agent                                            |
| -------------------------------- | --------------------------------------------------------- |
| `ucz mnie Pythona`               | Start kursu — onboarding lub powitanie i kontynuacja      |
| `zacznij lekcję`                 | To samo, bardziej formalnie                               |
| `kontynuujemy`                   | Kolejna lekcja z programu (`kurs/program.md`)             |
| `pokaż program kursu`            | Wyświetla zawartość `kurs/program.md`                     |
| `zmień program kursu`            | Edycja programu (np. zmiana celu, tempa)                  |

### 📚 W trakcie lekcji

| Komenda                          | Co zrobi agent                                            |
| -------------------------------- | --------------------------------------------------------- |
| `nie rozumiem [konceptu]`        | Wraca do podstaw konceptu nowym kątem                     |
| `daj mi przykład`                | Pokazuje minimalny przykład kodu (nie rozwiązanie)        |
| `co to znaczy [termin]?`         | Wyjaśnia termin przez pytania naprowadzające              |
| `powtórzmy tę lekcję`            | Wraca do bieżącej lekcji od początku                      |

### ✏️ Ćwiczenia i review

| Komenda                          | Co zrobi agent                                            |
| -------------------------------- | --------------------------------------------------------- |
| `daj mi zadanie`                 | Generuje ćwiczenie z bieżącej lekcji (3 poziomy)          |
| `daj mi więcej zadań`            | Dodatkowe ćwiczenia na opanowany koncept                  |
| `sprawdź moje zadanie`           | Sokratejski review kodu z `kurs/zadania/`                 |
| `skończyłem [warmup/main/star]`  | Review konkretnego rozwiązania                            |
| `nie działa mi`                  | Pomoc w debugowaniu — agent pyta o traceback              |
| `pokaż gwiazdkę`                 | Odsłania zadanie ⚡ gwiazdkowe (po ukończeniu pozostałych) |

### 🎯 Quizy i powtórki

| Komenda                          | Co zrobi agent                                            |
| -------------------------------- | --------------------------------------------------------- |
| `quiz`                           | Szybki quiz (3 pytania) z ostatnich lekcji                |
| `quiz pełny`                     | Pełny quiz (5-7 pytań) z całości materiału                |
| `quiz słabe`                     | Quiz z tematów oznaczonych w `do_powtorki`                |
| `powtórzmy [temat]`              | Krótka powtórka konkretnego konceptu                      |

### 📊 Postęp

| Komenda                          | Co zrobi agent                                            |
| -------------------------------- | --------------------------------------------------------- |
| `pokaż postępy`                  | Podsumowanie ze `student.json`                            |
| `gdzie skończyliśmy?`            | Przypomnienie aktualnej lekcji i ostatniej sesji          |
| `co mam do powtórki?`            | Lista tematów z pola `do_powtorki`                        |
| `co umiem najlepiej?`            | Lista z pola `mocne_strony`                               |

### 🔄 Reset i backup

| Komenda                          | Co zrobi agent                                            |
| -------------------------------- | --------------------------------------------------------- |
| `zresetuj kurs`                  | Reset **miękki** — czyści tylko postęp+program (z backupem) |
| `pełny reset kursu`              | Reset **pełny** — czyści wszystko, też Twój kod (z backupem) |
| `cofnij reset`                   | Przywrócenie ostatniego stanu z `postep/archiwum/`        |
| `przywróć backup`                | To samo — pokazuje listę archiwów do wyboru               |
| `pokaż backupy`                  | Wypisuje katalogi w `postep/archiwum/`                    |

### 🛠️ Środowisko i pomoc

| Komenda                          | Co zrobi agent                                            |
| -------------------------------- | --------------------------------------------------------- |
| `sprawdź Pythona`                | Weryfikacja, czy `python3` działa (skill `setup-python`)  |
| `jak uruchomić kod?`             | Odsyła do `kurs/JAK-PISAC-KOD.md`, sekcja 3-4             |
| `lista komend`                   | **Wyświetla tę listę w czacie** (skill `pomoc`)           |
| `pomoc` / `help` / `co mogę zrobić?` | To samo co `lista komend`                             |
| `krótka pomoc`                   | Skrócona wersja — tylko najważniejsze komendy             |

### 📖 Baza wiedzy

| Komenda                          | Co zrobi agent                                            |
| -------------------------------- | --------------------------------------------------------- |
| `odśwież bazę wiedzy`            | Pobiera najnowsze pliki z repo (z backupem)               |
| `pokaż stan bazy`                | Statystyki: ile plików, data ostatniego pobrania, commit  |
| `sprawdź czy baza aktualna`      | Porównuje lokalne pliki ze zdalnym repo                   |

> 💡 **Wskazówka:** Nie musisz pamiętać dokładnych fraz. "Zrób mi quiz", "wyczyść wszystko", "co robiłam ostatnio" — agent dopyta o szczegóły. Powyższe to kanoniczne wersje na wypadek, gdy chcesz mieć pewność.

## Wymagania

- **System operacyjny:** macOS, Linux lub Windows (PowerShell / cmd / WSL) — skill `setup-python` ma dedykowane gałęzie dla każdego
- **Python 3.10+** (rekomendowany 3.12 lub 3.13; sprawdzenie i instalacja przez skill `setup-python`)
- **Claude Code** (https://claude.com/code)
- **Edytor tekstu** — rekomendacja: VS Code + rozszerzenie Python (działa identycznie na każdym OS)

> 💡 **Notatka o komendach:** w lekcjach komendy są w wersji macOS/Linux (`python3`, `source .venv/bin/activate`). Na Windows używaj `py` (zamiast `python3`) i `.venv\Scripts\Activate.ps1` (zamiast `source ...`). Pełna mapa różnic w `kurs/JAK-PISAC-KOD.md` (sekcja 3) i skill `setup-python`.
