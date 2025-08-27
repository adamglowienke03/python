# Python
---
### Spis treści
- [Podstawy](#podstawy)
  - [Docstrings](#docstrings)
  - [Try: Except:](#try-except)

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
