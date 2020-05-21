// 8kyu - Hello Happy Codevarrior!

/* VVhat ?!?

None of zese codevarriors seemz to remember hiz ovvn name !

Kould you help ?

var albert = new Warrior("Al")
var boris  = new Warrior("Boris")

albert.toString() --> "Hi! my name's Boris" <-- ohoh..

Bugs

function Warrior(n) {
    name = n;
    this.name = function (n) {
        if (n) name = n;
        return name;
    }
}

Warrior.prototype.toString = function () {
    return "Hi! my name's " + this.name();
} */

class Warrior {
    constructor(n) {
        this.n = n
    }
    name(n) {
        if (n) this.n = n
        return this.n
    }
    toString() {
        return "Hi! my name's " + this.n;
    }
}


var albert = new Warrior("Albert")
var boris = new Warrior("Boris")

q = albert.toString() //"Hi! my name's Albert"
q
q = albert.name() // "Albert"
q
q = boris.name() // "Boris"
q

boris.name("Bobo")
q = boris.name() // "Bobo"
q