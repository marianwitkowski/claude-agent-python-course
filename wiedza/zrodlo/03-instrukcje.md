## Blok 3: Instrukcje warunkowe i pętle

Poniższy rozdział poświęcony jest kluczowym konstrukcjom logiki programu w Pythonie: instrukcjom warunkowym oraz pętlom. Poznanie tych elementów pozwoli na tworzenie bardziej dynamicznych i interaktywnych programów, które będą w stanie reagować na różne sytuacje i przetwarzać złożone dane. Przyjrzymy się składni oraz zastosowaniom instrukcji `if`, `elif` i `else`, a następnie omówimy dwie podstawowe pętle w Pythonie: `for` oraz `while`. Na koniec zaprezentujemy praktyczne przykłady, które pomogą utrwalić zdobytą wiedzę – między innymi program do zgadywania liczby oraz iterację po elementach listy w celu zsumowania wartości.

---

### 1. Wprowadzenie do instrukcji warunkowych

Instrukcje warunkowe pozwalają na wykonanie określonego fragmentu kodu tylko wtedy, gdy spełniony zostanie dany warunek logiczny. Oznacza to, że program może podejmować decyzje – np. sprawdzić, czy użytkownik wpisał poprawną wartość, czy dany plik istnieje, czy zmienna jest większa od pewnej liczby, i na tej podstawie wybrać odpowiednią ścieżkę działania.

Najważniejszą instrukcją warunkową w Pythonie jest `if`. Jej składnia jest prosta:

```python
if warunek:
    # kod do wykonania, jeśli warunek jest True
```

`warunek` to wyrażenie logiczne, które zwraca wartość `True` lub `False`. Jeśli wyrażenie jest prawdziwe, kod wewnątrz instrukcji `if` zostanie wykonany. Jeśli fałszywe – zostanie pominięty.

---

### 2. Instrukcje `if`, `elif` i `else`

Wiele sytuacji wymaga sprawdzenia nie tylko jednego, ale kilku alternatywnych warunków. W Pythonie używamy do tego `elif` (skrót od else-if), który pozwala zdefiniować kolejne warunki sprawdzane w przypadku, gdy poprzednie nie zostały spełnione. Dodatkowo używamy `else`, gdy chcemy określić co ma się stać, jeśli żaden z wcześniejszych warunków nie był prawdziwy.

Przykładowa konstrukcja:

```python
x = 10

if x > 10:
    print("x jest większy niż 10")
elif x == 10:
    print("x jest równy 10")
else:
    print("x jest mniejszy niż 10")
```

Jak to działa?  
- Najpierw sprawdzany jest `if x > 10`. Jeśli wartość `x` byłaby większa od 10, ten blok by się wykonał, a reszta zostałaby pominięta.  
- Jeśli `x > 10` nie jest prawdziwe, Python sprawdza `elif x == 10`. Jeżeli to będzie prawdą, wykona się kod po `elif`.  
- Jeśli żaden warunek nie zostanie spełniony, wykonujemy kod po `else`.

Instrukcje `if`, `elif`, `else` można łączyć w łańcuchy, sprawdzając wiele różnych warunków. Niezwykle przydatne jest to np. w walidacji danych użytkownika czy sterowaniu logiką biznesową programu.

---

### 3. Pętle `for` – iteracja po sekwencjach

Pętla `for` pozwala wykonać określony blok kodu dla każdego elementu w danej sekwencji (liście, krotce, stringu, zbiorze, słowniku lub innym obiekcie iterowalnym). Dzięki temu można łatwo przetworzyć serię danych, wykonując identyczną operację na każdym elemencie.

Podstawowa składnia:

```python
for element in sekwencja:
    # kod wykonywany dla każdego elementu
```

Przykład:

```python
lista = [1, 2, 3, 4, 5]
for liczba in lista:
    print(liczba * 2)
```

Powyższy kod wypisze kolejno: 2, 4, 6, 8, 10, ponieważ dla każdej liczby z listy wykonamy mnożenie przez 2 i wyświetlenie wyniku.

Innym przykładem może być iteracja po znakach w łańcuchu:

```python
tekst = "Python"
for znak in tekst:
    print(znak)
```

W tym przypadku każdy znak ze słowa "Python" zostanie wyświetlony w osobnej linii.

