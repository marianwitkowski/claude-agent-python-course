## Blok 7: Programowanie obiektowe (OOP)

Poniższy rozdział poświęcony jest podstawowym pojęciom programowania obiektowego (OOP) w Pythonie. Omówimy, czym są klasy i obiekty, w jaki sposób tworzyć i wykorzystywać konstruktory oraz definiować atrybuty i metody. Następnie przyjrzymy się dziedziczeniu i polimorfizmowi, dwóm kluczowym cechom programowania obiektowego, które pozwalają na tworzenie elastycznych i wielokrotnie używalnych komponentów oprogramowania. Na koniec zaprezentujemy przykłady prostych wzorców projektowych, które pomagają w organizacji kodu i budowaniu skalowalnych systemów. W części praktycznej zajmiemy się implementacją klasy reprezentującej konto bankowe lub produkt w sklepie internetowym oraz stworzymy prosty system zarządzania tymi obiektami.

---

### 1. Wprowadzenie do programowania obiektowego

**Programowanie obiektowe (OOP)** to paradygmat, w którym program składa się z obiektów – „klocków” reprezentujących elementy świata rzeczywistego lub abstrakcji biznesowych. Zamiast skupiać się na sekwencji instrukcji, OOP kładzie nacisk na strukturę i powiązania pomiędzy obiektami.

Python od początku wspiera OOP, oferując klasom i obiektom wszechstronne możliwości. Dzięki temu tworzenie i zarządzanie bardziej złożonymi programami staje się prostsze i bardziej intuicyjne.

Cechy charakterystyczne OOP:

- **Abstrakcja:** ukrywanie szczegółów implementacyjnych za interfejsem klasy.
- **Hermetyzacja (enkapsulacja):** łączenie danych (atrybutów) i operacji na nich (metod) w spójne jednostki (obiekty).
- **Dziedziczenie:** możliwość tworzenia nowych klas w oparciu o istniejące.
- **Polimorfizm:** możliwość jednolitego traktowania obiektów różnych klas, które realizują to samo „interfejsowe” zachowanie.

---

### 2. Klasy i obiekty w Pythonie

W Pythonie klasa to wzorzec (szablon) definiujący strukturę i zachowanie obiektów, które z niej powstaną. Obiekt jest konkretną instancją klasy, czyli „żywym” egzemplarzem, który posiada swoje własne dane i potrafi wykonywać operacje zdefiniowane przez klasę.

Definicja klasy w Pythonie wygląda następująco:

```python
class NazwaKlasy:
    # ciało klasy, definicje atrybutów i metod
    pass
```

Słowo kluczowe `class` wprowadza nową klasę, a `pass` służy jako wypełniacz, jeśli nie mamy jeszcze żadnej zawartości. Z takiej pustej klasy można tworzyć obiekty:

```python
class Produkt:
    pass

p = Produkt()
print(p)  # <__main__.Produkt object at 0x...>
```

`p` jest obiektem klasy `Produkt`. Na razie klasa nic nie robi, ale jest to już pierwszy krok do programowania obiektowego.

---

### 3. Konstruktory (`__init__`), atrybuty i metody

Klasy w Pythonie mają specjalną metodę `__init__`, nazywaną konstruktorem, która wywoływana jest automatycznie w momencie tworzenia obiektu. To idealne miejsce, by zainicjalizować wartości atrybutów obiektu.

Atrybuty to zmienne związane z obiektem, przechowujące jego stan. Metody to funkcje zdefiniowane wewnątrz klasy, które operują na atrybutach danego obiektu lub wykonują określone działania.

Przykład:

```python
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def wyswietl_info(self):
        print(f"Produkt: {self.nazwa}, Cena: {self.cena} zł")

p = Produkt("Chleb", 3.50)
p.wyswietl_info()  # Produkt: Chleb, Cena: 3.5 zł
```

