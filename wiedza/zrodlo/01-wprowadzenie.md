## Blok 1: Wprowadzenie i przygotowanie środowiska

Poniższy rozdział stanowi pierwszą część kursu, wprowadzającą w podstawy środowiska i przygotowanie do pracy z językiem Python. Skupimy się na zrozumieniu, czym jest Python, skąd się wziął, do czego jest wykorzystywany, a następnie przejdziemy przez proces instalacji zarówno samego interpretera Pythona, jak i środowiska programistycznego PyCharm Community Edition. Poznamy także podstawowe elementy interfejsu tego IDE i dowiemy się, jak rozpocząć swój pierwszy projekt. W części praktycznej spróbujemy napisać i uruchomić prosty program typu „Hello World”, co pozwoli nam zrozumieć cały proces tworzenia, zapisywania i uruchamiania kodu w tym środowisku.

---

### 1. Wprowadzenie do języka Python

**Czym jest Python?**  
Python to wysokopoziomowy, interpretowany język programowania, który został stworzony pod koniec lat 80. XX wieku przez Guido van Rossuma. Jego pierwsze oficjalne wydanie pojawiło się w 1991 roku. Od samego początku Python projektowano z myślą o czytelności kodu oraz prostocie składni. Dzięki temu kod napisany w Pythonie przypomina momentami pseudokod – jest klarowny i łatwy do odczytania nawet dla osób dopiero rozpoczynających swoją przygodę z programowaniem.

**Rys historyczny:**  
Python powstał jako odpowiedź na potrzebę języka prostego i przyjemnego w użyciu, łączącego możliwości skryptowe i ogólnego zastosowania. Guido van Rossum, pracując w Centrum Naukowo-Badawczym CWI w Amsterdamie, inspirował się językiem ABC, starając się stworzyć język o prostszej i bardziej przystępnej składni. Nazwa „Python” nie pochodzi od węża, lecz od brytyjskiej grupy komediowej Monty Python. Wpływ humoru i prostoty jest widoczny do dziś w dokumentacji i filozofii języka. Na przestrzeni lat Python zyskał ogromną popularność dzięki swojej uniwersalności i dynamicznemu rozwojowi. Dziś jest wspierany przez ogromną społeczność, a jego fundacja – Python Software Foundation – dba o standardy i rozwój języka.

**Zastosowania:**  
Python jest językiem ogólnego zastosowania (general-purpose), co oznacza, że można używać go w wielu obszarach:

1. **Analiza danych i nauka o danych (Data Science):**  
   Dzięki bibliotekom takim jak NumPy, Pandas czy Matplotlib, Python stał się wiodącym językiem w analizie danych i machine learningu. Ponadto frameworki jak TensorFlow i PyTorch umożliwiają tworzenie zaawansowanych modeli uczenia maszynowego i sieci neuronowych.

2. **Tworzenie aplikacji webowych:**  
   Frameworki takie jak Django czy Flask pozwalają na tworzenie wydajnych i skalowalnych aplikacji webowych. Wielu programistów decyduje się na Pythona przy tworzeniu backendów serwisów internetowych.

3. **Scripting i automatyzacja:**  
   Ze względu na prostotę składni i wszechstronność, Python świetnie nadaje się do tworzenia małych skryptów automatyzujących powtarzalne zadania – od obróbki plików tekstowych, przez przetwarzanie obrazów, po integrację z systemami operacyjnymi.

4. **Inne dziedziny:**  
   Python jest wykorzystywany w testowaniu oprogramowania, IoT (Internet of Things), tworzeniu gier (np. za pomocą Pygame), w robotyce, inżynierii oprogramowania i wielu innych obszarach.

---

### 2. Instalacja Pythona

Aby rozpocząć pracę z Pythonem, potrzebujemy zainstalować interpreter języka na naszym komputerze. Interpreter to program, który odczytuje i wykonuje kod Pythona linijka po linijce, pozwalając nam natychmiast sprawdzać poprawność i działanie napisanego kodu.

**Kroki instalacji (dla systemów Windows):**  
1. Wejdź na oficjalną stronę Pythona: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. Pobierz najnowszą wersję instalatora Pythona dla Windows.  
3. Uruchom plik instalacyjny i zaznacz opcję „Add Python to PATH” (jest to bardzo ważne, ponieważ pozwala na dostęp do interpretera z poziomu konsoli).  
4. Postępuj zgodnie z instrukcjami, wybierz opcję „Install Now” lub „Customize installation”, jeśli chcesz zmienić domyślne ścieżki.  
5. Po zakończonej instalacji możesz sprawdzić poprawność instalacji włączając wiersz poleceń (CMD) i wpisując:  
   ```bash
   python --version
   ```  
   Jeśli zobaczysz komunikat z wersją Pythona, oznacza to, że wszystko działa poprawnie.

