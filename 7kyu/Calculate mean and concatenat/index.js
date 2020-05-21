// 7kyu - Calculate mean and concatenate string

/* You will be given an array which will include both integers and characters.
Return an array of length 2 with a[0] representing the mean of the ten integers as a floating point number. 
There will always be 10 integers and 10 characters. 
Create a single string with the characters and return it as a[1] while maintaining the original order. */

function mean(lst) {
    let nums = lst.filter(v => v * 1 == v)
    let mean = nums.reduce((a, b) => a + Number(b), 0) / nums.length
    let string = lst.filter(v => !nums.includes(v)).join('')
    return [mean, string]
}

var lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']
q = mean(lst) // [3.6, "udiwstagwo"]
q
var lst = ['0', 'c', '7', 'x', '6', '2', '3', '5', 'w', '7', '0', 'y', 'v', 'u', 'h', 'i', 'n', 'u', '0', '0']
q = mean(lst) // [3.0, "cxwyvuhinu"]
q
var lst = ['0', 'u', 'a', 'y', '0', 'a', '9', 'q', '3', 'v', 'g', '7', '6', '4', 'y', 'd', '8', '6', '0', 'd']
q = mean(lst) // [4.3, "uayaqvgydd"]
q
var lst = ['s', 'n', '9', 'l', '0', 'm', 'i', 'z', '9', '7', 'y', '4', 'z', '3', '3', 'k', '4', '1', '0', 'k']
q = mean(lst) // [4.0, "snlmizyzkk"]
q
var lst = ['5', 'v', 'u', 'k', '8', '4', '9', 'b', '9', 'g', '5', 'z', '3', 'f', '6', 'u', 'i', '6', '6', 't']
q = mean(lst) // [6.1, "vukbgzfuit"]
q
var lst = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '0', 'a', 'a', 'd', 'd', 'g', 'q', 'u', 'v', 'y', 'y']
q = mean(lst) // [0.9, "aaddgquvyy"]
q
var lst = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'a', 'a', 'd', 'd', 'g', 'q', 'u', 'v', 'y', 'y']
q = mean(lst) // [1.0, "aaddgquvyy"]
q
