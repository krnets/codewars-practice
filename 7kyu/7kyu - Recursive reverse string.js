/* 7 kyu - Recursive reverse string

    ##Do you know how to write a recursive function? Let's test it!
    * Definition: Recursive function is a function that calls itself during its execution *

    function factorial(n) {
      return n <= 1 ? 1 : n * factorial(n-1) 
    }

    Your objective is to complete a recursive function reverse() that receives str as String 
    and returns the same string in reverse order

        reverse function should be executed exactly N times. N = length of the input string
        helper functions are not allowed
        changing the signature of the function is not allowed

    All tests for this Kata are randomly generated, besides checking the reverse logic 
    they will count how many times the reverse() function has been executed. */


function reverse(str) {
    if (str.length == 1) return str
    return str.slice(-1) + reverse(str.slice(0, -1))
}

// function reverse(str) {
//     if (str.length == 1) return str
//     return reverse(str.slice(1)) + str[0]
// }

// const reverse = ([head, ...tail]) => tail.length ? reverse(tail) + head : head
// const reverse = ([h, ...t]) => t[0] ? reverse(t) + h : h
// const reverse = str => str.length == 1 ? str : reverse(str.slice(1)) + str[0]
// const reverse = str => str[1] ? reverse(str.slice(1)) + str[0] : str[0]


q = reverse("hello world") // "dlrow olleh" (N = 11)
q
q = reverse("abcd") // "dcba" (N = 4)
q
q = reverse("12345") // "54321" (N = 5)
q