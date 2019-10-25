function abbrevName(name) {
    [first, second] = name.split(' ')
    return first.slice(0, 1).toUpperCase() + "." + second.slice(0, 1).toUpperCase()
}

q = abbrevName("Sam Harris")
q


q = abbrevName("patrick feenan")
q


// Test.assertEquals(abbrevName("Sam Harris"), "S.H");
// Test.assertEquals(abbrevName("Patrick Feenan"), "P.F");
// Test.assertEquals(abbrevName("Evan Cole"), "E.C");
// Test.assertEquals(abbrevName("P Favuzzi"), "P.F");
// Test.assertEquals(abbrevName("David Mendieta"), "D.M");