Pętla `for` jest niezwykle przydatna do iteracji po kolekcjach, tablicach, plikach czy wynikach zapytań do baz danych.

---

### 4. Pętle `while` – iteracja aż do spełnienia warunku

Pętla `while` powtarza wykonanie kodu tak długo, jak długo spełniony jest zadany warunek logiczny. Działa to na zasadzie:

```python
while warunek:
    # kod wykonywany, dopóki warunek jest True
```

Przykład:

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

Ten fragment kodu będzie wyświetlał wartości `0, 1, 2, 3, 4`. Gdy `x` osiągnie wartość 5, warunek `x < 5` przestanie być spełniony, pętla się zakończy, a wykonanie programu przejdzie dalej.

Pętla `while` świetnie sprawdza się, gdy nie jesteśmy z góry pewni, ile razy trzeba wykonać dany blok kodu – na przykład, dopóki użytkownik nie wprowadzi poprawnych danych lub dopóki nie zostanie osiągnięty pewien stan w programie.

---

### 5. Kontrola przepływu w pętlach: `break` i `continue`

Czasem potrzebujemy zakończyć pętlę przed osiągnięciem jej naturalnego końca. Służy do tego słowo kluczowe `break`. Kiedy Python napotka `break` wewnątrz pętli, natychmiast przerywa jej wykonanie i przechodzi dalej.

Przykład użycia `break`:

```python
for liczba in [1, 2, 3, 4, 5]:
    if liczba == 3:
        break
    print(liczba)
```

Ten kod wypisze `1, 2`, a gdy natrafi na `3`, wykona `break` i przerwie pętlę, nie wypisując `3`, `4` czy `5`.

Natomiast `continue` powoduje pominięcie dalszej części kodu wewnątrz pętli dla bieżącej iteracji i przejście do kolejnej iteracji. Przykładowo:

```python
for liczba in [1, 2, 3, 4, 5]:
    if liczba == 3:
        continue
    print(liczba)
```

W tym przypadku kod wypisze `1, 2, 4, 5`, pomijając tylko `3` (dla tej iteracji wykonał `continue`, co spowodowało przejście do następnej wartości).

`break` i `continue` to narzędzia pozwalające na precyzyjne sterowanie przebiegiem pętli.

---

### 6. Praktyczne zastosowania pętli i warunków

Instrukcje warunkowe i pętle to podstawa nie tylko do prostych przykładów, ale również do bardziej praktycznych zastosowań. Oto kilka sytuacji, w których te konstrukcje są niezastąpione:

- **Walidacje danych użytkownika:**  
  Możemy wykorzystać `if` oraz pętle, aby upewnić się, że użytkownik wprowadził poprawne dane. Na przykład, jeśli użytkownik ma wpisać liczbę z pewnego zakresu, pętla `while` może pytać go ponownie tak długo, aż poda poprawną wartość.

- **Iteracje po kolekcjach:**  
  Jeżeli mamy listę cen produktów i chcemy obliczyć ich sumę lub średnią, iteracja `for` po elementach listy w połączeniu z dodawaniem wartości do zmiennej zbiorczej da nam prosty i efektywny sposób na przetwarzanie danych.

- **Filtrowanie danych:**  
  Warunki `if` wewnątrz pętli umożliwiają łatwe filtrowanie elementów, przetwarzając tylko te, które spełniają określone kryteria (np. wypisanie tylko tych liczb z listy, które są parzyste).

---

### 7. Praktyka: Program do zgadywania liczby

Napiszmy prosty program, w którym komputer "pomyśli" sobie liczbę, a użytkownik będzie próbował ją odgadnąć. Zastosujemy pętlę `while` do ponawiania próśb o podanie liczby, aż użytkownik trafi w poprawny wynik lub zrezygnuje.

Przykładowy kod:

```python
import random

sekret = random.randint(1, 10)  # losujemy liczbę z zakresu od 1 do 10
odgadniete = False

print("Zgadnij liczbę od 1 do 10. Wpisz 0, aby się poddać.")

while not odgadniete:
    wybor = input("Podaj liczbę: ")
    
    # Spróbuj skonwertować wpis na liczbę całkowitą
    try:
        liczba = int(wybor)
    except ValueError:
        print("To nie jest liczba. Spróbuj ponownie.")
        continue

    if liczba == 0:
        print("Poddajesz się! Liczba to:", sekret)
        break
    elif liczba == sekret:
        print("Brawo! Odgadłeś liczbę.")
        odgadniete = True
    elif liczba < sekret:
        print("Za mała!")
    else:
        print("Za duża!")
```