`self` to odwołanie do konkretnego obiektu, na którym wywoływana jest metoda. Zawsze jest pierwszym argumentem metod instancji (poza metodami statycznymi i klasowymi, o których tutaj nieco mniej), ale wywołując metody, nie podajemy go jawnie:

```python
p.wyswietl_info()
```

Interpreter sam przekaże `p` jako argument `self`.

---

### 4. Dziedziczenie

Dziedziczenie umożliwia tworzenie nowych klas na bazie już istniejących. Pozwala to na ponowne wykorzystanie kodu, rozszerzanie i modyfikowanie zachowania klas bez konieczności pisania wszystkiego od nowa. Nowa klasa, zwana klasą pochodną (lub podklasą), może korzystać z atrybutów i metod klasy bazowej (nadklasy), a także je nadpisywać i dodawać własne.

Przykład:

```python
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def wyswietl_info(self):
        print(f"Produkt: {self.nazwa}, Cena: {self.cena} zł")

class ProduktSpozywczy(Produkt):
    def __init__(self, nazwa, cena, data_waznosci):
        super().__init__(nazwa, cena)  # wywołanie konstruktora klasy bazowej
        self.data_waznosci = data_waznosci

    def wyswietl_info(self):
        super().wyswietl_info()
        print(f"Data ważności: {self.data_waznosci}")
```

`ProduktSpozywczy` dziedziczy po `Produkt`, dodając atrybut `data_waznosci` oraz nadpisując metodę `wyswietl_info`, by wyświetlać dodatkową informację.

---

### 5. Polimorfizm

Polimorfizm pozwala traktować obiekty różnych klas w taki sam sposób, o ile spełniają one te same interfejsy (czyli mają te same metody). Dzięki polimorfizmowi możemy pisać funkcje czy pętle, które operują na obiektach, nie wiedząc, jakiej dokładnie są klasy – ważne, by miały określone metody.

Przykładowo:

```python
class Produkt:
    def wyswietl_info(self):
        print("Jestem produktem")

class ProduktElektroniczny(Produkt):
    def wyswietl_info(self):
        print("Jestem produktem elektronicznym")

class ProduktSpozywczy(Produkt):
    def wyswietl_info(self):
        print("Jestem produktem spożywczym")

produkty = [Produkt(), ProduktElektroniczny(), ProduktSpozywczy()]

for p in produkty:
    p.wyswietl_info()
```

W powyższym kodzie `for p in produkty:` iteruje po różnych obiektach. Każdy z nich ma metodę `wyswietl_info()`, ale każda klasa implementuje ją inaczej. Polimorfizm pozwala nam jednak traktować je jednolicie.

---

### 6. Hermetyzacja i atrybuty prywatne

W Pythonie nie ma ścisłego wymuszenia prywatności jak w C++ czy Javie. Konwencja jednak nakazuje:

- Atrybuty bez podkreślników są publiczne.
- Atrybut z jednym podkreślnikiem, np. `_cena`, sugeruje, że jest to atrybut do użytku wewnętrznego.
- Atrybut z dwoma podkreślnikami, np. `__cena`, uruchamia mechanizm name mangling, który utrudnia (choć nie uniemożliwia) bezpośredni dostęp z zewnątrz.

Przykład:

```python
class KontoBankowe:
    def __init__(self, numer, saldo=0):
        self._numer = numer    # atrybut "chroniony" (umowna konwencja)
        self.__saldo = saldo   # atrybut ze zmanglowaną nazwą

    def wplata(self, kwota):
        self.__saldo += kwota

    def wyplata(self, kwota):
        if kwota <= self.__saldo:
            self.__saldo -= kwota
        else:
            print("Brak środków.")

    def wyswietl_saldo(self):
        print(f"Saldo konta {self._numer}: {self.__saldo} zł")
```

Choć w Pythonie można się dostać do `__saldo` (przez `_KontoBankowe__saldo`), konwencja zachęca do unikania tego i traktowania takich atrybutów jako prywatnych.

---

### 7. Wzorce projektowe na prostym przykładzie

