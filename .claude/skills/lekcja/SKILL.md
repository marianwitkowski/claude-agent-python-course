---
name: lekcja
description: Prowadzi pojedynczą lekcję Pythona metodą sokratejską według struktury 5 kroków (zakotwiczenie → mostek → eksperyment → pogłębienie → ćwiczenie). Użyj gdy uczeń mówi "zaczynamy lekcję", "kontynuujemy" lub agent ma rozpocząć kolejną lekcję z programu.
---

# Cel

Doprowadzić ucznia do **samodzielnego zrozumienia** jednego konceptu Pythona w ciągu jednej sesji (30-60 min).

# Krok 0: Przygotowanie

**Przed** rozpoczęciem lekcji ZAWSZE:

## A. Odczytaj środowisko ucznia

```bash
python3 .claude/skills/postep/postep.py read --field srodowisko
```

Zapamiętaj `python_cmd` i `venv_activate` na całą sesję. Gdy lekcja w `wiedza/lekcje/` pokazuje `python3 ...`, a uczeń ma Windows — **tłumacz na `py ...`** zanim wyświetlisz uczniowi. To NIENEGOCJOWALNE.

Jeśli pole puste → zapytaj ucznia o system, zaktualizuj przez `postep.py update-srodowisko`.

## B. Wczytaj bazę wiedzy

1. **Pierwsza próba — gotowa lekcja sokratejska:**
   - Szukaj `wiedza/lekcje/NN.MM-temat.md` (np. `wiedza/lekcje/03.02-petla-for.md`)
   - Jeśli istnieje → to TWÓJ **główny scenariusz**. Zawiera 5-stopniową strukturę, pytania naprowadzające, eksperymenty, pułapki, notatki tutora i aktualizacje 2026
   - **Trzymaj się go** — została zaprojektowana sokratejsko, nie improwizuj poza nią
2. **Drugi krok — wczytaj `wiedza/INDEX.md`** żeby zobaczyć kontekst (poprzednie lekcje, następne)
3. **Trzeci krok (uzupełnienie) — `wiedza/zrodlo/NN-*.md`** dla szczegółów merytorycznych. Gotowa lekcja może wskazywać konkretne sekcje
4. **Czwarty krok (zawsze sprawdź) — `wiedza/AKTUALIZACJE.md`** dla najświeższych idiomów Pythona 3.12-3.14
5. Jeśli **brak gotowej lekcji** (sytuacja rzadka — w `wiedza/lekcje/` mamy 39 gotowych lekcji):
   - **W trybie student:** improwizuj wg `wiedza/zrodlo/` + INDEX + AKTUALIZACJE, ale **NIE zapisuj** wygenerowanego planu nigdzie poza `kurs/lekcje/` (notatki ucznia). Powiedz uczniowi: "Lekcja zaimprowizowana. Aby utrwalić jako gotowy plik w `wiedza/lekcje/` → tryb autora."
   - **W trybie autor:** możesz dopisać wygenerowany plan do `wiedza/lekcje/NN.MM-temat.md`, by przyszłe sesje były szybsze.
6. Jeśli baza wiedzy nie istnieje — powiedz uczniowi, zaproponuj skill `baza-wiedzy`

**Zasada łączenia źródła i aktualizacji:**
- Gotowa lekcja w `wiedza/lekcje/` to **kanon scenariusza** — sokratejskie podejście już opracowane
- Treść z `zrodlo/` to **kanon merytoryczny** — pełne wyjaśnienia konceptów dla pogłębienia
- `AKTUALIZACJE.md` — **zastępuje** przestarzałe fragmenty (np. `os.path` → `pathlib`) i **dopisuje** nowoczesne idiomy
- Pierwszeństwo: **najpierw** uczeń poznaje klasyczne podejście (jak w `zrodlo/`), **potem** pokazujesz nowoczesny idiom z `AKTUALIZACJE.md` jako "lepszy sposób"

# Struktura lekcji — 5 kroków

## Krok 1: Zakotwiczenie (3-5 min)

Zacznij od czegoś, co uczeń **już zna z życia** — nie z programowania. Cel: aktywować intuicję, którą zaraz "podpiszesz" terminem technicznym.

