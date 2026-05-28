---
name: setup-python
description: Sprawdza czy w systemie zainstalowany jest Python 3.10+, prowadzi ucznia przez instalację jeśli brak, weryfikuje że `python3 -c "print('ok')"` działa. Użyj na początku pierwszej sesji lub gdy uczeń zgłasza, że komenda `python3` nie działa.
---

# Cel

Doprowadzić ucznia do stanu, w którym w jego terminalu działa `python3 --version` i pokazuje Python 3.10 lub nowszy.

# Procedura

## Krok 1: sprawdź obecność

```bash
python3 --version
```

- Jeśli pokazuje `Python 3.10.x` lub nowszy → **gotowe**, przejdź do kroku 4.
- Jeśli `Python 3.9.x` lub starszy → ostrzeż ucznia, że niektóre nowsze funkcje mogą nie działać, ale można jechać. Przejdź do kroku 4.
- Jeśli `command not found` → krok 2.

## Krok 2: instalacja (macOS — bo użytkownik na darwin)

Zapytaj ucznia, czy ma zainstalowane Homebrew:

```bash
brew --version
```

- Jeśli tak → poproś o uruchomienie:
  ```
  brew install python@3.12
  ```
- Jeśli nie → wytłumacz dwie opcje (wybór ucznia):
  1. **Instalator z python.org** (najprościej): polecasz pobranie z https://www.python.org/downloads/macos/ — uczeń pobiera, klika, instaluje
  2. **Homebrew** (dla osób gotowych na narzędzie wiersza poleceń): instrukcje z https://brew.sh

**Nie instaluj nic sam.** Daj instrukcję, uczeń wykonuje, potem wracacie do kroku 1.

## Krok 3: weryfikacja

Po deklarowanej instalacji — zawsze powtórz krok 1 w **nowym** terminalu (`PATH` musi się odświeżyć).

## Krok 4: test "hello world" w terminalu

Poproś ucznia, by w terminalu wpisał:

```bash
python3 -c "print('działa')"
```

Powinno wypisać: `działa`.

Jeśli wypisuje → **gotowe**.

## Krok 5: edytor

Zapytaj, w czym uczeń będzie pisał kod. Rekomendacja dla początkujących:
- **VS Code** (https://code.visualstudio.com/) + rozszerzenie "Python" od Microsoftu
- Alternatywa: jakikolwiek edytor tekstu, byle nie Word

Nie wymagaj IDE — proste skrypty można pisać w czymkolwiek.

## Krok 6: instrukcja workflow

**Zawsze** na koniec setupu wskaż uczniowi plik `kurs/JAK-PISAC-KOD.md`:

> "Zanim zaczniemy pierwszą lekcję — otwórz w edytorze plik `kurs/JAK-PISAC-KOD.md` i przeczytaj go. To 5 minut, a wyjaśnia: gdzie zapisywać kod, jak uruchamiać pliki, jak czytać błędy i jak wygląda cały workflow ćwiczenia. Daj znać, gdy przeczytasz — będę odsyłał Cię do tej instrukcji, gdy się czegoś zapomnisz."

Nie idź dalej, dopóki uczeń nie potwierdzi, że przeczytał. To fundament — bez tego pierwsze ćwiczenie będzie chaotyczne.

# Twarde zasady

- **Nie uruchamiaj instalatorów** za ucznia. To jego maszyna.
- **Nie modyfikuj** `~/.zshrc`, `~/.bash_profile` etc.
- Jeśli widzisz, że `python` (bez 3) wskazuje na Python 2 — wyjaśnij uczniowi różnicę i każ zawsze pisać `python3`.

# Zwrotka do agenta-rodzica

Po zakończeniu zwróć krótko:
- `OK: Python 3.X.Y, edytor: ...`
- lub `BLOCKED: <co nie działa>`
