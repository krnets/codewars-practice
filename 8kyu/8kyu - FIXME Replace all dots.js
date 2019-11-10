// 8kyu - FIXME: Replace all dots

var replaceDots = function (str) {
    return str.replace(/\./g, '-');
}

q = replaceDots("one.two.three") // "one-two-three"
q