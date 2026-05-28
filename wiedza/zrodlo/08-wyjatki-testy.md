## Blok 8: Obsługa wyjątków i testowanie

Poniższy rozdział dotyczy jednych z najważniejszych aspektów profesjonalnego programowania: obsługi wyjątków i testowania oprogramowania. Poznasz mechanizmy pozwalające na wykrywanie i reagowanie na błędy (wyjątki), dowiesz się, jak tworzyć własne wyjątki i w jaki sposób zadbać o to, by kod był bardziej odporny na nieprzewidziane sytuacje. Następnie przejdziemy do podstaw testów jednostkowych, korzystając z modułu `unittest` dostępnego w standardowej bibliotece Pythona. Omówimy także znaczenie testów w procesie rozwoju oprogramowania, przyglądając się praktykom TDD (Test-Driven Development).

W części praktycznej napiszemy przykłady skryptów do przetwarzania danych, które obsługują błędy, oraz proste testy jednostkowe, które pomogą Ci zweryfikować poprawność kodu i zwiększyć pewność, że wprowadzane zmiany nie psują istniejącej funkcjonalności.

---

### 1. Czym są wyjątki i po co je stosować?

Wyjątki to mechanizm pozwalający przerwać normalny przebieg programu, gdy napotka on sytuację, której nie potrafi obsłużyć w standardowy sposób – np. brak pliku wejściowego, błąd w formacie danych, próba dzielenia przez zero czy brak połączenia z bazą danych. Zamiast pozwolić, aby program zakończył się w niekontrolowany sposób, wyjątki pozwalają przechwycić i obsłużyć błąd w kontrolowany, przewidywalny sposób.

W Pythonie każdy typ błędu (np. `ValueError`, `TypeError`, `FileNotFoundError`) jest reprezentowany jako klasa wyjątku. Dzięki temu można:
- Zidentyfikować rodzaj błędu po typie wyjątku.
- Przechwycić konkretne typy błędów i obsłużyć je inaczej niż ogólne błędy.
- Łatwo dziedziczyć i tworzyć własne wyjątki dopasowane do domeny problemu.

---

### 2. Rzucanie wyjątków za pomocą `raise`

Aby celowo wywołać wyjątek, można użyć instrukcji `raise`. Pozwala to zasygnalizować, że w danym punkcie kodu wystąpiła sytuacja, której nie da się sensownie kontynuować bez uwzględnienia błędu.

Przykład:

```python
def dziel(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero jest niedozwolone!")
    return a / b

# Wywołanie:
# wynik = dziel(10, 0)
# spowoduje zgłoszenie wyjątku ZeroDivisionError
```

Można także tworzyć własne komunikaty i tym samym zwiększyć czytelność oraz zrozumienie błędów. W dużych projektach `raise` jest kluczowym narzędziem do zachowania spójności i czytelności obsługi błędów.

---

### 3. Obsługa wyjątków: `try-except`, `finally`

Gdy istnieje prawdopodobieństwo wystąpienia błędu, można użyć bloku `try-except` do przechwycenia wyjątku i wykonania alternatywnych akcji.

Przykład:

```python
try:
    wynik = dziel(10, 0)
    print("Wynik dzielenia:", wynik)
except ZeroDivisionError as e:
    print("Wystąpił błąd:", e)
```

W powyższym kodzie, jeśli `dziel(10, 0)` wywoła wyjątek `ZeroDivisionError`, instrukcje w bloku `except` zostaną wykonane, zamiast wywołania błędu kończącego program.

Możemy użyć wielu bloków `except`, aby obsłużyć różne typy błędów:

```python
try:
    wynik = dziel(10, "pięć")
except ZeroDivisionError:
    print("Dzielenie przez zero!")
except TypeError:
    print("Zły typ argumentów!")
```

Jeżeli chcemy wykonać kod czyszczący zasoby niezależnie od tego, czy wyjątek wystąpił czy nie, używamy `finally`:

```python
plik = None
try:
    plik = open("dane.txt", "r")
    # przetwarzanie danych
except FileNotFoundError:
    print("Nie znaleziono pliku.")
finally:
    if plik:
        plik.close()
```

