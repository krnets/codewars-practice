// 3kyu - Upside-Down Numbers - Challenge Edition

/* In the original kata by @KenKamau you were limited to integers below 2^17. 
Here, you will be given strings of digits of up to 42 characters in length (upper bound is 10^42 - 1).

Your task is essentially the same, but an additional challenge is creating a fast, efficient solution.

Input:
Your function will receive two strings, each comprised of digits representing a positive integer. 
These two values will represent the upper and lower bounds of a range.

Output:
Your function must return the number of valid upside down numbers within the range of the two input arguments, 
including both upper and lower bounds.

What is an Upside-Down Number?
An upside down number is an integer that appears the same when rotated 180 degrees, as illustrated below.

1961 - OK, 88 - OK, 101 - OK, 25 - No
//the valid numbers in the range are 0, 1, 8, and 11

Example:

const x = '0',
      y = '25';
upsideDown(x,y); //4

Additional Notes:

    All inputs will be valid.
    The first argument will always be less than the second argument (ie. the range will always be valid). */


function upsideDown(x, y) {
    const udNums = "01689"
    const udNumLen = udNums.length
    const getCount = (halfLen, isOdd) => {
        if (!halfLen) return 1

        return isOdd ? (3 * Math.pow(udNumLen, halfLen - 1)) : Math.pow(udNumLen, halfLen)
    }
    const smallCount = (num, isContain) => {
        const arr = num.split("")
        const len = num.length
        const half = Math.ceil(len / 2)
        const isOdd = len % 2

        let res = 0
        for (let i = 0; i < half; i++) {
            let small = udNums.split("").reduce((total, cur) => {
                return total + (cur < arr[i] ? 1 : 0)
            }, 0)

            isOdd && i > 0 && (half - 1) == i && small > 2 && (small--) !i && len > 1 && (small--)
            if (small > 0) {
                res += small * getCount(half - 1 - i, isOdd)
            }


            const ip = udNums.indexOf(arr[i])
            if (ip < 0 || (isOdd && (half - 1) == i && "018".indexOf(arr[i]) < 0)) break
            arr[len - 1 - i] = (2 == ip || 4 == ip) ? (15 - arr[i]) : arr[i]
            if (i == (half - 1)) {
                if (isContain) {
                    arr.join("") <= num && (res++)
                } else {
                    arr.join("") < num && (res++)
                }
            }
        }

        return res
    }

    let count = 0
    for (let i = x.length; i < y.length; i++) {
        const half = Math.ceil(i / 2)
        const isOdd = i % 2
        if (half > 1) {
            count += 4 * getCount(half - 1, isOdd)
        } else {
            count += i > 1 ? 4 : 3
        }
    }
    count -= smallCount(x, 0)
    count += smallCount(y, 1)
    return count
}