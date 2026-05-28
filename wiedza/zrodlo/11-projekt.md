## Blok 11: Projekt końcowy

Projekt końcowy jest kulminacją zdobytej wiedzy i umiejętności podczas kursu. Jego celem jest umożliwienie praktycznego zastosowania poznanych technik programowania, integracji różnych narzędzi oraz doskonalenia procesów projektowania, implementacji i utrzymania kodu. W tym bloku zaprojektujemy i zrealizujemy prosty skrypt do scraping’u danych z wybranej strony internetowej, zapisania ich do pliku oraz przeprowadzenia analizy. Skrypt ten będzie obejmował obsługę błędów, testowanie, organizację kodu oraz dokumentację, co pozwoli na stworzenie solidnego i łatwego w utrzymaniu projektu.

### Cele projektu

- **Integracja umiejętności:** Zastosowanie zdobytej wiedzy z różnych bloków kursu w jednym, spójnym projekcie.
- **Praktyczne zastosowanie narzędzi:** Korzystanie z bibliotek takich jak `requests`, `csv`, `json`, `datetime`, `matplotlib` oraz zarządzanie środowiskiem za pomocą `virtualenv` lub `venv`.
- **Rozwijanie dobrych praktyk:** Organizacja kodu, obsługa wyjątków, pisanie testów jednostkowych, wersjonowanie kodu za pomocą Git, oraz tworzenie dokumentacji.
- **Praca zespołowa:** Jeśli projekt realizowany jest w grupach, nauka współpracy i zarządzania kodem w zespole.

### Przykładowy temat projektu

**Prosty skrypt do scraping’u danych z API pogodowego:**

- **Funkcjonalności:**
  - Pobieranie danych pogodowych z wybranego API (np. OpenWeatherMap).
  - Zapis danych do pliku CSV.
  - Analiza danych (np. obliczanie średniej temperatury, maksymalnej wilgotności).
  - Wizualizacja danych za pomocą wykresów.
  - Obsługa błędów i wyjątków.
  - Testowanie funkcjonalności skryptu.
  - Dokumentacja projektu.

### Planowanie projektu

#### 1. Definiowanie wymagań

**Funkcjonalne:**
- **Pobieranie danych:**
  - Pobieranie aktualnych danych pogodowych dla wybranego miasta za pomocą API.
- **Zapis danych:**
  - Zapis pobranych danych do pliku CSV.
- **Analiza danych:**
  - Obliczanie średniej temperatury.
  - Znajdowanie maksymalnej wilgotności.
- **Wizualizacja:**
  - Tworzenie wykresów przedstawiających zmiany temperatury w czasie.
- **Obsługa błędów:**
  - Reagowanie na błędy połączenia, błędne dane itp.
- **Testowanie:**
  - Pisanie testów jednostkowych dla kluczowych funkcji.
- **Dokumentacja:**
  - Opis projektu, instrukcje użytkowania, informacje o zależnościach.

**Niefunkcjonalne:**
- **Czytelność kodu:** Kod powinien być przejrzysty i dobrze zorganizowany.
- **Skalowalność:** Możliwość łatwego rozszerzenia funkcjonalności.
- **Przenośność:** Kod powinien działać na różnych systemach operacyjnych bez zmian.

#### 2. Wybór technologii

- **Język programowania:** Python 3.x
- **Biblioteki:**
  - `requests` – do pobierania danych z API.
  - `csv` – do zapisywania danych.
  - `json` – do przetwarzania danych JSON.
  - `datetime` – do obsługi dat i czasu.
  - `matplotlib` – do tworzenia wykresów.
  - `unittest` – do pisania testów jednostkowych.
- **Narzędzia:**
  - `virtualenv` lub `venv` – do zarządzania wirtualnym środowiskiem.
  - Git – do wersjonowania kodu.
  - IDE: PyCharm, Visual Studio Code lub inny preferowany edytor kodu.

#### 3. Podział projektu na etapy

1. **Przygotowanie środowiska:**
   - Instalacja Pythona.
   - Tworzenie wirtualnego środowiska.
   - Instalacja wymaganych bibliotek.
2. **Pobieranie danych z API:**
   - Konfiguracja zapytań do API.
   - Przechwytywanie i parsowanie danych JSON.
3. **Zapis danych do pliku CSV:**
   - Tworzenie funkcji do zapisu danych.
