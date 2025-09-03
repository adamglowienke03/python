# Python
---
### Spis treści
- [Python](#python)
    - [Spis treści](#spis-treści)
  - [***Podstawy***](#podstawy)
    - [Docstrings](#docstrings)
    - [Try: Except:](#try-except)
    - [PrettyTable](#prettytable)
  - [OOP](#oop)

---
## ***Podstawy***

### Docstrings
To krótki opis tego, co robi funkcja, klasa albo moduł. Pisze się go w potrójnych cudzysłowach `""" ... """` tuż pod definicją. Dzięki temu wiadomo, co robi kod.

```py
def format_name(f_name, l_name):
    """Returns a formatted name"""
    return f"{f_name} {l_name}".title()
```
### Try: Except:
Służy do obsługi błedów, sytuacji, które normalnie przerwałyby działanie programu

```py
a = 10
b = 0

try:
    score = a / b
    print("Wynik:", score)
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")

```

`try` – w tym bloku piszesz kod, który może spowodować błąd.

`except` – tutaj piszesz, co zrobić, jeśli wystąpi konkretny błąd (w tym przypadku ZeroDivisionError).


### PrettyTable
Prosta biblioteka, która służy do eleganckiego wyświetlania danych w formie tabeli tekstowej w konsoli
```py
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Charmander", "Fire"])
table.add_row(["Bulbasaur", "Grass/Poison"])
# lub
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Bulbasaur"])
table.add_column("Type", ["Electric", "Fire", "Grass/Poison"])
```
## OOP
---
```py
class Samochod:
    def __init__(self, marka, kolor):
        self.marka = marka
        self.kolor = kolor

auto1 = Samochod("BMW", "czarny")
auto2 = Samochod("Toyota", "czerwony")

print(auto1.marka, auto1.kolor)  # BMW czarny
print(auto2.marka, auto2.kolor)  # Toyota czerwony

```
`def __init__()` to specjalna metoda, która uruchamia się automatycznie w momencie tworzenia obiektu danej klasy
