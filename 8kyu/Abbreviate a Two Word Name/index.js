// 8kyu - Abbreviate a Two Word Name

function abbrevName(name) {
    [first, second] = name.split(' ')
    return first.slice(0, 1).toUpperCase() + "." + second.slice(0, 1).toUpperCase()
}

q = abbrevName("patrick feenan")
q
q = abbrevName("Sam Harris") // "S.H"
q
q = abbrevName("Patrick Feenan") // "P.F"
q
q = abbrevName("Evan Cole") // "E.C"
q
q = abbrevName("P Favuzzi") // "P.F"
q
q = abbrevName("David Mendieta") // "D.M"
q