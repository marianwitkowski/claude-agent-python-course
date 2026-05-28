---
name: setup-python
description: Sprawdza czy w systemie zainstalowany jest Python 3.10+ (działa na macOS / Linux / Windows), prowadzi ucznia przez instalację jeśli brak, weryfikuje że Python działa, instruuje o aktywacji venv specyficznej dla systemu. Użyj na początku pierwszej sesji lub gdy uczeń zgłasza, że komenda Pythona nie działa.
---

# Cel

Doprowadzić ucznia do stanu, w którym **w jego terminalu** działa `python --version` (Windows) lub `python3 --version` (macOS/Linux) i pokazuje Python 3.10 lub nowszy.

# Krok 0: rozpoznaj system operacyjny

**Zawsze najpierw** ustal, na jakim systemie pracuje uczeń — to determinuje komendy w dalszych krokach.

```bash
uname -s 2>/dev/null || echo "Windows (lub PowerShell)"
```

- `Darwin` → macOS
- `Linux` → Linux (Ubuntu/Debian/Fedora/Arch/...)
- `MINGW*` / `MSYS*` / brak `uname` → Windows

Jeśli niejasne — zapytaj ucznia wprost: "Na jakim systemie pracujesz: macOS, Linux czy Windows?"

# Krok 1: sprawdź obecność Pythona

## macOS / Linux

```bash
python3 --version
```

## Windows

```powershell
py --version
# lub:
python --version
```

**Uwaga dla Windows:** często instalator `python.org` instaluje `py` (launcher) + `python`. **`python3` na Windows zwykle nie istnieje.** Używaj `py` (najczystsze) lub `python`.

**Interpretacja:**
- `Python 3.10.x` lub nowszy → **gotowe**, przejdź do kroku 4.
- `Python 3.9.x` lub starszy → ostrzeż, że niektóre funkcje 3.10+ (match/case, lepsze tracebacki, f-string 3.12+) nie zadziałają, ale fundament jest OK. Przejdź do kroku 4.
- `command not found` (macOS/Linux) lub `nie jest rozpoznawany` (Windows) → krok 2.

# Krok 2: instalacja — gałąź wg systemu

**Nie instaluj nic sam.** Daj instrukcję, uczeń wykonuje, potem wracacie do kroku 1 w **nowym terminalu** (PATH musi się odświeżyć).

## 2A — macOS

Sprawdź Homebrew:
```bash
brew --version
```

- **Mam brew** → `brew install python@3.12`
- **Nie mam brew** → dwie opcje:
  1. **python.org** (najprościej dla niedoświadczonych): https://www.python.org/downloads/macos/ — pobierz `.pkg`, kliknij, zainstaluj. **Restart terminala obowiązkowy.**
  2. **Homebrew** (dla osób gotowych na CLI): instrukcje z https://brew.sh, potem `brew install python@3.12`

## 2B — Linux

Wg dystrybucji:

**Ubuntu / Debian:**
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

**Fedora / RHEL:**
```bash
sudo dnf install python3 python3-pip
```

**Arch:**
```bash
sudo pacman -S python python-pip
```

**Uwaga:** na większości dystrybucji `python3` jest **już zainstalowany**. Jeśli `python3 --version` z kroku 1 nie zadziałało, sprawdź też samo `python` (na niektórych dystrybucjach to alias).

## 2C — Windows

**Rekomendacja (najprostsza): instalator z python.org**

1. Wejdź na https://www.python.org/downloads/windows/
2. Pobierz "Windows installer (64-bit)" dla najnowszej wersji 3.12 lub 3.13
3. Uruchom instalator
4. **KRYTYCZNE:** zaznacz checkbox **"Add python.exe to PATH"** na pierwszym ekranie
5. Klik "Install Now"
6. **Zamknij i otwórz NOWY** PowerShell / terminal
7. Sprawdź: `py --version` lub `python --version`

**Alternatywa: Microsoft Store**

W menu Start wpisz "Python 3.12" → zainstaluj ze Store. Wygodne, ale ścieżka jest dziwna i czasem powoduje problemy z venv.

**Dla power users: WSL (Windows Subsystem for Linux)**

Jeśli uczeń jest gotowy na większy krok — WSL daje pełne środowisko Linuxa pod Windows:
```powershell
wsl --install
```
Po restart i konfiguracji → wszystkie komendy macOS/Linux z tego kursu działają. **Polecane dla osób, które wiedzą po co.**

# Krok 3: weryfikacja

Po deklarowanej instalacji uczeń musi:
1. **Otworzyć NOWY terminal** (stary nie zna nowego PATH)
2. Powtórzyć Krok 1

# Krok 4: test "działa"

## macOS / Linux

```bash
python3 -c "print('działa')"
```

## Windows (PowerShell)

```powershell
py -c "print('działa')"
```

Powinno wypisać `działa`. Jeśli tak — **Python OK**.

# Krok 5: aktywacja venv — różnice systemowe

To zapamiętaj raz na zawsze (przyda się od lekcji 9.2):

