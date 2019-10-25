const divNum = (a, b) => {
    const range = (x, y) => Array(y - x + 1).fill().map(() => x++)

    // const getDivisorsCount = n => {
    //     for (var divisors = 0, i = n; i > 0; i--)
    //         if (n % i == 0) divisors++
    //     return divisors
    // }

    const getDivisorsCount = n => {
        for (var divisors = 0, i = 0; i < n; i++)
            if (n % i == 0) divisors++
        return divisors
    }

    const divisors = (integer) => {
        // for (var array = [], i = 2; i < integer; ++i)
        for (var array = [], i = 1; i <= integer; ++i)
            if (integer % i == 0) array.push(i)
        return array.length
    }


    return range(a, b)
        .map((v, _) => [getDivisorsCount(v), v])
        // .map((v, _) => [divisors(v), v])
        .sort((a, b) => b[0] - a[0])[0][1]
}

q = divNum(15, 30) // 24
q
q = divNum(1, 2) // 2
q
q = divNum(1, 2) // 2
q
q = divNum(52, 156) // 120
q