4. **Analiza danych:**
   - Implementacja funkcji do obliczeń statystycznych.
5. **Wizualizacja danych:**
   - Tworzenie wykresów za pomocą `matplotlib`.
6. **Obsługa wyjątków:**
   - Implementacja bloków `try-except`.
7. **Testowanie:**
   - Pisanie testów jednostkowych.
8. **Dokumentacja:**
   - Tworzenie pliku `README.md` oraz komentarzy w kodzie.
9. **Wersjonowanie kodu (opcjonalnie):**
   - Inicjalizacja repozytorium Git.
   - Regularne commitowanie zmian.

### Implementacja projektu

#### 1. Przygotowanie środowiska pracy

**1.1. Instalacja Pythona:**
Upewnij się, że masz zainstalowaną najnowszą wersję Pythona 3.x. Możesz ją pobrać ze strony [python.org](https://www.python.org/downloads/).

**1.2. Tworzenie wirtualnego środowiska:**

```bash
# Tworzenie wirtualnego środowiska
python3 -m venv venv

# Aktywacja wirtualnego środowiska
# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**1.3. Instalacja wymaganych bibliotek:**

```bash
pip install requests matplotlib
```

Utwórz plik `requirements.txt`, aby łatwo zarządzać zależnościami:

```bash
pip freeze > requirements.txt
```

#### 2. Pobieranie danych z API

**2.1. Uzyskanie klucza API:**
Zarejestruj się na stronie [OpenWeatherMap](https://openweathermap.org/api) i uzyskaj klucz API.

**2.2. Implementacja funkcji pobierającej dane:**

```python
# weather_utils.py

import requests
from datetime import datetime

def pobierz_dane_pogodowe(miasto, klucz_api):
    """
    Pobiera dane pogodowe dla danego miasta z API OpenWeatherMap.

    Args:
        miasto (str): Nazwa miasta.
        klucz_api (str): Klucz API do OpenWeatherMap.

    Returns:
        dict: Słownik z danymi pogodowymi lub None w przypadku błędu.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={klucz_api}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Sprawdza status odpowiedzi
        dane = response.json()
        wynik = {
            "miasto": dane.get("name", "Nieznane"),
            "data": datetime.utcfromtimestamp(dane.get("dt", 0)).strftime('%Y-%m-%d %H:%M:%S'),
            "temperatura": dane["main"].get("temp", 0),
            "cisnienie": dane["main"].get("pressure", 0),
            "wilgotnosc": dane["main"].get("humidity", 0),
            "opis": dane["weather"][0].get("description", "brak")
        }
        return wynik
    except requests.exceptions.HTTPError as http_err:
        print(f"Błąd HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Błąd połączenia: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Przekroczono czas oczekiwania: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Inny błąd: {req_err}")
    except KeyError as key_err:
        print(f"Nieoczekiwana struktura danych: {key_err}")
    except Exception as e:
        print(f"Niespodziewany błąd: {e}")
    return None
```

**2.3. Testowanie funkcji pobierającej dane:**

```python
# main.py

from weather_utils import pobierz_dane_pogodowe

def main():
    API_KEY = "TWOJ_KLUCZ_API"  # Zamień na swój klucz API
    miasto = "Warsaw"
    dane = pobierz_dane_pogodowe(miasto, API_KEY)
    if dane:
        print(dane)

if __name__ == "__main__":
    main()
```

Po uruchomieniu skryptu powinniśmy zobaczyć dane pogodowe w konsoli.

#### 3. Zapis danych do pliku CSV

**3.1. Implementacja funkcji do zapisu danych:**

```python
# weather_utils.py (kontynuacja)

import csv

def zapisz_dane_do_csv(dane, nazwa_pliku):
    """
    Zapisuje listę słowników z danymi do pliku CSV.

    Args:
        dane (list): Lista słowników z danymi.
        nazwa_pliku (str): Ścieżka do pliku CSV.
    """
    if not dane:
        print("Brak danych do zapisania.")
        return
    pola = ["miasto", "data", "temperatura", "cisnienie", "wilgotnosc", "opis"]
    try:
        with open(nazwa_pliku, "w", newline='', encoding="utf-8") as plik:
            writer = csv.DictWriter(plik, fieldnames=pola)
            writer.writeheader()
            for rekord in dane:
                writer.writerow(rekord)
        print(f"Dane zapisane do pliku {nazwa_pliku}")
    except IOError as e:
        print(f"Nie można zapisać pliku: {e}")
```

**3.2. Testowanie funkcji zapisu:**

```python
# main.py (kontynuacja)

from weather_utils import pobierz_dane_pogodowe, zapisz_dane_do_csv

def main():
    API_KEY = "TWOJ_KLUCZ_API"  # Zamień na swój klucz API
    miasto = "Warsaw"
    nazwa_csv = "pogoda_warsaw.csv"
    dane = pobierz_dane_pogodowe(miasto, API_KEY)
    if dane:
        zapisz_dane_do_csv([dane], nazwa_csv)

if __name__ == "__main__":
    main()
```

Po uruchomieniu skryptu, plik `pogoda_warsaw.csv` powinien zawierać pobrane dane.

#### 4. Analiza danych

**4.1. Implementacja funkcji analitycznych:**

```python
# weather_utils.py (kontynuacja)

def oblicz_srednia_temperatura(dane):
    """
    Oblicza średnią temperaturę z listy danych pogodowych.

    Args:
        dane (list): Lista słowników z danymi pogodowymi.

    Returns:
        float: Średnia temperatura lub None, jeśli brak danych.
    """
    if not dane:
        print("Brak danych do analizy.")
        return None
    suma = sum(rekord["temperatura"] for rekord in dane)
    srednia = suma / len(dane)
    return srednia
```

**4.2. Testowanie funkcji analizy:**

```python
# main.py (kontynuacja)

from weather_utils import pobierz_dane_pogodowe, zapisz_dane_do_csv, oblicz_srednia_temperatura

def main():
    API_KEY = "TWOJ_KLUCZ_API"  # Zamień na swój klucz API
    miasto = "Warsaw"
    nazwa_csv = "pogoda_warsaw.csv"
    dane = pobierz_dane_pogodowe(miasto, API_KEY)
    if dane:
        zapisz_dane_do_csv([dane], nazwa_csv)
        srednia_temp = oblicz_srednia_temperatura([dane])
        if srednia_temp is not None:
            print(f"Średnia temperatura w {miasto}: {srednia_temp:.2f} °C")

if __name__ == "__main__":
    main()
```

#### 5. Wizualizacja danych

**5.1. Implementacja funkcji wizualizacyjnej:**

```python
# weather_utils.py (kontynuacja)

import matplotlib.pyplot as plt

def tworz_wykres_temperatury(dane, nazwa_pliku):
    """
    Tworzy wykres temperatury w czasie.

    Args:
        dane (list): Lista słowników z danymi pogodowymi.
        nazwa_pliku (str): Ścieżka do pliku wykresu.
    """
    if not dane:
        print("Brak danych do wizualizacji.")
        return
    daty = [rekord["data"] for rekord in dane]
    temperatury = [rekord["temperatura"] for rekord in dane]
    
    plt.figure(figsize=(10, 5))
    plt.plot(daty, temperatury, marker='o', linestyle='-', color='b')
    plt.title("Zmiany temperatury w czasie")
    plt.xlabel("Data i czas")
    plt.ylabel("Temperatura (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    try:
        plt.savefig(nazwa_pliku)
        plt.show()
        print(f"Wykres zapisany jako {nazwa_pliku}")
    except IOError as e:
        print(f"Nie można zapisać wykresu: {e}")
```

**5.2. Testowanie funkcji wizualizacyjnej:**

```python
# main.py (kontynuacja)

from weather_utils import pobierz_dane_pogodowe, zapisz_dane_do_csv, oblicz_srednia_temperatura, tworz_wykres_temperatury

def main():
    API_KEY = "TWOJ_KLUCZ_API"  # Zamień na swój klucz API
    miasto = "Warsaw"
    nazwa_csv = "pogoda_warsaw.csv"
    nazwa_wykresu = "wykres_temperatury_warsaw.png"
    
    dane = pobierz_dane_pogodowe(miasto, API_KEY)
    if dane:
        zapisz_dane_do_csv([dane], nazwa_csv)
        srednia_temp = oblicz_srednia_temperatura([dane])
        if srednia_temp is not None:
            print(f"Średnia temperatura w {miasto}: {srednia_temp:.2f} °C")
        tworz_wykres_temperatury([dane], nazwa_wykresu)

if __name__ == "__main__":
    main()
```

Po uruchomieniu skryptu, oprócz pliku CSV, zostanie wygenerowany wykres `wykres_temperatury_warsaw.png`.

#### 6. Organizacja kodu

Organizacja kodu jest kluczowa dla jego czytelności i łatwości utrzymania. Podzielmy projekt na moduły, które będą zawierać funkcje odpowiedzialne za różne aspekty działania skryptu.

**6.1. Struktura projektu:**

```
projekt_pogodowy/
│
├── main.py
├── weather_utils.py
├── tests/
│   ├── __init__.py
│   └── test_weather_utils.py
├── requirements.txt
└── README.md
```

**6.2. Główne moduły:**

- `main.py`: Główny skrypt uruchamiający projekt.
- `weather_utils.py`: Moduł zawierający funkcje do pobierania, zapisywania, analizy i wizualizacji danych.
- `tests/`: Katalog zawierający testy jednostkowe.

#### 7. Testowanie projektu

Testowanie jest nieodłącznym elementem tworzenia oprogramowania, zapewniającym jego poprawne działanie oraz ułatwiającym wprowadzanie zmian bez ryzyka wprowadzenia błędów.

**7.1. Implementacja testów jednostkowych:**

```python
# tests/test_weather_utils.py

import unittest
from unittest.mock import patch
from weather_utils import pobierz_dane_pogodowe, oblicz_srednia_temperatura

class TestWeatherUtils(unittest.TestCase):
    
    @patch('weather_utils.requests.get')
    def test_pobierz_dane_pogodowe_sukces(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "name": "Warsaw",
            "dt": 1609459200,
            "main": {
                "temp": 5.0,
                "pressure": 1013,
                "humidity": 80
            },
            "weather": [
                {"description": "clear sky"}
            ]
        }
        wynik = pobierz_dane_pogodowe("Warsaw", "dummy_key")
        expected = {
            "miasto": "Warsaw",
            "data": "2021-01-01 00:00:00",
            "temperatura": 5.0,
            "cisnienie": 1013,
            "wilgotnosc": 80,
            "opis": "clear sky"
        }
        self.assertEqual(wynik, expected)
    
    @patch('weather_utils.requests.get')
    def test_pobierz_dane_pogodowe_http_error(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        wynik = pobierz_dane_pogodowe("Warsaw", "dummy_key")
        self.assertIsNone(wynik)
    
    def test_oblicz_srednia_temperatura(self):
        dane = [
            {"temperatura": 10},
            {"temperatura": 20},
            {"temperatura": 30}
        ]
        srednia = oblicz_srednia_temperatura(dane)
        self.assertEqual(srednia, 20)
    
    def test_oblicz_srednia_temperatura_brak_danych(self):
        dane = []
        srednia = oblicz_srednia_temperatura(dane)
        self.assertIsNone(srednia)

if __name__ == '__main__':
    unittest.main()
```

**7.2. Uruchamianie testów:**

W PyCharm możesz uruchomić testy jednostkowe, klikając prawym przyciskiem myszy na pliku `test_weather_utils.py` i wybierając „Run 'test_weather_utils'”. Alternatywnie, możesz uruchomić testy z linii poleceń:

```bash
python -m unittest discover tests
```

**7.3. Dodawanie testów:**

Dodatkowe testy można dodać w miarę rozwijania projektu, obejmując różnorodne scenariusze i edge cases, co zwiększy pokrycie kodu testami i pewność jego poprawności.

#### 8. Obsługa błędów

Obsługa błędów jest kluczowa dla stabilności i niezawodności skryptu. W projekcie zastosowaliśmy mechanizmy `try-except`, które pozwalają na kontrolowane reagowanie na różne rodzaje błędów.

**8.1. Przykład obsługi błędów w funkcji pobierającej dane:**

```python
def pobierz_dane_pogodowe(miasto, klucz_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={klucz_api}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        dane = response.json()
        wynik = {
            "miasto": dane.get("name", "Nieznane"),
            "data": datetime.utcfromtimestamp(dane.get("dt", 0)).strftime('%Y-%m-%d %H:%M:%S'),
            "temperatura": dane["main"].get("temp", 0),
            "cisnienie": dane["main"].get("pressure", 0),
            "wilgotnosc": dane["main"].get("humidity", 0),
            "opis": dane["weather"][0].get("description", "brak")
        }
        return wynik
    except requests.exceptions.HTTPError as http_err:
        print(f"Błąd HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Błąd połączenia: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Przekroczono czas oczekiwania: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Inny błąd: {req_err}")
    except KeyError as key_err:
        print(f"Nieoczekiwana struktura danych: {key_err}")
    except Exception as e:
        print(f"Niespodziewany błąd: {e}")
    return None
```

**8.2. Obsługa błędów w funkcji zapisu do pliku:**

```python
def zapisz_dane_do_csv(dane, nazwa_pliku):
    if not dane:
        print("Brak danych do zapisania.")
        return
    pola = ["miasto", "data", "temperatura", "cisnienie", "wilgotnosc", "opis"]
    try:
        with open(nazwa_pliku, "w", newline='', encoding="utf-8") as plik:
            writer = csv.DictWriter(plik, fieldnames=pola)
            writer.writeheader()
            for rekord in dane:
                writer.writerow(rekord)
        print(f"Dane zapisane do pliku {nazwa_pliku}")
    except IOError as e:
        print(f"Nie można zapisać pliku: {e}")
```

**8.3. Korzystanie z bloków `finally`:**

Blok `finally` pozwala na wykonanie kodu niezależnie od tego, czy wystąpił wyjątek, czy nie. Może być używany do czyszczenia zasobów, takich jak zamykanie plików.

```python
def otworz_plik(nazwa_pliku):
    plik = None
    try:
        plik = open(nazwa_pliku, "r")
        # Przetwarzanie danych
    except IOError as e:
        print(f"Nie można otworzyć pliku: {e}")
    finally:
        if plik:
            plik.close()
            print("Plik zamknięty.")
```

### 9. Dokumentacja projektu

Dokumentacja jest niezbędna dla zrozumienia, jak korzystać z projektu oraz jak działa jego kod. W projekcie stworzymy plik `README.md`, który będzie zawierał opis projektu, instrukcje instalacji, użycia, informacje o testach oraz licencji.

**9.1. Przykładowy plik `README.md`:**

```markdown
# Skrypt do Pobierania i Analizy Danych Pogodowych

## Opis

Ten skrypt umożliwia pobieranie danych pogodowych dla wybranego miasta z API OpenWeatherMap, zapisywanie ich do pliku CSV oraz przeprowadzanie podstawowej analizy i wizualizacji danych.

## Wymagania

- Python 3.x
- Biblioteki:
  - requests
  - matplotlib

## Instalacja

1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/twoj_uzytkownik/projekt_pogodowy.git
    ```
2. Przejdź do katalogu projektu:
    ```bash
    cd projekt_pogodowy
    ```
3. Utwórz wirtualne środowisko:
    ```bash
    python3 -m venv venv
    ```
4. Aktywuj wirtualne środowisko:
    - Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
    - Windows:
        ```bash
        venv\Scripts\activate
        ```
5. Zainstaluj wymagane pakiety:
    ```bash
    pip install -r requirements.txt
    ```

## Użycie

1. Otwórz plik `main.py` i wprowadź swój klucz API:
    ```python
    API_KEY = "TWOJ_KLUCZ_API"
    ```
2. Uruchom skrypt:
    ```bash
    python main.py
    ```
3. Skrypt pobierze dane pogodowe, zapisze je do pliku `pogoda_warsaw.csv`, obliczy średnią temperaturę oraz utworzy wykres `wykres_temperatury_warsaw.png`.

## Testowanie

Aby uruchomić testy jednostkowe, przejdź do katalogu `tests` i uruchom:

```bash
python -m unittest discover tests
```

## Licencja

Ten projekt jest udostępniony na licencji MIT.
```

### 10. Wersjonowanie kodu za pomocą Git (opcjonalnie)

Git jest narzędziem do kontroli wersji, które pozwala śledzić zmiany w kodzie, współpracować z innymi programistami oraz zarządzać historią projektu.

**10.1. Inicjalizacja repozytorium Git:**

```bash
# Przejdź do katalogu projektu
cd projekt_pogodowy

# Inicjalizuj repozytorium Git
git init

# Dodaj wszystkie pliki do repozytorium
git add .

# Zrób pierwszy commit
git commit -m "Initial commit - Projekt końcowy skrypt do scraping’u danych pogodowych"
```

**10.2. Tworzenie repozytorium zdalnego:**

Utwórz repozytorium na platformie takiej jak GitHub, GitLab lub Bitbucket, a następnie połącz je z lokalnym repozytorium.

```bash
# Dodaj zdalne repozytorium (przykład dla GitHub)
git remote add origin https://github.com/twoj_uzytkownik/projekt_pogodowy.git

# Wypchnij zmiany do zdalnego repozytorium
git push -u origin main
```

**10.3. Podstawowe polecenia Git:**

- **Dodawanie zmian do indeksu:**
    ```bash
    git add .
    ```
- **Commitowanie zmian:**
    ```bash
    git commit -m "Opis zmian"
    ```
- **Wysyłanie zmian do zdalnego repozytorium:**
    ```bash
    git push origin main
    ```
- **Pobieranie zmian ze zdalnego repozytorium:**
    ```bash
    git pull origin main
    ```
- **Tworzenie nowej gałęzi:**
    ```bash
    git checkout -b nowa_gałąź
    ```
- **Przełączanie się na istniejącą gałąź:**
    ```bash
    git checkout main
    ```

### 11. Praktyka: Realizacja projektu

Przeprowadźmy kompletne przykłady implementacji poszczególnych etapów projektu.

#### 11.1. Implementacja funkcji pomocniczych

**weather_utils.py:**

```python
# weather_utils.py

import requests
from datetime import datetime
import csv
import matplotlib.pyplot as plt
from functools import reduce

def pobierz_dane_pogodowe(miasto, klucz_api):
    """
    Pobiera dane pogodowe dla danego miasta z API OpenWeatherMap.

    Args:
        miasto (str): Nazwa miasta.
        klucz_api (str): Klucz API do OpenWeatherMap.

    Returns:
        dict: Słownik z danymi pogodowymi lub None w przypadku błędu.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={klucz_api}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        dane = response.json()
        wynik = {
            "miasto": dane.get("name", "Nieznane"),
            "data": datetime.utcfromtimestamp(dane.get("dt", 0)).strftime('%Y-%m-%d %H:%M:%S'),
            "temperatura": dane["main"].get("temp", 0),
            "cisnienie": dane["main"].get("pressure", 0),
            "wilgotnosc": dane["main"].get("humidity", 0),
            "opis": dane["weather"][0].get("description", "brak")
        }
        return wynik
    except requests.exceptions.HTTPError as http_err:
        print(f"Błąd HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Błąd połączenia: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Przekroczono czas oczekiwania: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Inny błąd: {req_err}")
    except KeyError as key_err:
        print(f"Nieoczekiwana struktura danych: {key_err}")
    except Exception as e:
        print(f"Niespodziewany błąd: {e}")
    return None

def zapisz_dane_do_csv(dane, nazwa_pliku):
    """
    Zapisuje listę słowników z danymi do pliku CSV.

    Args:
        dane (list): Lista słowników z danymi.
        nazwa_pliku (str): Ścieżka do pliku CSV.
    """
    if not dane:
        print("Brak danych do zapisania.")
        return
    pola = ["miasto", "data", "temperatura", "cisnienie", "wilgotnosc", "opis"]
    try:
        with open(nazwa_pliku, "w", newline='', encoding="utf-8") as plik:
            writer = csv.DictWriter(plik, fieldnames=pola)
            writer.writeheader()
            for rekord in dane:
                writer.writerow(rekord)
        print(f"Dane zapisane do pliku {nazwa_pliku}")
    except IOError as e:
        print(f"Nie można zapisać pliku: {e}")

def oblicz_srednia_temperatura(dane):
    """
    Oblicza średnią temperaturę z listy danych pogodowych.

    Args:
        dane (list): Lista słowników z danymi pogodowymi.

    Returns:
        float: Średnia temperatura lub None, jeśli brak danych.
    """
    if not dane:
        print("Brak danych do analizy.")
        return None
    suma = sum(rekord["temperatura"] for rekord in dane)
    srednia = suma / len(dane)
    return srednia

def tworz_wykres_temperatury(dane, nazwa_pliku):
    """
    Tworzy wykres temperatury w czasie.

    Args:
        dane (list): Lista słowników z danymi pogodowymi.
        nazwa_pliku (str): Ścieżka do pliku wykresu.
    """
    if not dane:
        print("Brak danych do wizualizacji.")
        return
    daty = [rekord["data"] for rekord in dane]
    temperatury = [rekord["temperatura"] for rekord in dane]
    
    plt.figure(figsize=(10, 5))
    plt.plot(daty, temperatury, marker='o', linestyle='-', color='b')
    plt.title("Zmiany temperatury w czasie")
    plt.xlabel("Data i czas")
    plt.ylabel("Temperatura (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    try:
        plt.savefig(nazwa_pliku)
        plt.show()
        print(f"Wykres zapisany jako {nazwa_pliku}")
    except IOError as e:
        print(f"Nie można zapisać wykresu: {e}")
```

#### 11.2. Główny skrypt projektu

**main.py:**

```python
# main.py

from weather_utils import (
    pobierz_dane_pogodowe,
    zapisz_dane_do_csv,
    oblicz_srednia_temperatura,
    tworz_wykres_temperatury
)

def main():
    API_KEY = "TWOJ_KLUCZ_API"  # Zamień na swój klucz API
    miasto = "Warsaw"
    nazwa_csv = "pogoda_warsaw.csv"
    nazwa_wykresu = "wykres_temperatury_warsaw.png"
    
    # Pobieranie danych pogodowych
    dane = pobierz_dane_pogodowe(miasto, API_KEY)
    
    if dane:
        # Zapis danych do pliku CSV
        zapisz_dane_do_csv([dane], nazwa_csv)
        
        # Analiza danych
        srednia_temp = oblicz_srednia_temperatura([dane])
        if srednia_temp is not None:
            print(f"Średnia temperatura w {miasto}: {srednia_temp:.2f} °C")
        
        # Wizualizacja danych
        tworz_wykres_temperatury([dane], nazwa_wykresu)

if __name__ == "__main__":
    main()
```

#### 11.3. Testowanie projektu

**tests/test_weather_utils.py:**

```python
# tests/test_weather_utils.py

import unittest
from unittest.mock import patch
from weather_utils import pobierz_dane_pogodowe, oblicz_srednia_temperatura

class TestWeatherUtils(unittest.TestCase):
    
    @patch('weather_utils.requests.get')
    def test_pobierz_dane_pogodowe_sukces(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "name": "Warsaw",
            "dt": 1609459200,
            "main": {
                "temp": 5.0,
                "pressure": 1013,
                "humidity": 80
            },
            "weather": [
                {"description": "clear sky"}
            ]
        }
        wynik = pobierz_dane_pogodowe("Warsaw", "dummy_key")
        expected = {
            "miasto": "Warsaw",
            "data": "2021-01-01 00:00:00",
            "temperatura": 5.0,
            "cisnienie": 1013,
            "wilgotnosc": 80,
            "opis": "clear sky"
        }
        self.assertEqual(wynik, expected)
    
    @patch('weather_utils.requests.get')
    def test_pobierz_dane_pogodowe_http_error(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        wynik = pobierz_dane_pogodowe("Warsaw", "dummy_key")
        self.assertIsNone(wynik)
    
    def test_oblicz_srednia_temperatura(self):
        dane = [
            {"temperatura": 10},
            {"temperatura": 20},
            {"temperatura": 30}
        ]
        srednia = oblicz_srednia_temperatura(dane)
        self.assertEqual(srednia, 20)
    
    def test_oblicz_srednia_temperatura_brak_danych(self):
        dane = []
        srednia = oblicz_srednia_temperatura(dane)
        self.assertIsNone(srednia)

if __name__ == '__main__':
    unittest.main()
```

#### 11.4. Dokumentacja projektu

**README.md:**

```markdown
# Skrypt do Pobierania i Analizy Danych Pogodowych

## Opis

Ten skrypt umożliwia pobieranie danych pogodowych dla wybranego miasta z API OpenWeatherMap, zapisywanie ich do pliku CSV oraz przeprowadzanie podstawowej analizy i wizualizacji danych.

## Wymagania

- Python 3.x
- Biblioteki:
  - requests
  - matplotlib

## Instalacja

1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/twoj_uzytkownik/projekt_pogodowy.git
    ```
2. Przejdź do katalogu projektu:
    ```bash
    cd projekt_pogodowy
    ```
3. Utwórz wirtualne środowisko:
    ```bash
    python3 -m venv venv
    ```
4. Aktywuj wirtualne środowisko:
    - Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
    - Windows:
        ```bash
        venv\Scripts\activate
        ```
5. Zainstaluj wymagane pakiety:
    ```bash
    pip install -r requirements.txt
    ```

## Użycie

1. Otwórz plik `main.py` i wprowadź swój klucz API:
    ```python
    API_KEY = "TWOJ_KLUCZ_API"
    ```
2. Uruchom skrypt:
    ```bash
    python main.py
    ```
3. Skrypt pobierze dane pogodowe, zapisze je do pliku `pogoda_warsaw.csv`, obliczy średnią temperaturę oraz utworzy wykres `wykres_temperatury_warsaw.png`.

## Testowanie

Aby uruchomić testy jednostkowe, przejdź do katalogu `tests` i uruchom:

```bash
python -m unittest discover tests
```

## Licencja

Ten projekt jest udostępniony na licencji MIT.
```

### 12. Praktyczne wskazówki i najlepsze praktyki

**12.1. Regularne commitowanie zmian:**

Commituj zmiany często, dodając logiczne i dobrze opisane wiadomości commitów. Dzięki temu śledzenie historii projektu staje się łatwiejsze, a w razie potrzeby można szybko cofnąć się do wcześniejszej wersji kodu.

```bash
git add .
git commit -m "Dodanie funkcji pobierającej dane pogodowe"
```

**12.2. Używanie `.gitignore`:**

Plik `.gitignore` pozwala na wykluczenie z repozytorium plików, które nie powinny być śledzone, takich jak wirtualne środowiska, pliki tymczasowe czy dane wrażliwe.

**Przykład `.gitignore`:**

```
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
*.csv
*.png
.env
```

**12.3. Dokumentacja kodu:**

Stosuj docstringi do dokumentowania funkcji, klas i modułów. Dzięki temu inni użytkownicy (lub Ty sam w przyszłości) będą mogli łatwiej zrozumieć, jak działa Twój kod.

**Przykład docstringa:**

```python
def pobierz_dane_pogodowe(miasto, klucz_api):
    """
    Pobiera dane pogodowe dla danego miasta z API OpenWeatherMap.

    Args:
        miasto (str): Nazwa miasta.
        klucz_api (str): Klucz API do OpenWeatherMap.

    Returns:
        dict: Słownik z danymi pogodowymi lub None w przypadku błędu.
    """
    # Implementacja funkcji
```

**12.4. Stosowanie linters i formatters:**

Używaj narzędzi takich jak `flake8`, `pylint` czy `black`, aby utrzymać jednolity styl kodowania i wykrywać potencjalne błędy.

**Instalacja `black`:**

```bash
pip install black
```

**Formatowanie kodu:**

```bash
black main.py weather_utils.py
```

**12.5. Korzystanie z środowisk wirtualnych:**

Upewnij się, że wszystkie zależności projektu są zainstalowane w wirtualnym środowisku, aby uniknąć konfliktów wersji i problemów z kompatybilnością.

```bash
# Tworzenie wirtualnego środowiska
python3 -m venv venv

# Aktywacja środowiska
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalacja pakietów
pip install -r requirements.txt
```

### 13. Podsumowanie

Projekt końcowy jest nie tylko sposobem na sprawdzenie zdobytej wiedzy, ale także okazją do rozwinięcia umiejętności praktycznych, takich jak:

- **Projektowanie i organizacja kodu:** Tworzenie modularnych, czytelnych i łatwych w utrzymaniu struktur.
- **Praca z API:** Pobieranie i przetwarzanie danych z zewnętrznych źródeł.
- **Zarządzanie środowiskiem:** Korzystanie z wirtualnych środowisk do izolowania zależności.
- **Testowanie:** Pisanie testów jednostkowych, które zapewniają jakość i niezawodność kodu.
- **Obsługa błędów:** Implementacja mechanizmów zabezpieczających przed nieprzewidzianymi sytuacjami.
- **Wersjonowanie kodu:** Używanie Git do śledzenia zmian i współpracy z innymi.
- **Dokumentacja:** Tworzenie przejrzystych i pomocnych opisów projektu i kodu.

Dzięki realizacji tego projektu nauczyłeś się, jak integrować różne aspekty programowania, tworzyć funkcjonalne i niezawodne aplikacje oraz stosować najlepsze praktyki w codziennej pracy programisty. Kontynuuj eksperymentowanie, rozwijaj swoje umiejętności i podejmuj się coraz bardziej zaawansowanych projektów, aby stać się jeszcze lepszym specjalistą w dziedzinie programowania.

----

© 2024 Marian Witkowski

