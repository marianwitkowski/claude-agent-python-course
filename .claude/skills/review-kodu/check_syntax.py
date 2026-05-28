#!/usr/bin/env python3
"""Sprawdzenie składni pliku .py BEZ uruchamiania kodu i BEZ tworzenia .pyc.

Używa ast.parse — pure Python, zero side effects:
- nie tworzy __pycache__/*.pyc
- nie wykonuje żadnej linii kodu (tylko parsuje składnię)
- działa identycznie na każdym systemie (macOS / Linux / Windows)

Użycie:
    python3 check_syntax.py <plik.py>

Wyjście (stdout):
    "OK: <plik> — składnia poprawna"

Lub błąd (stderr + exit 1):
    "SyntaxError w <plik>, linia N kolumna M: <komunikat>"
    "        <fragment linii>"
    "        ^"

Skrypt może być używany przez skill review-kodu jako alternatywa dla
`python3 -m py_compile`, który tworzy plik .pyc i modyfikuje katalog ucznia.
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path


def check(path: Path) -> int:
    if not path.is_file():
        print(f"BŁĄD: {path} nie istnieje lub nie jest plikiem", file=sys.stderr)
        return 2

    try:
        source = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        print(f"BŁĄD kodowania w {path}: {e}", file=sys.stderr)
        print("Sprawdź, czy plik jest zapisany w UTF-8.", file=sys.stderr)
        return 2

    try:
        ast.parse(source, filename=str(path))
    except SyntaxError as e:
        # e.lineno, e.offset, e.msg, e.text
        print(f"SyntaxError w {path}, linia {e.lineno} kolumna {e.offset}: {e.msg}",
              file=sys.stderr)
        if e.text:
            print(f"        {e.text.rstrip()}", file=sys.stderr)
            if e.offset:
                # ASCII strzałka pod miejscem błędu (uwaga na taby — przybliżenie)
                print("        " + " " * max(0, e.offset - 1) + "^", file=sys.stderr)
        return 1

    print(f"OK: {path} — składnia poprawna")
    return 0


def main() -> int:
    if len(sys.argv) != 2:
        print("Użycie: python3 check_syntax.py <plik.py>", file=sys.stderr)
        return 2
    return check(Path(sys.argv[1]))


if __name__ == "__main__":
    sys.exit(main())
