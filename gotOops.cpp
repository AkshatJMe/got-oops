#include <iostream>
#include <memory>
using namespace std;

// === Strategy Interface ===
class BattleCryStrategy {
public:
    virtual void battleCry() const = 0;
    virtual ~BattleCryStrategy() = default;
};

// === Concrete Strategies ===
class DefaultBattleCry : public BattleCryStrategy {
public:
    void battleCry() const override {
        cout << "For Westeros!" << endl;
    }
};

class StarkBattleCry : public BattleCryStrategy {
public:
    void battleCry() const override {
        cout << "The North Remembers!" << endl;
    }
};

class TargaryenBattleCry : public BattleCryStrategy {
public:
    void battleCry() const override {
        cout << "Dracarys!" << endl;
    }
};

class LannisterBattleCry : public BattleCryStrategy {
public:
    void battleCry() const override {
        cout << "Hear Me Roar!" << endl;
    }
};

// === Base Character Class ===
class Character {
protected:
    string name;
    string house;
    string realParents = "Unknown";
    unique_ptr<BattleCryStrategy> battleCryStrategy;

public:
    Character(string n, string h, BattleCryStrategy* strategy)
        : name(move(n)), house(move(h)), battleCryStrategy(strategy) {}

    virtual ~Character() = default;

    virtual void introduce() const {
        cout << "I am " << name << " of House " << house << "." << endl;
    }

    virtual void fight() const {
        cout << name << " swings a sword!" << endl;
    }

    virtual void battleCry() const {
        battleCryStrategy->battleCry();
    }

    void setRealParents(const string& rp) {
        realParents = rp;
    }

    string revealParents() const {
        return "My real parents are: " + realParents;
    }

    string getName() const { return name; }
};

// === Concrete Character Classes ===
class Stark : public Character {
public:
    Stark(string name)
        : Character(move(name), "Stark", new StarkBattleCry()) {}

    void callDirewolf() const {
        cout << name << " whistles. A direwolf appears!" << endl;
    }
};

class Targaryen : public Character {
public:
    Targaryen(string name)
        : Character(move(name), "Targaryen", new TargaryenBattleCry()) {}

    void summonDragon() const {
        cout << name << " shouts. A dragon lands nearby." << endl;
    }
};

class Lannister : public Character {
public:
    Lannister(string name)
        : Character(move(name), "Lannister", new LannisterBattleCry()) {}

    void payDebt() const {
        cout << name << " pays their debts (or sends someone to do it)." << endl;
    }
};

// === Main ===
int main() {
    Stark jon("Jon Snow");
    Targaryen dany("Daenerys Targaryen");
    Lannister tyrion("Tyrion Lannister");

    jon.setRealParents("Rhaegar Targaryen & Lyanna Stark");

    jon.introduce();
    dany.introduce();
    tyrion.introduce();

    cout << "\n--- Battle Cries ---" << endl;
    jon.battleCry();
    dany.battleCry();
    tyrion.battleCry();

    cout << "\n--- Special Abilities ---" << endl;
    jon.callDirewolf();
    dany.summonDragon();
    tyrion.payDebt();

    cout << "\n--- Fights ---" << endl;
    jon.fight();
    dany.fight();
    tyrion.fight();

    cout << "\n--- Family Secrets ---" << endl;
    cout << jon.revealParents() << endl;

    return 0;
}
