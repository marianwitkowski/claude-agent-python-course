---
name: cwiczenie
description: Generuje 1-3 ćwiczenia do samodzielnego rozwiązania przez ucznia, dopasowane do bieżącej lekcji i poziomu trudności. Trzy poziomy: rozgrzewka, główne, gwiazdka. Użyj na końcu lekcji lub gdy uczeń prosi o "więcej zadań".
---

# Cel

Dać uczniowi **konkretne, mierzalne** zadanie do napisania w Pythonie — sam, bez podpowiedzi w kodzie.

# Trzy poziomy

Dla każdej lekcji wygeneruj zestaw 3 ćwiczeń:

| Poziom        | Cel                                            | Czas       | Wskazówka                   |
| ------------- | ---------------------------------------------- | ---------- | --------------------------- |
| Rozgrzewka 🔥 | Sprawdzenie, czy uczeń rozumie składnię        | 5 min      | "Powinno być łatwe"         |
| Główne ⭐     | Sprawdzenie, czy umie złożyć z poznanych klocków | 10-15 min  | "Pomyśl, zanim pisz"        |
| Gwiazdka ⚡   | Wyzwanie — łączy bieżącą lekcję z poprzednią   | 15-25 min  | "Może być trudne, to OK"    |

Uczeń wybiera, ile robi. Minimum: rozgrzewka + główne.

# Format ćwiczenia

Zapisz w `kurs/zadania/NN-temat/ZADANIA.md`:

```markdown
# Lekcja N: [temat] — ćwiczenia

## 🔥 Rozgrzewka
**Cel:** [jednolinijkowo, co robi]
**Zadanie:** [opis w 1-2 zdaniach]
**Wejście / wyjście (przykład):**
- jeśli podasz X, ma wypisać Y
- jeśli podasz Z, ma wypisać W

## ⭐ Główne
[jw.]

## ⚡ Gwiazdka
[jw.]
```

Uczeń zapisuje swój kod w `kurs/zadania/NN-temat/rozwiazanie_X.py` (X = warmup/main/star).

# Zasady dobrego ćwiczenia

- **Konkretny, sprawdzalny wynik.** Nie "napisz program o kotach", tylko "napisz program, który wypisze 5 razy 'miau'".
- **Realistyczny kontekst.** Nie `x = 5; y = 7; oblicz z`. Lepiej: "tata kupił 5 jabłek, mama 7, ile mają razem?"
- **Wymaga myślenia, nie kopiowania.** Jeśli rozwiązanie to skopiowanie przykładu z lekcji z podmianą liczb — ćwiczenie za łatwe.
- **Daj 2-3 przykłady wejścia/wyjścia.** Uczeń sam testuje swoje rozwiązanie.
- **Bez bibliotek zewnętrznych** do lekcji 11. Tylko Python standard.

# Przykłady (lekcja: zmienne i typy)

🔥 **Rozgrzewka:** Stwórz zmienne `imie` (twoje imię), `wiek` (twój wiek) i `ulubiony_kolor`. Wypisz każdą.

⭐ **Główne:** Napisz program-wizytówkę. Stwórz zmienne `imie`, `nazwisko`, `wiek`, `miasto`. Wypisz: `Cześć, jestem Anna Kowalska, mam 32 lata i mieszkam w Krakowie.` — z użyciem f-stringów.

⚡ **Gwiazdka:** Tata ma 45 lat, syn ma 12. Stwórz zmienne. Wypisz, ile lat różnicy. Potem wypisz, ile lat będzie miał syn, gdy tata będzie miał 60. (Bez ifów, bez inputu — tylko zmienne i arytmetyka.)

# Co po wygenerowaniu

- Pokaż uczniowi tylko 🔥 i ⭐ na start (gwiazdkę odsłaniaj dopiero, jak skończy oba).
- Powiedz dokładnie:
  - **gdzie** ma zapisać kod: `kurs/zadania/NN-temat/rozwiazanie_warmup.py`
  - **jak** uruchomić — używając komendy z `srodowisko.python_cmd` w `student.json` (NIE hardcoded `python3`):
    - macOS/Linux: `python3 kurs/zadania/NN-temat/rozwiazanie_warmup.py`
    - Windows: `py kurs/zadania/NN-temat/rozwiazanie_warmup.py`
- Jeśli uczeń wygląda na zagubionego co do workflow — przypomnij: "Spójrz do `kurs/JAK-PISAC-KOD.md`, sekcja 4 — cały workflow krok po kroku."
- Uczeń sam uruchamia kod. Ty potem robisz review (skill: review-kodu).

# Reguła komend — ZAWSZE z `student.json`

Przed wypisaniem JAKIEJKOLWIEK komendy uruchamiającej Pythona:
```bash
python3 .claude/skills/postep/postep.py read --field srodowisko.python_cmd
```

Użyj tej wartości w komendzie pokazanej uczniowi. Jeśli puste → zapytaj ucznia o system i zaktualizuj.

# Twarde zasady

- **Nigdy nie pisz rozwiązania** w pliku ZADANIA.md. Tylko opis zadania.
- **Nie pisz nawet szkieletu** w `rozwiazanie_X.py` — to pliki, które tworzy uczeń.
- Jeśli uczeń prosi "daj mi szablon" — odmów grzecznie: "Pomyśl, jakie zmienne będą Ci potrzebne. Wypisz mi je w czacie, zanim zaczniesz pisać kod."