`finally` wykona się zawsze, nawet jeśli wystąpił wyjątek lub użyto `return` w bloku `try`.

---

### 4. Tworzenie własnych wyjątków

Własne wyjątki pomagają lepiej dopasować obsługę błędów do logiki biznesowej. Możesz stworzyć własną klasę wyjątku, dziedzicząc po wbudowanej klasie `Exception`.

```python
class BlednaCenaException(Exception):
    pass

def ustaw_cene(cena):
    if cena < 0:
        raise BlednaCenaException("Cena nie może być ujemna!")
    print("Cena ustawiona na:", cena)
```

Teraz możesz obsłużyć ten specyficzny wyjątek:

```python
try:
    ustaw_cene(-10)
except BlednaCenaException as e:
    print("Błąd ustawiania ceny:", e)
```

Własne wyjątki pomagają w rozdzieleniu logiki błędów dziedzinowych od ogólnych i poprawiają czytelność kodu.

---

### 5. Wprowadzenie do testów jednostkowych

**Testy jednostkowe (unit tests)** to małe testy sprawdzające poszczególne fragmenty kodu (np. funkcje, metody) w izolacji od reszty systemu. Mają na celu upewnienie się, że dana jednostka działa zgodnie z założeniami i nadal będzie działać poprawnie po wprowadzeniu zmian w kodzie.

Korzyści z testów jednostkowych:

- Wykrywanie błędów na wczesnym etapie rozwoju.
- Łatwiejsze wprowadzanie zmian w kodzie bez obawy, że coś się zepsuje (regresje).
- Dokumentacja: testy pokazują, jak kod ma się zachowywać w różnych scenariuszach.
- Wsparcie dla TDD (Test-Driven Development), gdzie piszemy testy jeszcze przed implementacją, co pomaga w precyzyjnym określeniu wymagań.

---

### 6. Moduł `unittest` w Pythonie

Python posiada wbudowany moduł `unittest`, który udostępnia narzędzia do pisania i uruchamiania testów jednostkowych. Podstawowe elementy `unittest`:

- Klasy testowe dziedziczą po `unittest.TestCase`.
- Metody testowe to te, których nazwa zaczyna się od `test_`.
- `assert`-metody, takie jak `assertEqual`, `assertTrue`, `assertRaises`, pozwalają sprawdzić, czy otrzymany wynik jest zgodny z oczekiwaniami.

Przykład prostego testu:

```python
import unittest

def dodaj(a, b):
    return a + b

class TestDodawania(unittest.TestCase):
    def test_dodawanie_dodatnich(self):
        self.assertEqual(dodaj(2, 3), 5)

    def test_dodawanie_ujemnych(self):
        self.assertEqual(dodaj(-2, -3), -5)

if __name__ == "__main__":
    unittest.main()
```

Uruchamiając ten kod, `unittest` wykona testy i poinformuje nas, czy wszystko działa poprawnie.

---

### 7. Rola testów i podstawy TDD (Test-Driven Development)

**Test-Driven Development (TDD)** to metodologia, w której piszemy testy jeszcze przed napisaniem właściwego kodu. Cykl TDD składa się z trzech kroków:

1. **Red:** Napisz test, który nie przechodzi (bo nie ma jeszcze implementacji).
2. **Green:** Napisz minimalny kod, aby test przeszedł.
3. **Refactor:** Usprawnij kod, zachowując przechodzenie testów.

Ten styl pracy pomaga w precyzyjnym określeniu wymagań i zapewnieniu wysokiej jakości kodu. Programista najpierw definiuje, co kod ma robić (przez testy), a dopiero potem pisze implementację.

---

### 8. Obsługa wyjątków w testach jednostkowych

`unittest` umożliwia sprawdzanie, czy dana funkcja rzuca określony wyjątek w oczekiwanych warunkach. Służy do tego m.in. `assertRaises`:

```python
import unittest

def dziel(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero!")
    return a / b

class TestDzielenia(unittest.TestCase):
    def test_dzielenie_przez_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dziel(10, 0)

if __name__ == "__main__":
    unittest.main()
```

Dzięki temu można testować nie tylko poprawne działanie kodu, ale i to, czy zgłasza odpowiednie wyjątki w sytuacjach błędnych.

---

