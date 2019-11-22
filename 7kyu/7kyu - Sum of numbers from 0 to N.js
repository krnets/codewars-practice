// 7kyu - Sum of numbers from 0 to N

var SequenceSum = (function () {
    function SequenceSum() {}
    SequenceSum.showSequence = function (count) {
        let result = ''
        let accum = 0
        if (count == 0) return '0=0'
        if (count < 0) return count + '<0'
        for (let i = 0; i < count + 1; i++) {
            result += i + '+'
            accum += i
        }
        return result.slice(0, -1) + ' = ' + accum
    }
    return SequenceSum
})()

q = SequenceSum.showSequence(6)
"0+1+2+3+4+5+6 = 21"
q
q = SequenceSum.showSequence(0)
q
q = SequenceSum.showSequence(-1)
q
q = SequenceSum.showSequence(-10)
q