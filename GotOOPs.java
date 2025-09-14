interface BattleCryStrategy {
    void battleCry();
}

class DefaultBattleCry implements BattleCryStrategy {
    public void battleCry() {
        System.out.println("For Westeros!");
    }
}

class StarkBattleCry implements BattleCryStrategy {
    public void battleCry() {
        System.out.println("The North Remembers!");
    }
}

class TargaryenBattleCry implements BattleCryStrategy {
    public void battleCry() {
        System.out.println("Dracarys!");
    }
}

class LannisterBattleCry implements BattleCryStrategy {
    public void battleCry() {
        System.out.println("Hear Me Roar!");
    }
}

class Character {
    private String name;
    private String house;
    private String realParents = "Unknown";
    private BattleCryStrategy battleCryStrategy;

    public Character(String name, String house, BattleCryStrategy strategy) {
        this.name = name;
        this.house = house;
        this.battleCryStrategy = strategy;
    }

    public void introduce() {
        System.out.println("I am " + name + " of House " + house + ".");
    }

    public void fight() {
        System.out.println(name + " swings a sword!");
    }

    public void battleCry() {
        battleCryStrategy.battleCry();
    }

    public void setRealParents(String realParents) {
        this.realParents = realParents;
    }

    public String revealParents() {
        return "My real parents are: " + realParents;
    }

    public String getName() {
        return name;
    }
}

class Stark extends Character {
    public Stark(String name) {
        super(name, "Stark", new StarkBattleCry());
    }

    public void callDirewolf() {
        System.out.println(getName() + " whistles. A direwolf appears!");
    }
}

class Targaryen extends Character {
    public Targaryen(String name) {
        super(name, "Targaryen", new TargaryenBattleCry());
    }

    public void summonDragon() {
        System.out.println(getName() + " shouts. A dragon lands nearby.");
    }
}

class Lannister extends Character {
    public Lannister(String name) {
        super(name, "Lannister", new LannisterBattleCry());
    }

    public void payDebt() {
        System.out.println(getName() + " pays their debts (or sends someone to do it).");
    }
}

public class Main {
    public static void main(String[] args) {
        Stark jon = new Stark("Jon Snow");
        Targaryen dany = new Targaryen("Daenerys Targaryen");
        Lannister tyrion = new Lannister("Tyrion Lannister");

        jon.setRealParents("Rhaegar Targaryen & Lyanna Stark");

        jon.introduce();
        dany.introduce();
        tyrion.introduce();

        System.out.println("\n--- Battle Cries ---");
        jon.battleCry();
        dany.battleCry();
        tyrion.battleCry();

        System.out.println("\n--- Special Abilities ---");
        jon.callDirewolf();
        dany.summonDragon();
        tyrion.payDebt();

        System.out.println("\n--- Fights ---");
        jon.fight();
        dany.fight();
        tyrion.fight();

        System.out.println("\n--- Family Secrets ---");
        System.out.println(jon.revealParents());
    }
}
