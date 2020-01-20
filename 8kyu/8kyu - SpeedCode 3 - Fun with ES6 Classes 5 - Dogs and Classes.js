// 8kyu - SpeedCode 3 × Fun with ES6 Classes 5 - Dogs and Classes

// Preloaded for you is a class Dog:

class Dog {
    constructor(name, age, gender, species, size, master, loyal) {
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.species = species;
        this.legs = 4;
        this.size = size;
        this.master = master;
        this.loyal = loyal;
    }
}

// You are then given a working class Labrador as your initial code.

// class Labrador {
//   constructor(name, age, gender, master) {
//     this.name = name;
//     this.age = age;
//     this.gender = gender;
//     this.species = "Labrador";
//     this.legs = 4;
//     this.size = "Large";
//     this.master = master;
//     this.loyal = true;
//   }
// }

// Shorten it so that it meets the strict character count requirements for this Kata.
// Quick, get your timer out and get ready to time yourself. Are you ready? Ready, get set, GO!!! :D

// class Labrador extends Dog {
//   constructor(name, age, gender, master) {
//     super(name, age, gender)
//     this.species = "Labrador";
//     this.legs = 4;
//     this.size = "Large";
//     this.master = master;
//     this.loyal = true;
//   }
// }

class Labrador extends Dog {
    constructor(name, age, gender, master) {
        super(name, age, gender, "Labrador", "Large", master, true)
    }
}


var spitsy = new Labrador("Spitsy", 10, "Male", "Donald");
q = spitsy.name // "Spitsy"
q
q = spitsy.age // 10
q
q = spitsy.gender // "Male"
q
q = spitsy.species // "Labrador"
q
q = spitsy.legs // 4
q
q = spitsy.size // "Large"
q
q = spitsy.master // "Donald"
q
q = spitsy.loyal // true
q

var edward = new Labrador("Edward", 3, "Male", "Emma");
q = edward.name // "Edward"
q
q = edward.age // 3
q
q = edward.gender // "Male"
q
q = edward.species // "Labrador"
q
q = edward.legs // 4
q
q = edward.size // "Large"
q
q = edward.master // "Emma"
q
q = edward.loyal // true
q