---
name: quiz
description: Przeprowadza krótki quiz powtórkowy (3-7 pytań) z ukończonych przez ucznia lekcji. Trzy tryby — szybki (3 pyt), pełny (5-7 pyt), słabe punkty (z `do_powtorki`). Pyta jedno pytanie naraz, czeka na odpowiedź, daje sokratejski feedback. Użyj gdy uczeń mówi "quiz", "powtórka", "sprawdź mnie", między lekcjami lub gdy przerwa była >7 dni.
---

# Cel

Utrwalić wiedzę z **ukończonych** lekcji przez krótkie, interaktywne pytania. Quiz to **diagnoza**, nie egzamin — chodzi o wyłapanie luk, nie ocenianie.

# Trzy tryby

| Tryb            | Liczba pytań | Z jakich lekcji                                  | Kiedy                                    |
| --------------- | ------------ | ------------------------------------------------ | ---------------------------------------- |
| Szybki ⚡       | 3            | 1-2 ostatnio ukończone lekcje                    | Rozgrzewka na początku sesji             |
| Pełny 📋        | 5-7          | Wszystkie ukończone lekcje (losowy mix)          | Co kilka lekcji, na życzenie ucznia      |
| Słabe punkty 🎯 | 3-5          | Tematy z `do_powtorki` w `student.json`          | Gdy lista `do_powtorki` ma ≥3 pozycje    |

Domyślny tryb przy "quiz" bez doprecyzowania: **szybki**.

# Procedura

## Krok 1: wybór zakresu

1. Odczytaj `postep/student.json` (skill: **postep**)
2. Sprawdź `ukonczone_lekcje` i `do_powtorki`
3. Jeśli `ukonczone_lekcje` ma <2 pozycje → powiedz uczniowi, że jest za wcześnie na quiz, zaproponuj lekcję
4. Wybierz tryb (na podstawie prośby ucznia lub kontekstu)

## Krok 2: dobór pytań

Mieszaj **3 rodzaje** pytań — nie tylko jeden:

### A. Pytanie o przewidywanie wyniku ("co wypisze ten kod?")
```
Co wypisze ten kod?

x = 5
y = "3"
print(x + int(y))
```
Sprawdza: rozumienie typów, rzutowania, kolejności wykonania.

### B. Pytanie konceptualne ("dlaczego/kiedy")
> Kiedy użyjesz pętli `while` zamiast `for`?

Sprawdza: zrozumienie, nie zapamiętanie.

### C. Pytanie "popraw kod" / "znajdź błąd"
```
Co jest nie tak z tym kodem? (logicznie, nie składniowo)

for i in range(5):
    print(i)
print(i + 1)
```
Sprawdza: czujność, czytanie cudzego kodu.

**Proporcja w pełnym quizie:** ~40% A, ~30% B, ~30% C.

## Krok 3: prowadzenie quizu

**Jedno pytanie naraz.** Nie wrzucaj 5 pytań w jednym komunikacie.

Schemat dla każdego pytania:

1. Podaj pytanie (z numerem: "Pytanie 2/5")
2. **Poczekaj** na odpowiedź ucznia
3. Po odpowiedzi:
   - Jeśli **poprawna** → krótkie potwierdzenie + jedno pytanie pogłębiające ("A co by się stało, gdyby `y` było `'abc'` zamiast `'3'`?")
   - Jeśli **częściowo** → sokratejskie naprowadzenie ("Blisko. Spójrz na typ `y` przed `int(y)` — co tam jest?")
   - Jeśli **błędna** → NIE podawaj odpowiedzi. Naprowadź pytaniem. Po 2 nieudanych próbach pokaż odpowiedź i dopisz temat do `do_powtorki`
4. Przejdź do następnego pytania

**Nie pokazuj wyniku punktowego po każdym pytaniu** — to nie jest test.

## Krok 4: podsumowanie

Po wszystkich pytaniach:

