// 7kyu - Trim method

/* The trim() method removes whitespace from both sides of a string. w3schools
In this kata we are going to extend the trim method to be able to 
remove any character(upper and lower cases) from both sides of a string.

Create a method called trim which removes the passed parameter c(upper and lower cases) from the leading and tailing of the string.
1- If no parameter is being passed you need to remove the leading and tailing spaces.
2- The passed parameter will only be alphabet(upper and lower cases) characters.

string = "LLLHello Worldlll" and c = "l" => "Hello World"
string = "Visca ElbarcaXxX" and c = "X" => "Visca Elbarca"

Fundamentals | Strings | Regular Expressions | Declarative Programming | Advanced Language Features | 
Methods | Functions | Object-oriented Programming | Control Flow | Basic Language Features */

// String.prototype.trim = function (letter) {
//     return letter ?
//         this.replace(new RegExp(`^${letter}+|${letter}+$`, 'gi'), '') :
//         this.replace(/^\s+/, '').replace(/\s+$/, '')
// }

// String.prototype.trim = function (letter) {
//     letter = letter || ' '
//     return this.replace(new RegExp(`^${letter}+|${letter}+$`, 'gi'), '')
// }

String.prototype.trim = function (c = ' ') {
    return this.replace(new RegExp(`^${c}+|${c}+$`, 'gi'), '')
}

q = "LLLHello Worldlll".trim("l"), "Hello World"
q
q = "   Hello World                 ".trim(), "Hello World"
q
q = "XVisca ElbarcaXX".trim("X"), "Visca Elbarca"
q