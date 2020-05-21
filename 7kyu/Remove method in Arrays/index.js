// 7kyu - Remove method in Arrays

/* Some people really wonder why JavaScript arrays don't have a remove function to remove an element.
Go ahead and make one.

var someArray = [1, 2, 3];
someArray.remove(1);

This should remove the element on index 1 making someArray = [1, 3]
Note: You need to handle invalid input. ie If index not a number or out of bounds return array unchanged. */

Array.prototype.remove = function (index) {
    if (index >= 0 && index < this.length)
        return this.splice(index, 1)
}

someArray = [1, 2, 3, 4, 5, 6, 7, 8]
someArray.remove(1)
someArray // [1, 3]
q = someArray.remove(2)
q
someArray