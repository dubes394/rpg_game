class Character:
                
    def __init__(self, name, health=100, weapon="Sword", accessories = None, aggression = 0):
        self.name = name
        self.__health = health
        self.weapon = weapon
        if accessories is None:
            accessories = ["Basic Armour"]
        self.accessories = accessories
        self.__aggression = aggression
        self.inventory = []
        

    def show_stats(self):
      return (
    f"Name: {self.name}, "
    f"Health: {self.__health}, "
    f"Weapon: {self.weapon}, "
    f"Accessories: {self.accessories}, "
    f"Aggression: {self.__aggression}"
)
    def heal(self, health):
        if self.__health + health > 100:
            self.__health = 100
        else:
            self.__health = self.__health + health       
            
    def take_damage(self, damage):
           if self.__health - damage <= 0:
               self.__health = 0
           else:
               self.__health = self.__health - damage
               
    def attack(self, enemy):
        enemy.take_damage(self.weapon.damage)
        return f"{self.name} attacked {enemy.name} for {self.weapon.damage} damage"
    
    
    def use_potion(self, potion):
        self.heal(potion.heal_amount)
        self.inventory.remove(potion)  
        
    def add_item(self, item):
        return self.inventory.append(item)
    
    def show_inventory(self):
        for i in self.inventory:
            print(i)
                  

class Weapon:  
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
    def __str__(self):
        return f"{self.name} ({self.damage} damage)"
    
class Potion:
    def __init__(self, name, heal_amount):
        self.name = name
        self.heal_amount = heal_amount  
        
    def __str__(self):
        return f"{self.name} healed by (+{self.heal_amount}HP)"
        
sword = Weapon("Sword", 20)
axe = Weapon("axe", 15)

orc=Character(
    "Orc",
    weapon=axe
)

# health_potion = Potion("Health Potion",30)

knight = Character(
    "Knight",
    weapon=sword
    )

print(orc.show_stats())

knight.attack(orc)
print(knight.attack(orc))

print(orc.show_stats())
              
# knight.add_item(health_potion)  
# print(knight.inventory)  
# knight.show_inventory()

# knight.add_item(health_potion)
# print("Before:")

# knight.show_inventory()
# knight.use_potion(health_potion)

# print("After:")
# knight.show_inventory()        

# knight = Character(
#     "Knight",
#     weapon= ()
# )

# knight.add_items(heal_amount)
# print(knight.inventory)


# knight.take_damage(40)
# print(knight.show_stats())

# health_potion = Potion("Health Potion", 30)
# knight.use_potion(health_potion)
# print(knight.show_stats())