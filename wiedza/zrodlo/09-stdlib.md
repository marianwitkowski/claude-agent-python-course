## Blok 9: Standardowa biblioteka i wybrane biblioteki zewnętrzne

Poniższy rozdział skupia się na praktycznym wykorzystaniu standardowej biblioteki Pythona oraz na wprowadzeniu do zarządzania środowiskami i zewnętrznymi pakietami. Poznanie bogatego zestawu narzędzi dostępnych w standardowej bibliotece otwiera drogę do efektywnego rozwiązywania różnorodnych problemów, bez konieczności instalowania dodatkowych modułów. Przyjrzymy się też sposobom na rozszerzenie możliwości Pythona za pomocą zewnętrznych bibliotek, opanowując takie narzędzia jak `requests` oraz proces instalacji pakietów poprzez `pip` i `PyPI`. Następnie zbadamy znaczenie wirtualnych środowisk, co pozwoli na efektywne zarządzanie zależnościami w różnych projektach.

W części praktycznej zajmiemy się pobieraniem danych z publicznego API oraz prostym ich przetwarzaniem (parsowaniem), demonstrując w ten sposób praktyczne wykorzystanie poznanych narzędzi.

---

### 1. Przegląd standardowej biblioteki Pythona

Standardowa biblioteka Pythona to zbiór modułów i pakietów dostarczanych wraz z instalacją Pythona. Dzięki niej nie musimy szukać zewnętrznych rozwiązań do wielu typowych zadań, takich jak obsługa plików, operacje matematyczne, praca z datą i czasem, kompresja, szyfrowanie, tworzenie serwerów HTTP, parsowanie formatu JSON i wielu innych. 

Ta wszechstronność sprawia, że zanim sięgniemy po zewnętrzne pakiety, warto dokładnie poznać standardowe narzędzia, ponieważ często pozwalają rozwiązać problem „od ręki”.

---

### 2. Moduł `os`: praca z systemem operacyjnym

Moduł `os` służy do interakcji z systemem operacyjnym – umożliwia wykonywanie poleceń takich jak odczyt zawartości katalogów, tworzenie i usuwanie plików, pobieranie ścieżki do katalogu domowego czy zmiana aktualnego katalogu roboczego.

Podstawowe przykłady:

```python
import os

# Wyświetlenie ścieżki do aktualnego katalogu
print(os.getcwd())

# Lista plików w katalogu bieżącym
print(os.listdir('.'))

# Tworzenie katalogu
os.mkdir('nowy_katalog')

# Usuwanie pliku
os.remove('stary_plik.txt')
```

Dzięki `os.path` można operować na ścieżkach plików w sposób niezależny od systemu operacyjnego (Windows, Linux, macOS):

```python
import os

sciezka = os.path.join('home', 'user', 'dokumenty', 'plik.txt')
print(sciezka)  # poprawna ścieżka dla danego OS
```

To sprawia, że kod będzie bardziej przenośny, a my unikniemy problemów z różnymi separatorami katalogów (`/` lub `\`).

---

### 3. Moduł `math`: operacje matematyczne

Moduł `math` zapewnia dostęp do podstawowych funkcji matematycznych: pierwiastków, funkcji trygonometrycznych, logarytmów, stałych takich jak `pi` czy `e`.

Przykłady:

```python
import math

x = math.sqrt(16)       # 4.0
y = math.sin(math.pi/2) # 1.0
z = math.log(10, 10)     # 1.0
```

Wbudowane funkcje tego modułu są napisane w C, dzięki czemu są szybkie i wydajne. Korzystanie z nich jest przydatne w wielu dziedzinach, od analizy danych, przez obliczenia naukowe, po zwykłe przetwarzanie wartości liczbowych.

---

### 4. Moduł `datetime`: operacje na datach i czasie

Operacje na datach i czasach są częste w aplikacjach biznesowych, raportach czy analizie logów. Moduł `datetime` umożliwia tworzenie obiektów dat i czasów, dodawanie lub odejmowanie od nich okresów, formatowanie do czytelnych ciągów znaków oraz parsowanie napisów reprezentujących datę i czas.

Przykłady:

```python
from datetime import datetime, timedelta

# Aktualna data i czas
teraz = datetime.now()
print("Teraz:", teraz)

# Konwersja daty do tekstu
data_str = teraz.strftime("%Y-%m-%d %H:%M:%S")
print("Sformatowana data:", data_str)

# Tworzenie obiektu daty i dodanie 7 dni
tydzien_pozniej = teraz + timedelta(days=7)
print("Tydzień później:", tydzien_pozniej)
```

Możemy także konwertować tekst na obiekt `datetime`:

```python
data_wejscie = "2023-10-15 12:30"
data_obiekt = datetime.strptime(data_wejscie, "%Y-%m-%d %H:%M")
print(data_obiekt)
```

Dzięki temu łatwo przechowywać, sortować i porównywać daty oraz wykonywać zaawansowane operacje czasowe.

---

### 5. Pobieranie danych z sieci – moduł `requests` (zewnętrzny)

Pythonowe standardowe biblioteki do obsługi sieci (takie jak `urllib`) bywają nieco rozwlekłe w użyciu. Biblioteka `requests` jest zewnętrznym pakietem (nie jest częścią standardowej biblioteki), ale zyskała ogromną popularność i jest de facto standardem do pobierania danych z Internetu, wysyłania zapytań HTTP i pracy z API.

`requests` upraszcza obsługę HTTP:

```python
import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)
if response.status_code == 200:
    dane = response.json()
    print("Nazwa użytkownika:", dane["login"])
