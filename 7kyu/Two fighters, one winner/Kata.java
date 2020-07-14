/*
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious.
Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack will be integers larger than 0. You can mutate the Fighter objects.
*/

class Fighter {
    public String name;
    public int health, damagePerAttack;

    public Fighter(String name, int health, int damagePerAttack) {
        this.name = name;
        this.health = health;
        this.damagePerAttack = damagePerAttack;
    }
}

/*public class Kata {
    public static String declareWinner(Fighter fighter1, Fighter fighter2, String firstAttacker) {
        if (firstAttacker == fighter1.name)
             fighter2.health -= fighter1.damagePerAttack;
        else fighter1.health -= fighter2.damagePerAttack;

        String prevAttacker = firstAttacker;

        while (fighter1.health >= 0 && fighter2.health >= 0) {
            if (prevAttacker == fighter1.name) {
                fighter1.health -= fighter2.damagePerAttack;
                prevAttacker = fighter2.name;
            } else {
                fighter2.health -= fighter1.damagePerAttack;
                prevAttacker = fighter1.name;
            }
        }
        return fighter1.health <= 0 ? fighter2.name : fighter1.name;
    }
}*/

public class Kata {
    public static String declareWinner(Fighter fighter1, Fighter fighter2, String firstAttacker) {
        var f1AttackingMoves = Math.ceil((double) fighter2.health / fighter1.damagePerAttack);
        var f2AttackingMoves = Math.ceil((double) fighter1.health / fighter2.damagePerAttack);
        return f2AttackingMoves < f1AttackingMoves ? fighter2.name : f1AttackingMoves < f2AttackingMoves ? fighter1.name : firstAttacker;
    }
}