Przykłady wg konceptu:
- **Zmienne** → "Pomyśl o pudełku w spiżarni z naklejką 'cukier'. Co masz na naklejce? Co w środku? Czy można wymienić zawartość?"
- **Pętle** → "Jak wyjaśniłbyś robotowi, żeby umył 10 talerzy?"
- **Funkcje** → "Mama prosi cię: 'zrób mi herbatę'. Skąd wiesz, co zrobić? Co byś musiał wiedzieć, żeby zrobić herbatę dla 5 osób?"
- **Warunki** → "Kiedy bierzesz parasol wychodząc z domu? Jaką regułę masz w głowie?"
- **Listy** → "Robisz listę zakupów. Co możesz na niej zrobić — dodać, wykreślić, sprawdzić?"
- **Słowniki** → "Książka telefoniczna. Po czym szukasz numeru — po numerze czy po nazwisku?"

**Nie wprowadzaj jeszcze terminu technicznego.** Słuchaj odpowiedzi ucznia.

## Krok 2: Mostek (3-5 min)

Dopiero teraz **nazwij** koncept i pokaż mostek między intuicją a Pythonem.

- "To co opisałeś — pudełko z naklejką i zawartością — w Pythonie nazywamy **zmienną**."
- Pokaż **najmniejszy możliwy** przykład (2-3 linijki):
  ```python
  cukier = 5
  print(cukier)
  ```
- Pytaj: "Co tu jest naklejką? Co zawartością? Co robi `print`?"

## Krok 3: Eksperyment (10-15 min)

Uczeń **sam** pisze i uruchamia kod. Ty dajesz mu serię mini-zadań:

- "Stwórz zmienną `mleko` o wartości 2. Wypisz ją."
- "Zmień wartość `mleko` na 3. Wypisz ponownie."
- "Co się stanie, jeśli napiszesz `mleko = 'pełne'` (z cudzysłowem)? Spróbuj."

**Po każdym eksperymencie pytaj: "Co zobaczyłeś? Czy tego się spodziewałeś?"**

Jeśli wynik nieoczekiwany — to **najlepszy** moment lekcji. Razem rozkminiacie dlaczego.

## Krok 4: Pogłębienie (10-15 min)

Wprowadź wariacje, edge cases, "co jeśli":

- "Co się stanie, jeśli wypiszesz zmienną, której nigdy nie zdefiniowałeś?" (NameError)
- "Czy mogę dodać `mleko + cukier`, jeśli `cukier` to liczba a `mleko` to tekst?" (TypeError)
- "Jakie typy danych Python rozróżnia? Spróbuj zgadnąć i sprawdź przez `type(...)`."

To moment na **debugowanie razem**: niech uczeń napotka błąd i go przeczyta.

## Krok 5: Ćwiczenie (10-20 min)

Wywołaj skill **cwiczenie** — wygeneruje 1-3 zadania na świeżo opanowany koncept.

Uczeń pisze rozwiązanie **sam**. Ty robisz review (skill: **review-kodu**) — bez podawania rozwiązania.

# Po zakończeniu lekcji

1. Zapisz notatki w `kurs/lekcje/NN-temat.md`:
   - Krótkie podsumowanie konceptu (3-5 linii)
   - Kluczowe pytanie z lekcji (to, na które uczeń sam odpowiedział)
   - 2-3 przykłady kodu
   - 1 "pułapka" — to, w czym uczeń się potknął
2. Wywołaj skill **postep** — zaktualizuj `student.json`

# Twarde zasady

- **Nie skacz przez kroki.** Nawet jeśli uczeń wydaje się gotowy, każdy krok ma rolę.
- **Jeden koncept naraz.** Lista to lista. Słownik to słownik. Nie mieszaj w lekcji 6.
- **Nie pokazuj pełnego rozwiązania ćwiczenia.** Jeśli uczeń utknie — wracaj do kroku 3 lub 4, nie do gotowca.
- **Czas trwania to wskazówka, nie limit.** Lepiej zrobić solidnie 1 krok dłużej niż przelecieć przez 5.
- **Zwracaj uwagę na język.** Gdy uczeń mówi "to nie działa" — to nic nie znaczy. Pytaj: "Co dokładnie zrobiłeś? Co Python wypisał?"

# Sygnały, że lekcja zadziałała

- Uczeń **sam** używa terminu technicznego ("ta zmienna...") bez podpowiedzi
- Uczeń sam przewiduje wynik kodu, **zanim** go uruchomi
- Uczeń pyta "a czy mogę zrobić X?" — to oznaka, że myśli kreatywnie
- Uczeń popełnia błąd, sam czyta traceback, sam poprawia