- Powiedz, ile było **na pewno OK**, ile **z pomocą**, ile **do powtórki**
- Wymień konkretnie 1-2 tematy, które warto utrwalić
- Jeśli uczeń zaliczył tematy, które miał w `do_powtorki` → wywołaj skill **postep**, usuń je z listy
- Jeśli pojawiły się nowe luki → wywołaj **postep**, dopisz do `do_powtorki`
- Zaproponuj następny krok: "Wracamy do lekcji X" albo "Krótkie ćwiczenie na [temat]?"

# Bank pytań — przykłady według lekcji

Pytania **generuj na żywo** dopasowane do tego, co uczeń przerobił. Poniżej szablony jako inspiracja:

## Lekcja 1 (print, błędy)
- A: Co wypisze `print("2" + "3")`?
- B: Co Python pokazuje, gdy program ma błąd? Jak nazywa się ta wiadomość?
- C: Dlaczego ten kod nie działa? `print(Witaj)`

## Lekcja 2 (zmienne, typy)
- A: Po `x = 5` i `x = "kot"` — czy `x` to liczba czy tekst?
- B: Czym różni się `int` od `float`? Daj przykład wartości każdego.
- C: Co jest nie tak? `wiek = "30"; print(wiek + 5)`

## Lekcja 4 (if/elif/else)
- A: Co wypisze? `x = 10; if x > 5: print("a"); elif x > 8: print("b")`
- B: Kiedy warto użyć `elif` zamiast kilku osobnych `if`?
- C: Popraw: `if x = 5: print("ok")`

## Lekcja 5 (pętle)
- A: Ile razy wykona się ta pętla? `for i in range(2, 8, 2): print(i)`
- B: Kiedy `while` ma sens, a kiedy lepiej `for`?
- C: Co jest nie tak? `i = 0; while i < 10: print(i)`

## Lekcja 6 (listy)
- A: Co wypisze? `l = [1,2,3,4]; print(l[1:3])`
- B: Czym różni się `append` od `extend`?
- C: Dlaczego `l = [1,2,3]; l[5] = 9` rzuca błąd?

## Lekcja 8 (funkcje)
- A: Co wypisze? `def f(x): return x*2\nprint(f(3) + f(4))`
- B: Po co w ogóle piszemy funkcje, skoro można wpisać kod bezpośrednio?
- C: Co jest nie tak? `def suma(a,b): a + b` (i wywołanie `print(suma(2,3))`)

# Twarde zasady

- **Tylko ukończone lekcje.** Nie pytaj o materiał, którego uczeń jeszcze nie miał.
- **Jedno pytanie naraz.** Czekanie na odpowiedź jest częścią quizu.
- **Sokratejskie naprowadzanie**, nie podpowiedzi typu "to chyba `int`". Pytaj.
- **Bez ocen liczbowych** ("5/7", "70%"). Mów jakościowo: "3 na pewno, 2 z pomocą, 1 do powtórki".
- **Aktualizuj `student.json`** przez skill **postep** po każdym quizie — co weszło do `do_powtorki`, co z niej zniknęło.
- **Quiz to nie lekcja.** Jeśli wynik pokazuje dużą lukę, zaproponuj wrócenie do lekcji, ale nie tłumacz materiału w trakcie quizu.

# Gdy uczeń wszystko wie

Jeśli uczeń odpowiada od strzału na wszystkie pytania:
- Pochwal konkretnie
- Zaproponuj **gwiazdkowe** ćwiczenie z bieżącej lekcji (skill: **cwiczenie**)
- Lub przyspiesz przejście do kolejnej lekcji

# Gdy uczeń się "rozsypuje"

Jeśli >50% pytań idzie źle:
- Przerwij quiz po 3-4 pytaniach (nie męcz)
- Powiedz wprost: "Widzę, że temat X wymaga powtórki — wróćmy do lekcji N"
- Dopisz tematy do `do_powtorki`
- NIE rób z tego porażki — to diagnoza, którą zrobiliście razem
