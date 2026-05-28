# Jak pisać i uruchamiać kod — instrukcja dla ucznia

Ten dokument odpowiada na trzy pytania:
1. **Gdzie** pisać kod?
2. **W czym** pisać kod (edytor)?
3. **Jak** uruchomić kod, żeby zobaczyć, co robi?

Przeczytaj raz, na początku kursu. Potem wracaj, gdy o czymś zapomnisz.

---

## 1. Gdzie pisać kod — struktura katalogów

Twój kod żyje w katalogu `kurs/zadania/`. Dla każdej lekcji powstaje osobny podkatalog:

```
kurs/
└── zadania/
    ├── 01-pierwszy-print/
    │   ├── rozwiazanie_warmup.py
    │   ├── rozwiazanie_main.py
    │   └── rozwiazanie_star.py        ← gwiazdkowe, opcjonalne
    ├── 02-zmienne/
    │   ├── rozwiazanie_warmup.py
    │   └── rozwiazanie_main.py
    └── 03-...
```

### Reguły nazewnictwa

- Katalog: `NN-krotki-temat` (np. `02-zmienne`, `05-petle`)
- Plik: `rozwiazanie_warmup.py` / `rozwiazanie_main.py` / `rozwiazanie_star.py`
- **Numerację i nazwę katalogu poda Ci agent** — nie musisz tego wymyślać sam

### Eksperymenty na boku

Jeśli chcesz coś przetestować "na brudno", utwórz plik `notatnik.py` w katalogu lekcji. Nie wpływa to na ocenę i agent wie, że to plik roboczy.

---

## 2. W czym pisać kod — edytor

### Rekomendacja: VS Code

1. Pobierz z https://code.visualstudio.com/
2. Zainstaluj rozszerzenie **Python** od Microsoftu (Extensions → wyszukaj "Python")
3. Otwórz cały katalog kursu: `File → Open Folder → ITMOBILE-kurs-python`
4. Pliki `.py` będą miały kolorowanie składni i podpowiedzi

### Inne opcje

- **PyCharm Community** — pełne IDE, mocniejsze ale cięższe; dobre, jeśli już znasz
- **Sublime Text / Notepad++** — wystarczą dla początkującego
- **NIE używaj:** Worda, TextEdit (na macOS w trybie domyślnym), Notatnika Windows w domyślnej konfiguracji — psują formatowanie

### Co musi umieć Twój edytor

- Pokazywać **wcięcia** (Python jest na nie wrażliwy — pomyłka 3 vs 4 spacje to błąd!)
- Zapisywać pliki w **UTF-8** (dla polskich znaków `ą ę ć`)
- Mieć **kolorowanie składni** Pythona (żebyś widział słowa kluczowe)

---

## 3. Jak uruchomić kod — terminal

### Co to terminal?

To okienko, w którym wpisujesz **komendy tekstowe** zamiast klikać.

| System    | Jak otworzyć terminal                                          | Komenda Pythona |
| --------- | -------------------------------------------------------------- | --------------- |
| **macOS** | Cmd+Space → "Terminal" → Enter                                 | `python3`       |
| **Linux**| Ctrl+Alt+T (większość dystrybucji)                              | `python3`       |
| **Windows** | Win+X → "Windows PowerShell" (lub "Terminal" na Win11)       | `py` lub `python` |

**⚠️ Ważne dla Windows:** w tej instrukcji wszędzie tam, gdzie widzisz `python3 plik.py`, **u Ciebie ma być `py plik.py`** (lub `python plik.py`). Komenda `python3` na Windows zwykle nie istnieje.

**⚠️ Ważne dla aktywacji venv (lekcja 9.2):**
- macOS/Linux: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Windows cmd: `.venv\Scripts\activate.bat`

Agent dopasuje komendy do Twojego systemu — daj mu znać na początku, jakiego używasz.

### Krok po kroku — uruchomienie pliku

#### 1. Przejdź do katalogu z kodem

```bash
cd ~/Desktop/Projekty/ITMOBILE-kurs-python
```

`cd` = "change directory" (zmień katalog).

Sprawdź, gdzie jesteś:
```bash
pwd
```
Powinno pokazać: `/Users/marian/Desktop/Projekty/ITMOBILE-kurs-python`

#### 2. Uruchom plik

```bash
python3 kurs/zadania/01-pierwszy-print/rozwiazanie_warmup.py
```

Output (czyli to, co program wypisze przez `print`) pojawi się **w terminalu**, pod komendą.

#### 3. Coś się nie zgadza? Czytaj komunikat

Jeśli Python pokaże coś takiego:

```
Traceback (most recent call last):
  File "rozwiazanie_warmup.py", line 3, in <module>
    print(witaj)
NameError: name 'witaj' is not defined
```

To **nie jest katastrofa** — to Python mówi, gdzie i co poszło źle:
- **`File "rozwiazanie_warmup.py", line 3`** — błąd jest w linii 3
- **`NameError: name 'witaj' is not defined`** — użyłeś zmiennej `witaj`, której wcześniej nie zdefiniowałeś

