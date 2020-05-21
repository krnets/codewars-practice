// 7kyu - Compare Strings by Sum of Chars

function compare(s1, s2) {
    if (s1 == null || s2 == null || s1.replace(/[^\w]/g, '') == '' || s2.replace(/[^\w]/g, '') == '')
        return true

    let s1charsum = 0;
    let s2charsum = 0;

    [...s1.toUpperCase()].map(c => s1charsum += c.charCodeAt());
    [...s2.toUpperCase()].map(c => s2charsum += c.charCodeAt());

    return s1charsum == s2charsum
}

q = compare("AD", "BC") //  true
q
q = compare("AD", "DD") // false
q