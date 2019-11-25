// 8kyu - Broken Counter

// function Counter() {
//     this.value = 0;
// }

// Counter.prototype.increase = function () {
//     this.value++;
// };

// Counter.prototype.getValue = function () {
//     return this.value;
// };

// Counter.prototype.reset = function () {
//     this.value = 0;
// };

// function Counter() {
//     this.value = 0;
// }

// Counter.prototype = {
//     increase: function () {
//         this.value++;
//     },
//     getValue: function () {
//         return this.value;
//     },
//     reset: function () {
//         this.value = 0;
//     }
// }

class Counter {
    constructor() { this.reset() }
    increase() { this.value++ }
    getValue() { return this.value }
    reset() { return this.value = 0 }
}


var counter = new Counter()
counter
q = counter.getValue() // 1, 'Initial counter value must be 0');
q

counter.increase();
q = counter.getValue() // 1, 'Counter value must be increased');
q

counter.reset();
q = counter.getValue() // 0, 'Counter value must be 0 after reset');
q