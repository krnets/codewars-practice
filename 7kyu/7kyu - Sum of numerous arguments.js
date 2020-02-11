// 7kyu - Sum of numerous arguments

/* After calling the function findSum() with any number of non-negative integer arguments, 
it should return the sum of all those arguments. If no arguments are given, 
the function should return 0, if negative arguments are given, it should return -1.

Hint: research the arguments object on google or read Chapter 4 from Eloquent Javascript */

// const findSum = (...args) => args.reduce((a, b) => a + b, 0);
// const findSum = (...args) => args.some(v => v < 0) ? -1 : args.reduce((a, b) => a + b, 0);

const findSum = (...nums) => nums.reduce((a, b) => (a < 0 || b < 0 ? -1 : a + b), 0);

q = findSum(1, 3, 5); // 9, "1 + 3 + 5 = 9"
q;
q = findSum(0, 3, 9, 2); // 14, "0+3+9+2 = 14"
q;
q = findSum(); // 0, "If no arguments, function should return 0"
q;
q = findSum(1, -2, 4); // -1, "If negative arguments are passed, function should return -1"
q;
q = findSum(0); // 0, "The sum of 0 is 0"
q;
q = findSum(1, 2, 3, 4); // returns 10
q;
q = findSum(1, -2); // returns -1
q;
q = findSum(); // returns 0
q;
