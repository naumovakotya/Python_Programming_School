# Python Homework №4: Battle Game Simulation

This repository contains a game simulation built with object-oriented programming, demonstrating the use of classes, inheritance, and custom methods. The program includes battles between various character classes, with detailed logging of each fight.

## Overview of Features
- **Class Inheritance**: The game includes multiple character types, such as `Warrior`, `Knight`, `Defender`, and `Vampire`, all inheriting common behavior from the `Warrior` base class.
- **Polymorphism**: Each character class overrides certain methods (e.g., special abilities like vampirism for `Vampire` or defense for `Defender`).
- **Battle System**: The `Battle` class manages fights between individual characters or entire armies, with support for logging each battle.
- **Operator Overloading**: The `Warrior` and `Army` classes use operator overloading (`+`, `*`) to modify the health and attack of the characters dynamically.

## Character Classes

1. [**Warrior**](https://github.com/naumovakotya/Python_Programming_School/blob/main/HW_4/Warrior.py): 
   - Base class with health, attack, and basic attack mechanics.
   - Methods include `deal_damage()`, `get_damage()`, and `is_alive()`.

2. [**Knight**](https://github.com/naumovakotya/Python_Programming_School/blob/main/HW_4/Knight.py): 
   - Inherits from `Warrior`, with increased attack power.

3. [**Defender**](https://github.com/naumovakotya/Python_Programming_School/blob/main/HW_4/Defender.py):
   - A defensive character with reduced damage intake thanks to a defense attribute.

4. [**Vampire**](https://github.com/naumovakotya/Python_Programming_School/blob/main/HW_4/Vampire.py):
   - A character that heals based on the damage it deals, using its vampirism ability.

## Army and Battle

- [**Army**](https://github.com/naumovakotya/Python_Programming_School/blob/main/HW_4/Army.py):
  - Manages a group of warriors, adding members and organizing battles.

- [**Battle**](https://github.com/naumovakotya/Python_Programming_School/blob/main/HW_4/Battle.py):
  - Handles the logic of a fight between two armies, including logging the details of each round.
  - Supports individual and group battles, with detailed round-by-round logging in CSV files for further analysis.

## Logging
- Each fight can be logged using the [`log.py`](https://github.com/naumovakotya/Python_Programming_School/blob/main/HW_4/log.py) module, generating detailed reports of the battle rounds, including the type of characters, their health, damage, and any special attributes like defense or vampirism.

## Example Usage

```python
import Army as a
import log
import Warrior as w
import Knight as k
import Defender as d
import Vampire as v

# Create two armies
army1 = a.Army('First Army')
army2 = a.Army('Second Army')

# Fill the armies with different types of warriors
army1.add_members(50, w.Warrior(), k.Knight(), d.Defender(), v.Vampire())
army2.add_members(50, w.Warrior(), k.Knight(), d.Defender(), v.Vampire())

# Log the battle between the two armies
log.logging(army1, army2)

