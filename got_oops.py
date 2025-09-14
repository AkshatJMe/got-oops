from abc import ABC, abstractmethod

# === Interfaces / Abstractions === #

class BattleCryStrategy(ABC):
    @abstractmethod
    def battle_cry(self):
        pass

class HasDirewolf(ABC):
    def call_direwolf(self):
        print("A direwolf appears!")

class HasDragon(ABC):
    def summon_dragon(self):
        print("A dragon lands nearby!")

class PaysDebt(ABC):
    def pay_debt(self):
        print("Pays their debts (or sends someone to do it).")


# === Concrete Battle Cry Strategies === #

class DefaultBattleCry(BattleCryStrategy):
    def battle_cry(self):
        print("For Westeros!")

class StarkBattleCry(BattleCryStrategy):
    def battle_cry(self):
        print("The North Remembers!")

class TargaryenBattleCry(BattleCryStrategy):
    def battle_cry(self):
        print("Dracarys!")

class LannisterBattleCry(BattleCryStrategy):
    def battle_cry(self):
        print("Hear Me Roar!")


# === Base Character Entity === #

class Character:
    def __init__(self, name, house, battle_cry_strategy: BattleCryStrategy):
        self.name = name
        self.house = house
        self.__real_parents = "Unknown"  # Encapsulation
        self.battle_cry_strategy = battle_cry_strategy

    def introduce(self):
        print(f"I am {self.name} of House {self.house}.")

    def fight(self):
        print(f"{self.name} swings a sword!")

    def battle_cry(self):
        self.battle_cry_strategy.battle_cry()

    # Encapsulated getters/setters for private attributes
    def set_real_parents(self, parents: str):
        self.__real_parents = parents

    def reveal_parents(self):
        return f"My real parents are: {self.__real_parents}"


# === Concrete Characters with Composition === #

class Stark(Character, HasDirewolf):
    def __init__(self, name):
        super().__init__(name, "Stark", StarkBattleCry())


class Targaryen(Character, HasDragon):
    def __init__(self, name):
        super().__init__(name, "Targaryen", TargaryenBattleCry())


class Lannister(Character, PaysDebt):
    def __init__(self, name):
        super().__init__(name, "Lannister", LannisterBattleCry())


class Commoner(Character):
    def __init__(self, name):
        super().__init__(name, "Unknown", DefaultBattleCry())


# === Driver Code === #

def main():
    # Create characters
    jon = Stark("Jon Snow")
    daenerys = Targaryen("Daenerys Targaryen")
    tyrion = Lannister("Tyrion Lannister")
    gendry = Commoner("Gendry")

    # Set real parent (encapsulation)
    jon.set_real_parents("Rhaegar Targaryen & Lyanna Stark")

    # Introductions
    jon.introduce()
    daenerys.introduce()
    tyrion.introduce()
    gendry.introduce()

    print("\n--- Battle Cries ---")
    jon.battle_cry()
    daenerys.battle_cry()
    tyrion.battle_cry()
    gendry.battle_cry()

    print("\n--- Fights ---")
    jon.fight()
    daenerys.fight()
    tyrion.fight()
    gendry.fight()

    print("\n--- Special Abilities ---")
    jon.call_direwolf()
    daenerys.summon_dragon()
    tyrion.pay_debt()

    print("\n--- Secrets (Encapsulation) ---")
    print(jon.reveal_parents())

    # Attempt to access private data directly
    try:
        print(jon.__real_parents)
    except AttributeError:
        print("Error: Cannot access '__real_parents' directly. Use a getter!")


if __name__ == "__main__":
    main()
