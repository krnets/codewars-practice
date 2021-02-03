### Round To Nearest

You are given a list of numbers (positive / negative integers) and you need to get the nearest entries of a given value.

For example:

The number 10 is given and you need to get the nearest number in this series: 1, 2, 3, 4, 6, 12. The answer should be 12.
```c
int[] intArray = new int[] {1,2,3,4,6,12};
int givenValue = 10;

RoundUp(givenValue, intArray) => {12};
```

If the given number is 5, the result should be {4,6};
```c
int[] intArray = new int[] {1,2,3,4,6,12};
int givenValue = 5;

RoundUp(givenValue, intArray) => {4,6};
```

If the method gets an empty array, it will return an empty array.
```c
int[] intArray = new int[] {};
int givenValue = 42;

RoundUp(givenValue, intArray) => {};