## macOS / Linux (bash / zsh / fish)

```bash
python3 -m venv .venv
source .venv/bin/activate
# w fish: source .venv/bin/activate.fish
```

Deaktywacja:
```bash
deactivate
```

## Windows — PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

**Jeśli PowerShell rzuca błąd o execution policy:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
(uruchom jako Administrator, potwierdź `Y`)

## Windows — cmd.exe

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
```

**Sygnał, że venv aktywny:** prompt zaczyna się od `(.venv)`.

# Krok 6: edytor

Rekomendacja dla początkujących (działa na wszystkich systemach):
- **VS Code** (https://code.visualstudio.com/) + rozszerzenie **"Python"** od Microsoftu

Alternatywy:
- **PyCharm Community** (darmowy w pełni od 2024)
- Jakikolwiek edytor tekstu (Notepad++, Sublime Text, vim) — **NIE Word, NIE TextEdit w trybie domyślnym na macOS**

# Krok 7: instrukcja workflow

**Zawsze** na koniec setupu wskaż uczniowi plik `kurs/JAK-PISAC-KOD.md`:

> "Zanim zaczniemy pierwszą lekcję — otwórz w edytorze plik `kurs/JAK-PISAC-KOD.md` i przeczytaj go. To 5 minut, a wyjaśnia: gdzie zapisywać kod, jak uruchamiać pliki, jak czytać błędy, plus różnice komend między macOS/Linux/Windows. Daj znać, gdy przeczytasz."

Nie idź dalej, dopóki uczeń nie potwierdzi.

# Mapa komend wg systemu — ściąga dla agenta

| Co                       | macOS / Linux              | Windows PowerShell           |
| ------------------------ | -------------------------- | ---------------------------- |
| Uruchom Python           | `python3 plik.py`          | `py plik.py` (lub `python plik.py`) |
| Wersja                   | `python3 --version`        | `py --version`               |
| Tryb interaktywny        | `python3`                  | `py`                         |
| Stwórz venv              | `python3 -m venv .venv`    | `py -m venv .venv`           |
| Aktywuj venv             | `source .venv/bin/activate`| `.venv\Scripts\Activate.ps1` |
| Deaktywuj venv           | `deactivate`               | `deactivate`                 |
| Sprawdź ścieżkę pythona  | `which python3`            | `where python` / `Get-Command python` |
| Bieżący katalog          | `pwd`                      | `pwd` (PS) / `cd` bez args (cmd) |
| Lista plików             | `ls`                       | `ls` (PS) / `dir` (cmd)       |
| Zmiana katalogu          | `cd folder`                | `cd folder`                  |

**Zasada agenta:** zanim pokażesz komendę, **wiedz na jakim systemie jest uczeń**. Komendy mac w PowerShell nie działają i odwrotnie.

# Twarde zasady

- **Nie uruchamiaj instalatorów** za ucznia. To jego maszyna.
- **Nie modyfikuj** `~/.zshrc`, `~/.bash_profile`, profilu PowerShell itp.
- **`python` (bez 3) na macOS/Linux** — sprawdź wersję, jeśli to Python 2 — każ używać `python3`.
- **`python3` na Windows** — często nie istnieje. Używaj `py` lub `python`.
- **Po instalacji ZAWSZE nowy terminal** — to oszczędzi długich poszukiwań "czemu nie działa".

# Zapis środowiska do `student.json`

Po zakończonym setupie ZAWSZE zapisz środowisko (po onboardingu może być od razu w `init`, w trakcie kursu przez `update-srodowisko`):

```bash
# Jeśli student.json istnieje (np. setup uruchomiony powtórnie):
python3 .claude/skills/postep/postep.py update-srodowisko \
  --system "macOS" \
  --python-cmd "python3" \
  --venv-activate "source .venv/bin/activate" \
  --shell "zsh" \
  --edytor "VS Code"
```

**Mapowanie systemu → komendy:**

| System  | `python_cmd` | `venv_activate`                       | `shell`        |
| ------- | ------------ | ------------------------------------- | -------------- |
| macOS   | `python3`    | `source .venv/bin/activate`           | `zsh`/`bash`   |
| Linux   | `python3`    | `source .venv/bin/activate`           | `bash`/`zsh`   |
| Windows | `py`         | `.venv\Scripts\Activate.ps1`          | `PowerShell`   |
| WSL     | `python3`    | `source .venv/bin/activate`           | `bash`         |

Zapis przez `postep.py` jest atomowy — nie ma ryzyka uszkodzenia `student.json`.

# Zwrotka do agenta-rodzica

Po zakończeniu zwróć krótko:
- `OK: Python 3.X.Y na <system>, komenda: <python3|py>, edytor: <nazwa> — środowisko zapisane`
- lub `BLOCKED: <co nie działa>`

**Od tego momentu** WSZYSTKIE skille edukacyjne (lekcja, cwiczenie, review-kodu) muszą używać `srodowisko.python_cmd` z `student.json`, nie hardcoded `python3`.
