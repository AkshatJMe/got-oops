# Parent class (Base class)
class Character:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.__real_parents = "Unknown"  # Encapsulated (private attribute)

    # Public method to introduce the character
    def introduce(self):
        print(f"I am {self.name} of House {self.house}.")

    # Encapsulation: Getter method to reveal secret info
    def reveal_parents(self):
        return f"My real parents are: {self.__real_parents}"

    # Encapsulation: Setter method to update secret info
    def set_real_parents(self, parents):
        self.__real_parents = parents

    # Polymorphic method (can be overridden)
    def battle_cry(self):
        print("For Westeros!")

    # Bonus method: every character can fight
    def fight(self):
        print(f"{self.name} swings a sword!")


# Subclass: House Stark
class Stark(Character):
    def __init__(self, name):
        super().__init__(name, "Stark")
        self.has_direwolf = True

    # Polymorphism: override battle_cry
    def battle_cry(self):
        print("The North Remembers!")

    def call_direwolf(self):
        if self.has_direwolf:
            print(f"{self.name} whistles. A direwolf appears!")
        else:
            print(f"{self.name} doesn't have a direwolf.")


# Subclass: House Targaryen
class Targaryen(Character):
    def __init__(self, name):
        super().__init__(name, "Targaryen")
        self.has_dragon = True

    # Polymorphism: override battle_cry
    def battle_cry(self):
        print("Dracarys!")

    def summon_dragon(self):
        if self.has_dragon:
            print(f"{self.name} shouts. A dragon lands nearby.")
        else:
            print(f"{self.name} has no dragon to summon.")


# Subclass: House Lannister
class Lannister(Character):
    def __init__(self, name):
        super().__init__(name, "Lannister")
        self.rich = True

    # Polymorphism: override battle_cry
    def battle_cry(self):
        print("Hear Me Roar!")

    def pay_debt(self):
        print(f"{self.name} pays their debts (or sends someone to do it).")


# Main Program
def main():
    # Create characters
    jon = Stark("Jon Snow")
    daenerys = Targaryen("Daenerys Targaryen")
    tyrion = Lannister("Tyrion Lannister")

    # Set secret parent info (encapsulation)
    jon.set_real_parents("Rhaegar Targaryen & Lyanna Stark")

    # Introduce characters
    jon.introduce()
    daenerys.introduce()
    tyrion.introduce()

    print("\n--- Battle Cries (Polymorphism) ---")
    jon.battle_cry()
    daenerys.battle_cry()
    tyrion.battle_cry()

    print("\n--- Special Abilities ---")
    jon.call_direwolf()
    daenerys.summon_dragon()
    tyrion.pay_debt()

    print("\n--- Fights ---")
    jon.fight()
    daenerys.fight()
    tyrion.fight()

    print("\n--- Family Secrets (Encapsulation) ---")
    print(jon.reveal_parents())  # Only Jon has real parents set

    # Try accessing private variable directly (will fail)
    try:
        print(jon.__real_parents)
    except AttributeError:
        print("Error: Cannot access private attribute '__real_parents' directly!")

if __name__ == "__main__":
    main()
