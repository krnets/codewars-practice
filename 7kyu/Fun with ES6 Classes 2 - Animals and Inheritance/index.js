// 7kyu - Fun with ES6 Classes #2 - Animals and Inheritance

/* Preloaded for you in this Kata is a class Animal

Define the following classes that inherit from Animal.
I. Shark

The constructor function for Shark should accept 3 arguments in total in the following order: 
name, age, status. All sharks should have a leg count of ** 0 (since they obviously do not have any legs) and should have a
species of "shark" .**

II. Cat

The constructor function for Cat should accept the same 3 arguments as with Shark: 
name, age, status. Cats should always have a leg count of 4 and a species of "cat".

Furthermore, the introduce/Introduce method for Cat should be identical to the original 
except there should be exactly 2 spaces and the words "Meow meow!" after the phrase. For example:

var example = new Cat("Example", 10, "Happy");
example.introduce() === "Hello, my name is Example and I am 10 years old.  Meow meow!"; // Notice the TWO spaces - very important

III. Dog

The Dog constructor should accept 4 arguments in the specified order: 
name, age, status, master. master is the name of the dog's master which will be a string. 
Furthermore, dogs should have 4 legs and a species of "dog".

Dogs have an identical introduce/Introduce method as any other animal, but they have their own method 
called greetMaster/GreetMaster which accepts no arguments and returns "Hello (insert_master_name_here)" 
(of course not the literal string but replace the (insert_master_name_here) with the name of the dog's master). */

class Animal {
    constructor(name, age, legs, species, status) {
        this.name = name;
        this.age = age;
        this.legs = legs;
        this.species = species;
        this.status = status;
    }
    introduce() {
        return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
    }
}

class Shark extends Animal {
    constructor(name, age, status) {
        super(name, age, 0, 'shark', status)
    }
}

class Cat extends Animal {
    constructor(name, age, status) {
        super(name, age, 4, 'cat', status)
    }
    introduce() {
        return `${super.introduce()}  Meow meow!`
    }
}

class Dog extends Animal {
    constructor(name, age, status, master) {
        super(name, age, 4, 'dog', status)
        this.master = master
    }
    greetMaster() {
        return `Hello ${this.master}`
    }
}


var billy = new Shark("Billy", 3, "Alive and well");
q = billy.name // "Billy"
q
q = billy.age // 3
q
q = billy.legs // 0
q
q = billy.species // "shark"
q
q = billy.status //  "Alive and well"
q
q = billy.introduce() // `Hello, my name is Billy and I am 3 years old.`
q

var charles = new Shark("Charles", 8, "Finding a mate");
q = charles.name // "Charles"
q
q = charles.age //  8
q
q = charles.legs // 0
q
q = charles.species // "shark"
q
q = charles.status // "Finding a mate"
q
q = charles.introduce(), `Hello, my name is Charles and I am 8 years old.`
q

var cathy = new Cat("Cathy", 7, "Playing with a ball of yarn");
q = cathy.name // "Cathy"
q
q = cathy.age // 7
q
q = cathy.legs // 4
q
q = cathy.species // "cat"
q
q = cathy.status // "Playing with a ball of yarn"
q
q = cathy.introduce() // "Hello, my name is Cathy and I am 7 years old.  Meow meow!"
q

var spitsy = new Cat("Spitsy", 6, "sleeping");
q = spitsy.name // "Spitsy"
q
q = spitsy.age // 6
q
q = spitsy.legs // 4
q
q = spitsy.species // "cat"
q
q = spitsy.status // "sleeping"
q
q = spitsy.introduce() // "Hello, my name is Spitsy and I am 6 years old.  Meow meow!"
q

var doug = new Dog("Doug", 12, "Serving his master", "Eliza");
q = doug.name // "Doug"
q
q = doug.age // 12
q
q = doug.legs // 4
q
q = doug.species // "dog"
q
q = doug.status // "Serving his master"
q
q = doug.introduce() // "Hello, my name is Doug and I am 12 years old."
q
q = doug.greetMaster() // "Hello Eliza"
q