**Instalacja na macOS i Linux:**  
W przypadku macOS i Linux Python jest często preinstalowany, choć może to być starsza wersja języka. Zaleca się zainstalowanie nowszej wersji ze strony python.org lub korzystając z menedżerów pakietów (np. `brew` na macOS). Na macOS pobieramy instalator z python.org i postępujemy podobnie jak na Windows, zaś na Linuxie można skorzystać z poleceń w terminalu, np.:  
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

---

### 3. Instalacja i konfiguracja PyCharm Community Edition

**Czym jest PyCharm?**  
PyCharm to zaawansowane środowisko programistyczne (IDE) stworzone przez firmę JetBrains, specjalizującą się w narzędziach dla deweloperów. PyCharm ułatwia pracę z Pythonem, oferując podpowiedzi składniowe, inspekcje kodu, wsparcie dla testów, integrację z systemami kontroli wersji, debugger, profilery i wiele innych narzędzi zwiększających produktywność programisty.

**Wersja Community:**  
PyCharm Community Edition jest darmową, otwartoźródłową wersją PyCharm, która zawiera większość niezbędnych funkcji do nauki i codziennej pracy z kodem Python. Nie posiada wszystkich zaawansowanych funkcji dostępnych w wersji Professional (np. zaawansowane wsparcie dla frameworków webowych, narzędzi do analizy kodu na dużą skalę czy integracji z wieloma usługami w chmurze), jednak do podstaw i celów naszego kursu będzie w pełni wystarczająca.