W tym programie:
- Używamy modułu `random` do wylosowania liczby.  
- Pętla `while` działa dopóki użytkownik nie odgadnie (zmienna `odgadniete` jest `False`) lub nie przerwie gry.  
- `if`, `elif`, `else` służą do ustalenia, czy wpisana liczba to poprawna próba, za mała, za duża, czy użytkownik się poddał.  
- `continue` wykorzystaliśmy do powtórzenia pętli w razie błędnych danych wejściowych, a `break` do zakończenia gry przy poddaniu.

---

### 8. Praktyka: Iteracja po elementach listy i sumowanie wartości

Załóżmy, że mamy listę liczb i chcemy obliczyć ich sumę. Wykorzystamy pętlę `for` do iteracji po elementach i dodawania ich do zmiennej sumującej.

```python
liczby = [10, 5, 8, 12, 3]
suma = 0

for liczba in liczby:
    suma += liczba

print("Suma liczb to:", suma)
```

Ten kod przejdzie przez całą listę i do zmiennej `suma` będzie dodawał kolejne elementy. Rezultat wypiszemy na końcu.

Możemy także użyć warunków, aby zsumować tylko wybrane wartości, np. tylko te większe od 5:

```python
liczby = [10, 5, 8, 12, 3]
suma_duzych = 0

for liczba in liczby:
    if liczba > 5:
        suma_duzych += liczba

print("Suma liczb większych niż 5 to:", suma_duzych)
```

---

### 9. Najczęstsze błędy i pułapki

- **Błędny warunek w pętli `while`:**  
  Jeśli warunek pętli `while` nigdy nie przestanie być spełniony, pętla stanie się nieskończona. Upewnij się, że wewnątrz pętli zmieniasz wartość zmiennej kontrolującej warunek lub przewidujesz sytuację, w której `break` zakończy pętlę.

- **Niepoprawne wcięcia:**  
  W Pythonie wcięcia decydują o przynależności linii do bloku kodu. Upewnij się, że linie należące do `if`, `elif`, `else` czy ciała pętli są poprawnie wcięte i spójne w całym projekcie.

- **Niewłaściwe użycie `break` i `continue`:**  
  Pamiętaj, że `break` przerywa całkowicie pętlę, a `continue` jedynie pomija dalszy kod dla bieżącej iteracji i przechodzi do następnej. Nie myl tych dwóch instrukcji.

- **Nieodpowiednie warunki porównań:**  
  Upewnij się, że używasz operatorów porównania poprawnie: `==` do porównania wartości, `!=` do sprawdzenia, czy wartości są różne, `>`, `<`, `>=`, `<=` do porównań liczbowych. Jedno równa się (`=`) służy tylko do przypisywania wartości zmiennej.

---

### 10. Podsumowanie i dalsze kroki

W tym rozdziale poznaliśmy kluczowe elementy logiki programów w Pythonie:

- Instrukcje warunkowe `if`, `elif`, `else` pozwalają na podejmowanie decyzji w zależności od spełnienia określonych warunków.
- Pętle `for` i `while` umożliwiają wielokrotne wykonanie fragmentu kodu – czy to iterując po elementach sekwencji, czy też powtarzając czynność do momentu osiągnięcia pożądanego stanu.
- Nauczyliśmy się praktycznego zastosowania pętli i warunków, tworząc prosty program do zgadywania liczby i iterując po liście w celu zsumowania jej elementów.
- Poznaliśmy instrukcje `break` i `continue` do bardziej elastycznego sterowania przebiegiem pętli.

Te umiejętności są niezbędne do tworzenia funkcjonalnych, interaktywnych i elastycznych programów. W kolejnych rozdziałach przejdziemy do jeszcze bardziej zaawansowanych zagadnień, takich jak struktury danych, funkcje, a także programowanie obiektowe. Zrozumienie podstaw warunków i pętli jest fundamentem, na którym będziemy budować coraz bardziej skomplikowane logiki oprogramowania. Utrwal tę wiedzę, eksperymentując z własnymi przykładami, modyfikując kod i szukając kreatywnych zastosowań.

----

© 2024 Marian Witkowski
