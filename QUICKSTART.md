# QUICKSTART — Jak korzystać z agenta `python-tutor`

Krótki przewodnik dla osoby zaczynającej naukę Pythona z tym kursem.

> **⚠️ Użytkownicy Windows:** Wszystkie komendy w lekcjach i tym dokumencie są pisane w wersji **macOS/Linux**. Na Windows zamień:
> - `python3` → `py`
> - `source .venv/bin/activate` → `.venv\Scripts\Activate.ps1`
> - `which python3` → `Get-Command python`
>
> Agent automatycznie tłumaczy komendy podczas sesji (jeśli w onboardingu zaznaczyłeś Windows). Ta uwaga dotyczy **ręcznego** czytania dokumentów.

---

## 🚀 Pierwsze uruchomienie

### 1. Sprawdź, gdzie jesteś
```bash
cd /Users/emilzatopek/kurs-python
pwd
```
Musisz być **w tym katalogu** — agent i skille są lokalne (`.claude/`).

### 2. Uruchom Claude Code
```bash
claude
```

### 3. Napisz w czacie
```
ucz mnie Pythona
```

Agent automatycznie:
1. Wykryje brak `postep/student.json` → uruchomi **onboarding**
2. Sprawdzi czy masz Pythona (`python3 --version`)
3. Każe Ci przeczytać `kurs/JAK-PISAC-KOD.md` (5 min)
4. Zapyta o imię, cel (praca/dane/hobby/szkoła), tempo (h/tydzień)
5. Wygeneruje **Twój** `kurs/program.md` (39 lekcji dopasowanych do celu)
6. Utworzy `postep/student.json` ze stanem początkowym
7. Zaproponuje rozpoczęcie lekcji 1.1

---

## 📚 Typowa sesja nauki

### Układ dwóch okien obok siebie

```
┌──────────────────────────┬──────────────────────────┐
│                          │                          │
│      Claude Code         │     VS Code + terminal   │
│      (lewa połowa)       │     (prawa połowa)       │
│                          │                          │
│  Tutaj rozmawiasz        │  Tutaj piszesz kod       │
│  z agentem               │  i go uruchamiasz        │
│                          │                          │
└──────────────────────────┴──────────────────────────┘
```

### Przebieg lekcji

1. **W Claude Code:** napisz `kontynuujemy`
2. Agent wczytuje gotową lekcję z `wiedza/lekcje/03.02-petla-for.md` i prowadzi Cię **sokratejsko** (zadaje pytania, Ty odpowiadasz)
3. **Eksperyment** — agent każe Ci coś napisać; otwierasz VS Code, piszesz w `kurs/zadania/03-petle/notatnik.py`
4. **W terminalu** uruchamiasz: `python3 kurs/zadania/03-petle/notatnik.py`
5. Wracasz do Claude Code, mówisz "wypisało X" — agent dopytuje
6. **Ćwiczenie** — agent generuje 3 zadania (🔥/⭐/⚡)
7. Piszesz rozwiązania jako `rozwiazanie_warmup.py`, `rozwiazanie_main.py`
8. Mówisz `sprawdź moje zadanie` → agent robi **sokratejski review** (pyta, nie ocenia bezpośrednio)
9. Agent aktualizuje `postep/student.json`, ustawia następną lekcję

---

## 🎯 Najczęstsze komendy

| Co chcę zrobić                  | Komenda                          |
| -------------------------------- | -------------------------------- |
| Wrócić do nauki po przerwie     | `kontynuujemy`                   |
| Coś przetestować                | `daj mi zadanie`                 |
| Sprawdzić mój kod               | `sprawdź moje zadanie`           |
| Powtórka                        | `quiz` (3 pyt) / `quiz słabe`    |
| Stan postępów                   | `pokaż postępy`                  |
| Zapomniałem, co mogę robić      | `lista komend`                   |
| Coś nie działa                  | `nie działa mi` + wklej kod      |
| Zacząć od nowa                  | `zresetuj kurs`                  |

Pełna lista — napisz `lista komend` w czacie lub zobacz [README.md](README.md).

---

## ⏸ Co zrobić, gdy wracasz po tygodniach

Po prostu napisz `ucz mnie Pythona` albo `kontynuujemy`:
- Agent czyta `postep/student.json`
- Wita Cię po imieniu, pokazuje ostatnią lekcję
- Jeśli przerwa > 7 dni → **automatycznie** zaproponuje krótki quiz powtórkowy
- Potem ruszacie z bieżącą lekcją

---

## 🔧 Komendy techniczne (rzadziej)

| Sytuacja                              | Komenda                          |
| ------------------------------------- | -------------------------------- |
| Pierwsze uruchomienie, brak Pythona  | `sprawdź Pythona`                |
| Odświeżenie materiałów z repo źródł. | `odśwież bazę wiedzy`            |
| Sprawdzenie stanu bazy               | `pokaż stan bazy`                |
| Cofnięcie resetu                     | `cofnij reset`                   |

---

## 📂 Co jest gdzie