**Instalacja PyCharm Community Edition (Windows):**  
1. Przejdź na stronę [https://www.jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download) i wybierz opcję „Community Edition”.  
2. Pobierz instalator i uruchom go.  
3. Podczas instalacji możesz zaznaczyć dodanie skrótu na pulpit lub integrację z powłoką systemową.  
4. Po zakończonej instalacji uruchom PyCharm. Przy pierwszym uruchomieniu zostaniesz poproszony o zaakceptowanie warunków licencji i ewentualnie o import ustawień z poprzednich instalacji.

**Konfiguracja interpretera Pythona w PyCharm:**  
Po uruchomieniu PyCharm:  
1. Kliknij „File” > „Settings” (na Windows) lub „PyCharm” > „Preferences” (na macOS).  
2. W ustawieniach przejdź do „Project: [nazwa_projektu]” > „Python Interpreter”.  
3. Upewnij się, że na liście Interpreterów widnieje zainstalowana przez ciebie wersja Pythona. Jeśli nie, kliknij ikonę koła zębatego i wybierz „Add Interpreter”, a następnie wskaż lokalizację zainstalowanego Pythona.

Po poprawnej konfiguracji jesteś gotów do pracy. PyCharm wykryje składnię Pythonową, podpowie funkcje, zmienne, moduły i będzie wspierał podczas pisania kodu.

---

### 4. Pierwsze uruchomienie projektu w PyCharm i interfejs IDE

**Tworzenie nowego projektu:**  
Po uruchomieniu PyCharm pojawi się okno powitalne, z którego możesz wybrać opcję „New Project”. Następnie:  
1. Podaj nazwę swojego projektu.  
2. Wskaż lokalizację, w której ma zostać utworzony folder projektu.  
3. Upewnij się, że Interpreter jest ustawiony na zainstalowaną przez ciebie wersję Pythona.  
4. Kliknij „Create”.

Po tych krokach PyCharm utworzy nowy projekt z podstawową strukturą folderów (czasem nawet z plikiem `main.py`, jeśli wybierzesz taką opcję).

**Poznanie interfejsu IDE:**  
Główny obszar roboczy PyCharm składa się z kilku kluczowych elementów:  
- **Editor** – centralna część ekranu, gdzie piszesz kod.  
- **Projekt (Project) pane** – zazwyczaj po lewej stronie. Prezentuje drzewiastą strukturę plików i folderów w projekcie.  
- **Toolbar i narzędzia** – górny pasek, zawiera skróty do najważniejszych funkcji, jak uruchamianie programów, korzystanie z kontroli wersji, debuggera itp.  
- **Status bar** – na dole okna, pokazuje informacje o statusie projektu, gałęziach Gita, trybach edycji i inne komunikaty.  
- **Terminal, Python Console, Version Control** – dodatkowe panele dostępne zazwyczaj na dole okna, które można przełączać. Terminal pozwala na pracę z linią komend, Python Console na bezpośrednie wykonywanie fragmentów kodu, a zakładka Version Control integruje z Git i innymi systemami kontroli wersji.

**Podświetlanie składni i podpowiedzi kodu:**  
W miarę pisania kodu PyCharm automatycznie podpowiada nazwy funkcji, zmiennych i klas, a także sprawdza składnię pod kątem błędów i ostrzeżeń. Linie z błędami lub ostrzeżeniami są zwykle podkreślane, a po najechaniu kursorem na taką linię otrzymasz wskazówki, jak naprawić problem.


<img src="img/pycharm-ide.jpeg" />

---

### 5. Struktura typowego projektu Pythonowego

Choć Python nie narzuca ścisłych reguł co do organizacji plików i folderów, istnieją dobre praktyki, które warto poznać już na początku. Typowy projekt Pythonowy może wyglądać następująco:

```
nazwa_projektu/
|-- nazwa_projektu/
|   |-- __init__.py
|   |-- main.py
|   `-- moduł1.py
|-- tests/
|   `-- test_moduł1.py
|-- requirements.txt
`-- README.md
```

- **Folder główny projektu (nazwa_projektu)**: Zazwyczaj w nim znajdują się pliki konfiguracyjne, plik README z opisem projektu oraz często plik `requirements.txt` z listą zewnętrznych bibliotek wymaganych do uruchomienia projektu.
- **Folder o takiej samej nazwie jak projekt**: W nim umieszczamy właściwy kod źródłowy aplikacji – pliki `.py` zawierające funkcje, klasy i logikę biznesową.
- `__init__.py` zwykle wskazuje, że dany folder jest traktowany jako moduł, co ułatwia importy wewnątrz projektu.
- **Folder tests**: W nim można umieszczać testy jednostkowe sprawdzające poprawność działania poszczególnych fragmentów kodu.
- **Plik requirements.txt**: Zawiera listę zależności (bibliotek zewnętrznych) potrzebnych do uruchomienia projektu.  
- **Plik README.md**: Zawiera opis projektu, instrukcje instalacji i uruchomienia, a także inne informacje dla użytkowników.

Na początkowym etapie nauki nie musisz się sztywno trzymać tego wzorca, ale warto go poznać, aby w przyszłości organizować kod w czytelny i przewidywalny sposób.

---

### 6. Praktyka: Utworzenie nowego projektu w PyCharm i „Hello World”

Przejdźmy do części praktycznej. Załóżmy, że masz już zainstalowany Python i PyCharm Community Edition, oraz skonfigurowany interpreter Pythona.

**Kroki praktyczne:**

1. **Utworzenie nowego projektu:**
   - Uruchom PyCharm.
   - W oknie powitalnym wybierz opcję „New Project”.
   - W polu „Location” podaj ścieżkę, np. `C:\Users\TwojaNazwaUżytkownika\Documents\HelloWorld`.
   - Upewnij się, że w sekcji „Python Interpreter” wybrana jest poprawna wersja Pythona.
   - Kliknij „Create”.

2. **Utworzenie nowego pliku Python:**
   - W panelu po lewej stronie (Project) znajdź nazwę swojego projektu `HelloWorld`.
   - Kliknij prawym przyciskiem myszy na nazwę projektu i wybierz „New” > „Python File”.
   - Nazwij plik `hello.py` (lub dowolnie inaczej, np. `main.py`).

3. **Napisanie kodu „Hello World”:**
   - W otwartym pliku `hello.py` w edytorze wpisz:
     ```python
     print("Hello World!")
     ```
   
   To krótkie polecenie wypisze tekst „Hello World!” w konsoli po uruchomieniu programu.

4. **Uruchomienie programu:**
   - W górnym pasku narzędzi znajdziesz przycisk „Run” (zielony trójkąt).
   - Jeśli PyCharm poprosi o konfigurację uruchomienia (tzw. Run Configuration), potwierdź, że chcesz uruchomić plik `hello.py`.
   - W dolnej części okna PyCharm pojawi się panel z wynikami działania programu. Powinieneś zobaczyć:
     ```
     Hello World!
     ```
   
   Gratulacje! Właśnie uruchomiłeś swój pierwszy program w Pythonie korzystając z PyCharm.

---

### Podsumowanie

W tym rozdziale zapoznaliśmy się z Pythonem – poznaliśmy jego krótką historię, zalety i szerokie spektrum zastosowań. Dowiedzieliśmy się, jak zainstalować interpreter Pythona z oficjalnej strony, a następnie jak zainstalować i skonfigurować PyCharm Community Edition, narzędzie, które będzie nam towarzyszyć podczas dalszej nauki i pracy.

Poznaliśmy interfejs PyCharm, dowiedzieliśmy się, czym jest projekt w tym IDE, jakie są elementy środowiska i gdzie znaleźć poszczególne funkcje. Następnie zapoznaliśmy się z przykładową strukturą projektu Pythonowego, co pozwoli nam w przyszłości utrzymać porządek w kodzie.

Wreszcie wykonaliśmy pierwsze praktyczne ćwiczenie: utworzyliśmy nowy projekt, dodaliśmy do niego prosty plik źródłowy i napisaliśmy krótki program typu „Hello World”. To mały, ale symboliczny krok – od tego momentu możesz już tworzyć i uruchamiać własny kod w Pythonie, co będzie fundamentem do kolejnych kroków i rozbudowy twoich umiejętności.

W kolejnych rozdziałach przyjrzymy się składni języka, jego podstawowym typom danych, instrukcjom warunkowym i pętlom, a także wielu innym elementom, które czynią Pythona tak potężnym i wszechstronnym narzędziem.

----

© 2024 Marian Witkowski