Czytanie błędów to **kluczowa umiejętność**. Agent będzie Ci pomagał — ale Twoją rolą jest najpierw **przeczytać samodzielnie**.

---

## 4. Cały workflow — od zadania do oceny

Tak wygląda jedna runda nauki:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Agent prowadzi lekcję w czacie Claude Code               │
│    → odpowiadasz na pytania naprowadzające                  │
├─────────────────────────────────────────────────────────────┤
│ 2. Agent daje ćwiczenie ("napisz program, który...")        │
│    → mówi, gdzie zapisać: kurs/zadania/NN-temat/...py       │
├─────────────────────────────────────────────────────────────┤
│ 3. Otwórz drugi terminal / VS Code obok Claude Code         │
│    → utwórz plik, napisz kod                                │
├─────────────────────────────────────────────────────────────┤
│ 4. W terminalu uruchom:                                     │
│    python3 kurs/zadania/NN-temat/rozwiazanie_warmup.py      │
│    → patrzysz na output                                     │
├─────────────────────────────────────────────────────────────┤
│ 5. Sam(a) oceń: czy wynik jest taki, jakiego oczekiwałeś?   │
│    → jeśli nie, czytaj traceback i poprawiaj                │
├─────────────────────────────────────────────────────────────┤
│ 6. Gdy działa — wracasz do Claude Code i piszesz:           │
│    "skończyłem warmup z lekcji 2"                           │
│    → agent zrobi review przez pytania                       │
└─────────────────────────────────────────────────────────────┘
```

**Wskazówka praktyczna:** trzymaj **dwa okna obok siebie** — Claude Code po lewej, terminal/edytor po prawej. Nie musisz przełączać kart.

---

## 5. Najczęstsze pułapki początkujących

### ❌ Uruchamiam `python plik.py`, a Python jest w wersji 2

Zawsze pisz `python3`, nie `python`. Na macOS `python` często wskazuje na bardzo starą wersję.

### ❌ "Permission denied"

Sprawdź, czy jesteś w dobrym katalogu (`pwd`). Nie trzeba `chmod +x` dla plików `.py`.

### ❌ "ModuleNotFoundError"

W podstawach kursu (lekcje 1-10) **nie używamy zewnętrznych bibliotek**. Jeśli widzisz ten błąd — prawdopodobnie literówka w `import` (np. `improt` zamiast `import`).

### ❌ Polskie znaki wypisują się jako "Ä…"

To problem kodowania. Upewnij się, że edytor zapisuje w UTF-8 (w VS Code widać w prawym dolnym rogu).

### ❌ Wcięcia "wyglądają tak samo", ale Python rzuca `IndentationError`

Pewnie mieszasz **spacje z tabulatorami**. Wybierz jedno (rekomendacja: 4 spacje) i trzymaj się. VS Code z rozszerzeniem Python robi to za Ciebie.

### ❌ Zapomniałem zapisać plik przed uruchomieniem

Najczęstszy błąd. Cmd+S **zawsze** przed `python3 plik.py`.

---

## 6. Komendy terminala — minimum, które Ci wystarczy

| Komenda                        | Co robi                                          |
| ------------------------------ | ------------------------------------------------ |
| `pwd`                          | Pokaż, w którym katalogu jestem                  |
| `ls`                           | Pokaż pliki w bieżącym katalogu                  |
| `cd nazwa-katalogu`            | Wejdź do podkatalogu                             |
| `cd ..`                        | Wyjdź o jeden katalog wyżej                      |
| `cd ~`                         | Wróć do katalogu domowego                        |
| `python3 plik.py`              | Uruchom plik Pythona                             |
| `python3`                      | Tryb interaktywny — pisz Python linijka po linijce |
| `exit()` (w trybie interaktywnym) | Wyjdź z trybu interaktywnego                  |
| **Ctrl+C**                     | Przerwij działający program (np. nieskończoną pętlę) |
| **strzałka w górę**            | Powtórz ostatnią komendę                         |

---

## 7. Tryb interaktywny — przyjaciel początkującego

Wpisz w terminalu:

```bash
python3
```

Zobaczysz `>>>`. Możesz pisać Pythona linijka po linijce:

```python
>>> x = 5
>>> y = 7
>>> x + y
12
>>> print("test")
test
>>> exit()
```

Świetne do **szybkich eksperymentów** ("co zwróci `len('Anna')`?"). Nie zastępuje plików `.py` — tu nic się nie zapisuje.

---

## Pytania? Pisz do agenta

W Claude Code możesz w każdej chwili powiedzieć:

- *"jak mam to uruchomić?"*
- *"nie wiem, gdzie zapisać kod"*
- *"co znaczy ten błąd?"*

Agent wróci do odpowiedniego fragmentu tej instrukcji albo poprowadzi Cię krok po kroku.