```
ITMOBILE-kurs-python/
│
├── .claude/                      ← agent + skille (NIE dotykaj)
├── wiedza/                       ← baza wiedzy (39 lekcji gotowych)
│
├── kurs/
│   ├── JAK-PISAC-KOD.md          ← PRZECZYTAJ NA POCZĄTKU (5 min)
│   ├── program.md                ← Twój plan kursu (powstanie po onboardingu)
│   ├── lekcje/                   ← Twoje notatki z lekcji (agent zapisuje)
│   └── zadania/                  ← TU PISZESZ SWÓJ KOD
│       └── 03-petle/
│           ├── rozwiazanie_warmup.py     ← tworzysz Ty
│           ├── rozwiazanie_main.py
│           └── ZADANIA.md                ← zapisuje agent
│
└── postep/
    ├── student.json              ← Twój stan (możesz podglądać)
    └── archiwum/                 ← backupy po resetach
```

---

## 💡 Mini-przykład pełnej sesji

```
Ty:    ucz mnie Pythona
Agent: Cześć! Widzę, że jesteś tu pierwszy raz. Zacznijmy od sprawdzenia,
       czy masz Pythona. Otwórz terminal i wpisz: python3 --version

Ty:    Python 3.13.1
Agent: Świetnie. Teraz proszę przeczytaj kurs/JAK-PISAC-KOD.md — 5 minut,
       wyjaśnia gdzie piszesz kod i jak go uruchamiasz. Daj znać gdy skończysz.

Ty:    przeczytałam
Agent: Super. Teraz 4 pytania, żeby dopasować kurs:
       1. Jak masz na imię?
       2. Czemu chcesz się uczyć Pythona? (praca / dane / hobby / szkoła)
       3. Ile godzin tygodniowo możesz poświęcić?
       4. Programowałaś już kiedyś w innym języku?

Ty:    Anna, hobby, 3-5h tygodniowo, nigdy nie programowałam
Agent: [generuje program.md, student.json] Mam dla Ciebie 39 lekcji w 12 modułach,
       dopasowane do tempa ~3 lekcje/tydzień. Pełen kurs zajmie ~13 tygodni.
       Zaczynamy od lekcji 1.1 — "Co to jest Python"?

Ty:    tak, zaczynamy
Agent: Pomyśl o przepisie kulinarnym...
```

---

## ⚠️ Kilka pułapek na start

- **Plik niezapisany przed `python3 plik.py`** — najczęstszy błąd. Zawsze `Cmd+S`.
- **Uruchamianie z złego katalogu** — sprawdź `pwd`.
- **Polskie znaki + Windows** — agent ostrzeże, używaj `encoding="utf-8"`.
- **Nie kopiuj rozwiązań** — uczysz się przez próbowanie, nie czytanie.
- **`python` vs `python3`** — zawsze `python3` na macOS/Linux.

---

## 🆘 Co zrobić, gdy coś nie działa

| Problem                                | Co zrobić                                       |
| -------------------------------------- | ----------------------------------------------- |
| Agent się nie aktywuje                 | Sprawdź `pwd` — musisz być w katalogu kursu     |
| Nie pamiętam komend                    | `lista komend`                                  |
| Utknąłem na zadaniu                    | `nie działa mi` + wklej kod + wklej błąd        |
| Chcę zacząć od nowa                    | `zresetuj kurs` (z backupem)                    |
| Zgubiłem postęp                        | `przywróć backup` (z `postep/archiwum/`)        |
| Materiały wyglądają nieaktualnie       | `odśwież bazę wiedzy`                           |
| Pytanie o Pythona, nie kurs           | Po prostu zapytaj agenta normalnie              |

---

## 📤 Dla autora (publikacja na GitHubie)

Jeśli chcesz udostępnić kurs:

```bash
git init
git add .
git status                # sprawdź czy nic wrażliwego (postep/student.json itd. ignorowane)
git commit -m "Initial: agent + baza wiedzy"
gh repo create python-kurs-tutor --public --source=. --push
```

`.gitignore` zadba, żeby Twój prywatny postęp i kod nie trafiały do publicznego repo — można bezpiecznie udostępnić **strukturę kursu**, a każdy uczeń klonuje i ma własny `student.json`.

---

## 🎓 Filozofia kursu — w 3 zdaniach

1. **Sokratejsko, nie wykładowo** — agent zadaje pytania, Ty dochodzisz do odpowiedzi sam(a). Wolniej, ale głębiej.
2. **Nie uruchamiamy kodu za Ciebie** — sam piszesz, sam uruchamiasz, sam czytasz output. Część nauki.
3. **Twoje tempo** — czas trwania lekcji to wskazówka, nie deadline. Możesz wrócić za tydzień, agent wie gdzie skończyliście.

---

## 🔗 Powiązane dokumenty

- **[README.md](README.md)** — pełna dokumentacja, struktura, lista komend
- **[kurs/JAK-PISAC-KOD.md](kurs/JAK-PISAC-KOD.md)** — workflow pisania i uruchamiania kodu (przeczytaj raz na początku)
- **[wiedza/INDEX.md](wiedza/INDEX.md)** — mapa 39 lekcji
- **[wiedza/AKTUALIZACJE.md](wiedza/AKTUALIZACJE.md)** — co się zmieniło w Pythonie 2024 → 2026

---

**Powodzenia!** 🐍
