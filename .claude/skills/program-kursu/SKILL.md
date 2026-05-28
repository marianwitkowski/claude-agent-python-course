---
name: program-kursu
description: Generuje plik kurs/program.md — spersonalizowany program 12 modułów / 39 lekcji podstaw Pythona, na podstawie bazy wiedzy w `wiedza/INDEX.md`. Dostosowuje do celu ucznia (praca/hobby/dane/szkoła) i deklarowanego tempa. Użyj raz, podczas onboardingu, po krótkim wywiadzie z uczniem.
---

# Cel

Stworzyć `kurs/program.md` — plan kursu, do którego uczeń i tutor będą wracać. To **kompas**, nie sztywne tory.

# Źródło prawdy

**Zawsze** opieraj plan na pliku `wiedza/INDEX.md`. Nie wymyślaj modułów ani lekcji — tabela z INDEX.md to kanon (12 modułów, **39 lekcji**, oparte na repo `marianwitkowski/python-kurs-podstawowy`).

Jeśli `wiedza/INDEX.md` nie istnieje → coś jest nie tak z bazą wiedzy. Powiedz uczniowi i zaproponuj uruchomienie skill `baza-wiedzy` (pobranie z repo).

# Wejście

Wymagane od ucznia (przed wywołaniem skill):
- **Cel:** praca / dane / hobby / szkoła / inne
- **Czas tygodniowo:** <2h / 2-5h / 5-10h / 10+h
- **Doświadczenie z programowania:** brak / coś dotykał / inny język

# Procedura

1. **Wczytaj** `wiedza/INDEX.md` — to źródło struktury kursu
2. **Skopiuj** kanon (12 modułów, 39 lekcji — niektóre moduły 3, niektóre 4)
3. **Personalizuj** wg celu (patrz niżej)
4. **Dostosuj tempo** wg dostępnego czasu
5. **Zapisz** do `kurs/program.md`

# Personalizacja wg celu

W zależności od celu ucznia, **akcentuj** odpowiednie lekcje i projekt końcowy:

- **Cel: praca (backend/automation)** → moduł 9 z naciskiem na `venv` + `pyproject.toml` + `requests`; projekt końcowy: prosty API client lub skrypt automatyzujący zadanie z pracy
- **Cel: dane** → po module 4 dodaj wzmiankę o CSV (`csv` w stdlib); moduł 9 z naciskiem na czytanie plików z sieci; projekt: analiza prostego pliku CSV (przegląd, agregacja, sortowanie)
- **Cel: hobby / gry** → moduł 11 projekt jako gra tekstowa (zgadywanka, RPG-text, kółko-krzyżyk); moduł 10 minimal
- **Cel: szkoła / matematyka** → projekt jako kalkulator/solver problemów matematycznych; moduł 10 standardowy (lambda do funkcji matematycznych)
- **Cel: inny** → zapytaj o konkret, dobierz akcent

# Tempo

| Czas/tydz | Lekcji/tydz | Czas trwania kursu |
| --------- | ----------- | ------------------ |
| <2h       | 1           | ~30 tygodni        |
| 2-5h      | 2-3         | ~10-15 tygodni     |
| 5-10h     | 3-5         | ~6-10 tygodni      |
| 10+h      | 5-7         | ~4-6 tygodni       |

# Format pliku `kurs/program.md`

```markdown
# Program kursu Python — [imię]

**Cel:** [praca / dane / hobby / szkoła]
**Tempo:** [X lekcji / tydz]
**Rozpoczęto:** YYYY-MM-DD
**Bazujemy na:** wiedza/INDEX.md (źródło: github.com/marianwitkowski/python-kurs-podstawowy)

## Jak działa kurs
Krótki paragraf: sokratejskie podejście, własne tempo, postęp w postep/student.json.

## Moduły i lekcje

### Moduł 1: Wprowadzenie i środowisko
- Lekcja 1.1: Co to jest Python i do czego służy
- Lekcja 1.2: Pierwszy program — `print` w REPL i z pliku
- Lekcja 1.3: Edytor i terminal — workflow ucznia

### Moduł 2: Podstawy języka
- Lekcja 2.1: Zmienne i typy proste
- Lekcja 2.2: Operatory i wyrażenia
- Lekcja 2.3: `print` i f-stringi

[...kontynuuj wg INDEX.md, wszystkie 12 modułów...]

## Projekt końcowy (Moduł 11)
[Spersonalizowany pod cel ucznia — z 2-3 propozycjami do wyboru]
```

# Twarde zasady

- **Źródłem prawdy jest `wiedza/INDEX.md`.** Nie wymyślaj nowych lekcji, nie pomijaj modułów bez zgody ucznia.
- **Trzymaj się 12 modułów.** Jeśli uczeń chce mniej — pomiń moduły 10-12, ale nie zmieniaj struktury środka.
- **Nie wymyślaj** modułów typu "Django", "ML", "asyncio" — to nie kurs zaawansowany. Te tematy są wzmiankowane w module 12 (mapa dalszych kroków), nie jako lekcje.
- Plik nadpisujesz **tylko jeśli** uczeń świadomie chce zmienić program (np. zmieniły mu się cele).

# Po wygenerowaniu

Pokaż uczniowi spis modułów (nie cały plik) i zapytaj, czy chce coś zmienić, zanim ruszycie z lekcją 1.
