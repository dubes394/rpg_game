# rpg_game
A simple console-based RPG project built in Python to practice Object-Oriented Programming (OOP) concepts

## Features

- Create characters with health, weapons, and inventory
- Equip weapons with different damage values
- Attack enemy characters
- Take and heal damage
- Use health potions
- Store items in inventory
- Display character stats and inventory

## OOP Concepts Practiced

- Classes and Objects
- Constructors (`__init__`)
- Instance Attributes
- Encapsulation (private health attribute)
- Composition (Character has a Weapon)
- Collections of Objects (Inventory)
- Methods and Object Interaction
- Special Methods (`__str__`)
- Code Reusability and DRY Principles

## Project Structure

```text
Character
├── Health
├── Weapon
├── Inventory
├── Attack
├── Heal
└── Use Potion

Weapon
├── Name
└── Damage

Potion
├── Name
└── Heal Amount
```

## Example Gameplay

```python
sword = Weapon("Sword", 20)
axe = Weapon("Axe", 15)

knight = Character("Knight", weapon=sword)
orc = Character("Orc", weapon=axe)

print(knight.attack(orc))
```

Output:

```text
Knight attacked Orc for 20 damage
```

## Purpose

This project was built as part of my Python learning journey to strengthen OOP fundamentals before moving on to larger backend, FastAPI, and production-oriented projects.

## Technologies

- Python 3

## Future Improvements

- Aggression/Mana system
- Multiple potion types
- Armor and defense mechanics
- Enemy AI
- Save/Load game state
- File persistence