else:
    print("Błąd pobierania danych:", response.status_code)
```

`requests` automatycznie radzi sobie z kodowaniem, nagłówkami, obsługą błędów i formatuje dane zwracane przez serwer. Jeśli dane są w JSON, wystarczy wywołać `response.json()`, aby otrzymać słownik Pythona.

---

### 6. Wirtualne środowiska: `virtualenv` i integracja z PyCharm

W miarę rozwoju, projekty będą wymagać różnych bibliotek w różnych wersjach. Jedna aplikacja może potrzebować `requests` w wersji 2.24, a inna w 3.0. Aby uniknąć konfliktów, używa się **wirtualnych środowisk**. Wirtualne środowisko to izolowana instancja Pythona z własnymi zainstalowanymi pakietami, niezależna od globalnej instalacji.

`virtualenv` to popularne narzędzie do tworzenia wirtualnych środowisk, aczkolwiek nowsze wersje Pythona mają wbudowany moduł `venv`.

Utworzenie wirtualnego środowiska z `venv`:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Po aktywowaniu w środowisku można instalować pakiety bez wpływu na systemowy Python.

PyCharm domyślnie umożliwia tworzenie wirtualnych środowisk dla nowych projektów. Wystarczy w ustawieniach projektu wybrać Interpreter > Add > Virtualenv, a IDE samo przygotuje środowisko.

---

### 7. Instalacja pakietów z użyciem `pip` i `PyPI`

`pip` to narzędzie do instalacji pakietów z Python Package Index (PyPI) – centralnego repozytorium pakietów Pythona. Aby zainstalować `requests`, wystarczy:

```bash
pip install requests
```

To pobiera najnowszą wersję `requests` z PyPI i instaluje ją w aktywnym środowisku (globalnie, jeśli wirtualne środowisko nie jest aktywne). Można też zainstalować konkretną wersję:

```bash
pip install requests==2.25.1
```

Aby zobaczyć zainstalowane pakiety:

```bash
pip list
```

Aby zaktualizować pakiet:

```bash
pip install --upgrade requests
```

Zalecane jest zapisywanie zależności projektu do pliku `requirements.txt` lub korzystanie z narzędzi jak `pipenv` czy `poetry` do zarządzania pakietami i wirtualnymi środowiskami w bardziej zautomatyzowany sposób.

---

### 8. Praktyka: Skrypt pobierający dane z publicznego API

Załóżmy, że chcemy pobrać dane pogodowe z publicznego API i je wyświetlić. API przykładowo: OpenWeatherMap (wymaga klucza API, ale istnieją też inne publiczne źródła). Załóżmy, że mamy klucz i chcemy pobrać temperaturę dla danego miasta.

```python
import requests

API_KEY = "TWOJ_KLUCZ"
miasto = "Warsaw"
url = f"http://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    dane = response.json()
    temp = dane["main"]["temp"]
    print(f"Temperatura w {miasto}: {temp} °C")
else:
    print("Błąd pobierania danych:", response.status_code)
```

Po uruchomieniu skryptu zobaczymy aktualną temperaturę dla podanego miasta. To prosty przykład, ale w praktyce można w ten sposób budować całe aplikacje integrujące się z usługami zewnętrznymi.

---

### 9. Prosty parser danych

Załóżmy, że dane pogodowe chcemy zapisać do pliku CSV lub wybrać tylko część informacji. Możemy użyć modułu `csv` ze standardowej biblioteki lub po prostu ręcznie przetworzyć dane:

```python
import csv

