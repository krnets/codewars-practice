// 7kyu - Method For Counting Total Occurence Of Specific Digits

/* We need a method in the List Class that may count specific digits from a given list of integers.
This marked digits will be given in a second list.

The method.countSpecDigits() will accept two arguments, a list of an uncertain amount of integers
integersLists(and of an uncertain amount of digits, too) and a second list, digitsList that has the
specific digits to count which length cannot be be longer than 10(It 's obvious, we've got ten digits).

The method will output a list of tuples, each tuple having two elements, the first one will be a digit to count,
and second one, its corresponding total frequency in all the integers of the first list.
This list of tuples should be ordered with the same order that the digits have in digitsList */

// function List() {
//     this.countSpecDigits = function (integersList, digitsList) {
//         let cmp = integersList.map(String)
//         return digitsList.map(v => [v, cmp.join('').replace(new RegExp(`[^${v}]`, 'g'), '').length])
//     }
// }

function List() {
    this.countSpecDigits = function (integersList, digitsList) {
        return digitsList.map(v => [v, integersList.join('').split(v).length - 1])
    }
}

// class List {
//     countSpecDigits(array, digits) {
//         return digits.map(digit => [digit, array.join ``.split(digit).length - 1]);
//     }
// }

l = new List();

integersList = [1, 1, 2, 3, 1, 2, 3, 4];
digitsList = [1, 3];
q = l.countSpecDigits(integersList, digitsList) // [[1, 3], [3, 2]]
q

integersList = [-18, -31, 81, -19, 111, -888];
digitsList = [1, 8, 4];
q = l.countSpecDigits(integersList, digitsList) // [[1, 7], [8, 5], [4, 0]]
q

integersList = [-77, -65, 56, -79, 6666, 222];
digitsList = [1, 8, 4];
q = l.countSpecDigits(integersList, digitsList) //  [[1, 0], [8, 0], [4, 0]]
q

integersList = [-77, -65, 56, -79, 6666, 222];
digitsList = [];
q = l.countSpecDigits(integersList, digitsList) // []
q

integersList = [];
digitsList = [1, 8, 4];
q = l.countSpecDigits(integersList, digitsList) // [[1, 0], [8, 0], [4, 0]]
q