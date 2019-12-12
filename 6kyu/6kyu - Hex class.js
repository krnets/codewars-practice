// 6kyu - Hex class

/* Create a class Hex which takes a number as an argument.
Adding a hex object to a number (by using valueOf) generates a number, 
but calling toString or toJSON will show its hexidecimal value starting with "0x". 
To make hex objects comparable you have to provide a method equals.

var FF = new Hex(255);
FF.toString() == "0xFF";
FF.valueOf() + 1 == 256;

Also create two methods, plus and minus which will add or subtract a number or Hex object and return a new Hex object.

var a = new Hex(10);
var b = new Hex(5);
a.plus(b).toJSON() == "0xF";

Also, create a parse class method that can parse Hexidecimal numbers and convert them to standard decimal numbers:

Hex.parse("0xFF") == 255;
Hex.parse("FF") == 255;

Note: If you define both valueOf and toString, "Hex value:" + new Hex(255) may not behave as expected!
Fundamentals | Algorithms | Parsing | Strings | Numbers | Data Conversion | Data | Classes | Basic Language Features | Object-oriented Programming */

// function Hex(value){
//     //...
//     this.valueOf = function(){};
//     this.toString = function(){};
//     this.toJSON = function(){};
//     this.plus = function(){};
//     this.minus = function(){}
//   }
//   Hex.parse = function(string){ 
//     //...
//   }

class Hex {
    constructor(value) { this.value = value }
    valueOf()  { return Number(this.value) }
    toString() { return '0x' + this.value.toString(16).toUpperCase() }
    toJSON()   { return this.toString() }
    plus(n)    { return new Hex(this.value + Number(n)) }
    minus(n)   { return new Hex(this.value - Number(n)) }
    static parse(string) { return parseInt(string, 16) }
}

FF = new Hex(255)

q = FF.toString() // "0xFF"
q
q = FF + 1 // 256
q
q = FF.toJSON() // "0xFF"
q
q = FF.minus(1).toString() // "0xFE"
q
q = FF.minus(FF).valueOf() == 0 // true / "Should be zero"
q
q = new Hex(10).plus(5).toString() // "0xF"
q
q = Hex.parse("FF") // 255
q
q = Hex.parse("0xFF") // 255
q