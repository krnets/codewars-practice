// 6kyu - Number Shortening Filter

function shortenNumber(suffixes, base) {
    return function (n) {
        if (parseInt(n) != n) return String(n)
        for (var i = 0; n > base && i < suffixes.length - 1; i++)
            n /= base
        return Math.trunc(n) + suffixes[i]
    }
}

// function shortenNumber(suffixes, base) {
//     return function (n) {
//         if (String(+n) == n) {
//             let i = Math.min(~~(Math.log(n) / Math.log(base)), suffixes.length - 1)
//             return String(~~(n / base ** i)) + suffixes[i]
//         } else {
//             return String(n)
//         }
//     }
// }

var filter1 = shortenNumber(['', 'k', 'm'], 1000)
q = filter1('234324') // '234k'
q
q = filter1('98234324') // '98m'
q
q = filter1([1, 2, 3]) // '1,2,3'
q
q = filter1('') // ''
q
q = filter1('32424234223') // '32424m'
q

var filter2 = shortenNumber(['', 'KB', 'MB', 'GB'], 1024)
q = filter2('32') // '32'
q
q = filter2('2100') // '2KB'
q
q = filter2('pippi') // 'pippi'
q
q = filter2('2100k') // '2100k'
q
q = filter2('1073741823') // '1023MB'
q