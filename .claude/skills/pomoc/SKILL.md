---
name: pomoc
description: Wyświetla uczniowi pogrupowaną listę dostępnych komend kursu — frazy, którymi może sterować agentem. Pokazuje 7 kategorii (start, lekcja, ćwiczenia, quizy, postęp, reset, środowisko). Użyj gdy uczeń mówi "lista komend", "pomoc", "help", "co mogę zrobić?", "jakie są komendy?", "nie pamiętam co mam wpisać".
---

# Cel

Pokazać uczniowi **szybką ściągawkę** dostępnych komend bez zmuszania go do otwierania README.

# Co wyświetlić

Wypisz w czacie poniższą listę. **Nie modyfikuj** kategorii ani ikon — uczeń może mieć ją z pamięci.

```
📋 LISTA KOMEND KURSU PYTHONA

🚀 Start i kontynuacja
  • ucz mnie Pythona          → start kursu lub powitanie
  • kontynuujemy              → następna lekcja
  • pokaż program kursu       → zawartość kurs/program.md
  • zmień program kursu       → edycja celu/tempa

📚 W trakcie lekcji
  • nie rozumiem [konceptu]   → wraca do podstaw nowym kątem
  • daj mi przykład           → minimalny przykład kodu
  • co to znaczy [termin]?    → wyjaśnienie sokratejskie
  • powtórzmy tę lekcję       → od początku

✏️  Ćwiczenia i review
  • daj mi zadanie            → ćwiczenie z bieżącej lekcji
  • daj mi więcej zadań       → dodatkowe ćwiczenia
  • sprawdź moje zadanie      → review kodu
  • skończyłem [warmup/main/star] → review konkretnego rozwiązania
  • nie działa mi             → pomoc w debugowaniu
  • pokaż gwiazdkę            → odsłania zadanie ⚡

🎯 Quizy i powtórki
  • quiz                      → szybki (3 pytania)
  • quiz pełny                → pełny (5-7 pytań)
  • quiz słabe                → z tematów do powtórki

📊 Postęp
  • pokaż postępy             → podsumowanie student.json
  • gdzie skończyliśmy?       → bieżąca lekcja + ostatnia sesja
  • co mam do powtórki?       → lista do_powtorki
  • co umiem najlepiej?       → lista mocne_strony

🔄 Reset i backup
  • zresetuj kurs             → reset miękki (z backupem)
  • pełny reset kursu         → reset pełny (z backupem)
  • cofnij reset              → przywrócenie z archiwum
  • pokaż backupy             → lista postep/archiwum/

🛠️  Środowisko i pomoc
  • sprawdź Pythona           → weryfikacja python3
  • jak uruchomić kod?        → odsyła do JAK-PISAC-KOD.md
  • lista komend / pomoc      → ten widok

📖 Baza wiedzy
  • odśwież bazę wiedzy       → pobierz najnowsze pliki z repo
  • pokaż stan bazy           → statystyki bazy
  • sprawdź czy baza aktualna → porównaj ze zdalnym repo

💡 Nie musisz pamiętać dokładnych fraz — agent zrozumie też "wyczyść kurs",
   "co robiłam ostatnio", "zrób mi test" itp.
```

# Wariant skrócony

Jeśli uczeń poprosi o "krótką pomoc" / "tylko najważniejsze":

```
🎯 NAJWAŻNIEJSZE KOMENDY

  • kontynuujemy              → następna lekcja
  • daj mi zadanie            → nowe ćwiczenie
  • sprawdź moje zadanie      → review kodu
  • nie działa mi             → debugowanie
  • quiz                      → szybka powtórka
  • pokaż postępy             → twój stan
  • lista komend              → pełna lista
```

# Twarde zasady

- **Wypisuj listę w jednym bloku** — nie dziel na wiele wiadomości, ma być do skopiowania / scrollowania.
- **Nie wymyślaj nowych komend** poza tymi z listy. Jeśli uczeń pyta o coś, co nie istnieje — powiedz wprost: "tego nie ma, ale możesz [...]" i zaproponuj alternatywę.
- **Po pokazaniu listy** zadaj jedno pytanie: "Z czego dziś korzystamy?" — żeby nie zostać w trybie "wyświetlam pomoc i czekam".
- **Nie pokazuj listy** w środku trwającej lekcji bez wyraźnej prośby — to wybija z rytmu.
