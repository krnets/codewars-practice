// 7kyu - Two fighters, one winner

/* Create a function that returns the name of the winner in a fight between two fighters.
Each fighter takes turns attacking the other and whoever kills the other first is victorious. 
Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack will be integers larger than 0. You can mutate the Fighter objects. */

function Fighter(name, health, damagePerAttack) {
    this.name = name;
    this.health = health;
    this.damagePerAttack = damagePerAttack;
    this.toString = function () {
        return this.name;
    }
}

function declareWinner(fighter1, fighter2, firstAttacker) {
    let f1 = Math.ceil(fighter1.health / fighter2.damagePerAttack)
    let f2 = Math.ceil(fighter2.health / fighter1.damagePerAttack)
    return f1 < f2 ? fighter2.name : f2 < f1 ? fighter1.name : firstAttacker
}

q = declareWinner(new Fighter("Lew", 10, 2), new Fighter("Harry", 5, 4), "Lew") // "Lew"
q
q = declareWinner(new Fighter("Lew", 10, 2), new Fighter("Harry", 5, 4), "Harry") // "Harry"
q
q = declareWinner(new Fighter("Harald", 20, 5), new Fighter("Harry", 5, 4), "Harry") // "Harald"
q
q = declareWinner(new Fighter("Harald", 20, 5), new Fighter("Harry", 5, 4), "Harald") // "Harald"
q
q = declareWinner(new Fighter("Jerry", 30, 3), new Fighter("Harald", 20, 5), "Jerry") // "Harald"
q
q = declareWinner(new Fighter("Jerry", 30, 3), new Fighter("Harald", 20, 5), "Harald") // "Harald"
q