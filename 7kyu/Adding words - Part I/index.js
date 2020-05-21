// 7kyu - Adding words - Part I

/* Add two English words together

Implement a class Arith such that

  //javascript
  var k = new Arith("three");
  k.add("seven"); //this should return "ten"  */

class Arith {
    constructor(a) { 
        this.a = a 
    }
    add(b) { 
        let numbers = ['zero', 'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve',
                       'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
        return numbers[numbers.indexOf(this.a) + numbers.indexOf(b)]
    }
}

i = new Arith('three')
i
q = i.add('seven') // "ten"
q
q = i.add('eight') // "eleven"
q
q = i.add('zero') // "three"
q
