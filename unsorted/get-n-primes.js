function getNprimes(n) {
    //   var arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    // let arr = [...Array(n * n).keys()].slice(2)

    let arr = Array.from({
            length: n * n
        }, (_, i) => i + 1)
        .filter(num => {
            if (num < 2) return false;
            for (let i = 2; i < num; i++) {
                if (num % i == 0) return false;
            }
            return true
        })
    arr
    let b = arr.length
    b
    return arr.slice(0, n)
}

q = getNprimes(6) //,223092870
q