dane_pogodowe = [
    {"miasto": "Warsaw", "temp": 10, "cisnienie": 1013},
    {"miasto": "Berlin", "temp": 8, "cisnienie": 1007}
]

with open("pogoda.csv", "w", newline="", encoding="utf-8") as plik:
    writer = csv.DictWriter(plik, fieldnames=["miasto", "temp", "cisnienie"])
    writer.writeheader()
    for rekord in dane_pogodowe:
        writer.writerow(rekord)
```

Następnie możemy wczytać te dane i je przetwarzać:

```python
with open("pogoda.csv", "r", encoding="utf-8") as plik:
    reader = csv.DictReader(plik)
    for row in reader:
        print(row["miasto"], row["temp"], row["cisnienie"])
```

Dzięki standardowym modułom nie potrzebujemy dodatkowych pakietów, aby pracować z popularnymi formatami danych. Oczywiście, do bardziej złożonych zadań można sięgnąć po biblioteki specjalistyczne.

---

### 10. Dalsze przykłady standardowej biblioteki

Standardowa biblioteka oferuje znacznie więcej:

- `json` – parsowanie i generowanie JSON
- `re` – wyrażenia regularne do przetwarzania tekstu
- `sqlite3` – wbudowana baza danych SQLite
- `logging` – narzędzia do logowania zdarzeń w aplikacji
- `argparse` – przetwarzanie argumentów linii poleceń
- `subprocess` – uruchamianie zewnętrznych programów

To tylko niewielki wycinek. Dokumentacja standardowej biblioteki (docs.python.org) zawiera pełen przegląd modułów i funkcji.

---

### 11. Praktyczne wskazówki dot. zarządzania środowiskami i pakietami

Zaleca się, aby dla każdego projektu tworzyć oddzielne wirtualne środowisko. W ten sposób unikamy konfliktów zależności i możemy bezpiecznie aktualizować pakiety w jednym projekcie, nie ryzykując destabilizacji innego.

Jeśli pracujemy nad aplikacją, która ma być zainstalowana na innym środowisku, tworzymy plik `requirements.txt` zawierający listę pakietów z ich wersjami:

```bash
pip freeze > requirements.txt
```

Następnie na innym komputerze czy serwerze można odtworzyć środowisko:

```bash
pip install -r requirements.txt
```

W przypadku bardziej złożonych potrzeb można rozważyć użycie `poetry` lub `pipenv`, które oferują ulepszone zarządzanie zależnościami i wirtualnymi środowiskami.

---

### 12. Podsumowanie i dalsze kroki

W tym rozdziale zapoznałeś się z możliwościami standardowej biblioteki Pythona oraz z wprowadzeniem do użycia zewnętrznych pakietów. Nauczyłeś się, jak:

- Korzystać z modułów `os`, `math` i `datetime` do obsługi plików, wykonywania obliczeń matematycznych i pracy z datami.
- Sięgnąć po bibliotekę `requests` do pobierania danych z sieci i integracji z publicznymi API.
- Stosować wirtualne środowiska (np. `venv`) i konfigurować je z poziomu PyCharm, aby skutecznie zarządzać zależnościami.
- Instalować i aktualizować pakiety z użyciem `pip` i `PyPI`.
- Tworzyć i czytać pliki CSV oraz przetwarzać dane, integrując pobrane informacje z innymi funkcjonalnościami języka Python.

Korzystanie ze standardowej biblioteki pozwala ograniczyć zależności, uprościć konfigurację projektu i skupić się na rozwiązywaniu problemów, a nie na instalowaniu niezliczonych pakietów. Wirtualne środowiska zapewniają stabilne i przewidywalne środowisko uruchomieniowe, a znajomość `pip` i `PyPI` pozwala szybko rozbudowywać możliwości Twojej aplikacji.

W kolejnych rozdziałach przyjrzymy się bardziej zaawansowanym zagadnieniom, jednak solidne opanowanie podstaw standardowej biblioteki i zarządzania pakietami jest fundamentem efektywnej pracy z Pythonem. Kontynuuj eksperymenty, testuj różne moduły i biblioteki, a z czasem stworzysz bogaty warsztat narzędziowy, który pozwoli Ci skutecznie realizować nawet najbardziej złożone projekty.

----

© 2024 Marian Witkowski