### 9. Przykład praktyczny: obsługa błędów w skryptach do przetwarzania danych

Załóżmy, że mamy funkcję przetwarzającą dane z pliku CSV, gdzie kolumna z cenami musi być liczbą. Jeśli natrafimy na błędny format, chcemy to obsłużyć. Stworzymy wyjątek `BledneDaneException` i użyjemy go w kodzie, a następnie napiszemy testy.

```python
class BledneDaneException(Exception):
    pass

def przetworz_dane(linie):
    """
    linie to lista linii CSV w formacie: nazwa; cena
    """
    produkty = []
    for linia in linie:
        nazwa, cena_str = linia.strip().split(";")
        try:
            cena = float(cena_str)
        except ValueError:
            raise BledneDaneException(f"Błędny format ceny: {cena_str}")
        produkty.append((nazwa, cena))
    return produkty
```

Testowanie tej funkcji:

```python
import unittest

class TestPrzetwarzaniaDanych(unittest.TestCase):
    def test_poprawne_dane(self):
        dane = ["Chleb;3.50", "Maslo;5.00"]
        wynik = przetworz_dane(dane)
        self.assertEqual(len(wynik), 2)
        self.assertEqual(wynik[0], ("Chleb", 3.50))

    def test_bledny_format_ceny(self):
        dane = ["Jablko;trzy"]
        with self.assertRaises(BledneDaneException):
            przetworz_dane(dane)

if __name__ == "__main__":
    unittest.main()
```

Testy sprawdzą zarówno poprawne działanie, jak i obsługę błędów.

---

### 10. Uruchamianie testów w PyCharm

PyCharm integruje się z `unittest`, pozwalając na wygodne uruchamianie testów i przeglądanie wyników. Aby uruchomić testy:

- Umieść testy w pliku (np. `test_przetwarzanie.py`).
- Otwórz plik w PyCharm.
- Kliknij prawym przyciskiem myszy na nazwie klasy testowej lub funkcji testowej i wybierz „Run <test>”.
- Wyniki testów pojawią się w panelu „Run”, pokazując, które testy przeszły, a które nie.

Dzięki integracji z IDE, testowanie staje się prostsze i bardziej interaktywne.

---

### 11. Rozszerzone możliwości testów i TDD w praktyce

Wraz ze wzrostem projektu można:

- Dodawać kolejne testy pokrywające nowe funkcjonalności.
- Stosować TDD: najpierw napisać test, który definiuje oczekiwanie, a dopiero potem kod, który test zrealizuje.
- Używać `setUp` i `tearDown` w klasach testowych, aby przygotować środowisko testowe przed każdym testem i posprzątać po nim.
- Łączyć testy jednostkowe z testami integracyjnymi, a w większych projektach stosować narzędzia do raportowania pokrycia kodu testami (coverage) czy do ciągłej integracji (CI/CD).

Najważniejsze to systematycznie pisać testy wraz z rozwojem kodu, aby unikać sytuacji, w której rozległy, nietestowany kod trudno zrefaktoryzować i utrzymać.

---

### 12. Podsumowanie i dalsze kroki

W tym rozdziale nauczyłeś się:

- Jak rzucać i obsługiwać wyjątki w Pythonie, by tworzyć bardziej odporny kod.
- Jak definiować własne wyjątki, dostosowane do konkretnej domeny problemu.
- Czym są testy jednostkowe, jak je pisać w Pythonie przy pomocy `unittest`.
- Jak testować obsługę wyjątków i wykorzystywać testy do zwiększenia jakości i pewności kodu.
- Jaka jest rola testów w procesie tworzenia oprogramowania i jak podstawy TDD mogą pomóc w lepszym projektowaniu systemów.

Testy jednostkowe i kontrolowana obsługa błędów to kluczowe elementy profesjonalnego programowania. Ich stosowanie zwiększa stabilność aplikacji, ułatwia wprowadzanie zmian oraz współpracę w zespole, a także skraca czas diagnozowania problemów. W dalszych blokach będziesz mógł rozwijać te umiejętności, łącząc je z pozostałymi elementami ekosystemu Pythona i najlepszymi praktykami inżynierii oprogramowania.

----

© 2024 Marian Witkowski