Wzorce projektowe to sprawdzone sposoby rozwiązywania powtarzalnych problemów w projektach programistycznych. Przykładem wzorca jest **Singleton**, zapewniający, że istnieje tylko jedna instancja danej klasy.

Przykład prostego Singletona w Pythonie (nie jest to idealne rozwiązanie, a raczej ilustracja idei):

```python
class Singleton:
    _instancja = None

    def __new__(cls, *args, **kwargs):
        if cls._instancja is None:
            cls._instancja = super(Singleton, cls).__new__(cls)
        return cls._instancja

# Wszystkie obiekty tej klasy będą wskazywać na tę samą instancję.
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

Innym popularnym wzorcem jest **Fasada (Facade)**, który upraszcza interfejs do złożonego systemu lub **Adapter**, który pozwala dostosować interfejs jednej klasy do innej. Poznanie i stosowanie wzorców projektowych zwiększa jakość kodu i ułatwia jego rozwój.

---

### 8. Praktyka: Implementacja klasy reprezentującej konto bankowe

Spróbujmy w praktyce zaprojektować klasę `KontoBankowe`. Załóżmy, że potrzebujemy:

- Numeru konta
- Salda
- Metod do wpłaty i wypłaty
- Metody wyświetlającej saldo

Kod przykładowy:

```python
class KontoBankowe:
    def __init__(self, numer, saldo=0.0):
        self.numer = numer
        self.saldo = saldo

    def wplata(self, kwota):
        self.saldo += kwota

    def wyplata(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
        else:
            print("Brak wystarczających środków")

    def wyswietl_saldo(self):
        print(f"Konto {self.numer}, saldo: {self.saldo:.2f} zł")

# Tworzymy obiekt
konto = KontoBankowe("PL1234567890", 1000.0)
konto.wyswietl_saldo()  # saldo: 1000.00 zł
konto.wplata(200)
konto.wyplata(50)
konto.wyswietl_saldo()  # saldo: 1150.00 zł
```

Taki kod jest czytelny i logiczny: `konto` jest obiektem, który posiada swoje dane (`numer`, `saldo`) i metody do zarządzania nimi.

---

### 9. Praktyka: Produkt w sklepie internetowym i zarządzanie obiektami

Napiszmy klasę `Produkt` (jak wcześniej), a potem listę takich produktów. Wyobraźmy sobie, że chcemy przechowywać w liście różne produkty i mieć metody do ich przetwarzania, np. szukania najdroższego produktu.

```python
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def wyswietl_info(self):
        print(f"{self.nazwa} - {self.cena} zł")

class Sklep:
    def __init__(self):
        self.produkty = []

    def dodaj_produkt(self, p: Produkt):
        self.produkty.append(p)

    def najdrozszy_produkt(self):
        if not self.produkty:
            return None
        # Zwracamy produkt o najwyższej cenie
        return max(self.produkty, key=lambda p: p.cena)

    def wyswietl_asortyment(self):
        for p in self.produkty:
            p.wyswietl_info()

# Przykładowe użycie
sklep = Sklep()
sklep.dodaj_produkt(Produkt("Chleb", 3.50))
sklep.dodaj_produkt(Produkt("Masło", 6.00))
sklep.dodaj_produkt(Produkt("Czekolada", 4.50))

sklep.wyswietl_asortyment()
najdrozszy = sklep.najdrozszy_produkt()
print("Najdroższy produkt:")
najdrozszy.wyswietl_info()
```

Mamy tutaj prosty system zarządzania obiektami – lista produktów w klasie `Sklep`, metody do dodawania produktów i wyszukiwania najdroższego.

---

### 10. Dziedziczenie na przykładzie produktów spożywczych i elektronicznych

Możemy rozszerzyć nasz przykład sklepu. Załóżmy, że chcemy w asortymencie mieć również produkty spożywcze z datą ważności i produkty elektroniczne z gwarancją. Wykorzystamy dziedziczenie, aby uniknąć powtarzania kodu.

```python
class ProduktSpozywczy(Produkt):
    def __init__(self, nazwa, cena, data_waznosci):
        super().__init__(nazwa, cena)
        self.data_waznosci = data_waznosci

    def wyswietl_info(self):
        super().wyswietl_info()
        print(f"Data ważności: {self.data_waznosci}")

class ProduktElektroniczny(Produkt):
    def __init__(self, nazwa, cena, gwarancja_mce):
        super().__init__(nazwa, cena)
        self.gwarancja_mce = gwarancja_mce

    def wyswietl_info(self):
        super().wyswietl_info()
        print(f"Gwarancja: {self.gwarancja_mce} miesięcy")

sklep = Sklep()
sklep.dodaj_produkt(ProduktSpozywczy("Jabłka", 5.00, "2024-07-01"))
sklep.dodaj_produkt(ProduktElektroniczny("Smartfon", 1500.00, 24))
sklep.wyswietl_asortyment()
```

Teraz nasz sklep może zawierać różne typy produktów, a wszystkie zachowują się spójnie, co jest zasługą polimorfizmu. Każdy produkt ma `wyswietl_info()`, a klasa `Sklep` nie musi wiedzieć, jaki to dokładnie rodzaj produktu – wystarczy wywołać tę metodę.

---

### 11. Rozbudowany przykład: prosty wzorzec projektowy

Weźmy prosty wzorzec – **Fabryka (Factory)**. Załóżmy, że zależnie od jakiegoś warunku chcemy tworzyć różne produkty, ale nie chcemy martwić się w kodzie głównym o szczegóły ich tworzenia.

```python
class ProduktFactory:
    @staticmethod
    def stworz_produkt(rodzaj, nazwa, cena, **kwargs):
        if rodzaj == "spożywczy":
            return ProduktSpozywczy(nazwa, cena, kwargs.get("data_waznosci", "nieznana"))
        elif rodzaj == "elektroniczny":
            return ProduktElektroniczny(nazwa, cena, kwargs.get("gwarancja_mce", 12))
        else:
            return Produkt(nazwa, cena)

sklep = Sklep()
sklep.dodaj_produkt(ProduktFactory.stworz_produkt("spożywczy", "Ser", 8.00, data_waznosci="2023-12-31"))
sklep.dodaj_produkt(ProduktFactory.stworz_produkt("elektroniczny", "Laptop", 3000.00, gwarancja_mce=36))
sklep.wyswietl_asortyment()
```

Fabryka pozwala uprościć logikę tworzenia obiektów w kodzie głównym.

---

### 12. Podsumowanie i dalsze kroki

W tym rozdziale poznałeś fundamenty programowania obiektowego w Pythonie:

- Czym są klasy i obiekty, oraz jak je definiować.
- Jak działa konstruktor `__init__`, atrybuty i metody.
- Jak wykorzystać dziedziczenie do tworzenia hierarchii klas oraz polimorfizm do wspólnego traktowania różnych obiektów.
- Jak stosować proste wzorce projektowe, takie jak Singleton czy Fabryka, aby organizować kod w bardziej elastyczny i łatwy do utrzymania sposób.

Praktyczna część pokazała, jak napisać klasę reprezentującą konto bankowe, produkty w sklepie oraz system zarządzania obiektami. Poznałeś, jak można rozszerzać funkcjonalność klas i stosować polimorfizm.

W dalszym ciągu warto zgłębiać programowanie obiektowe, poznawać bardziej zaawansowane wzorce projektowe, w tym te opisane przez GoF (Gang of Four), oraz uczyć się dobrych praktyk projektowych. W kolejnych rozdziałach i etapach nauki zajmiemy się kolejnymi aspektami Pythona i tworzenia skalowalnego, czystego kodu. Regularne praktykowanie OOP i wzorców projektowych pomoże w budowaniu coraz bardziej profesjonalnego i łatwiejszego w utrzymaniu oprogramowania.

----

© 2024 Marian Witkowski
