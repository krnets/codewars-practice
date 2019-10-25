String.prototype.toAlternatingCase = function () {
    return this.split('').map((v) => v.toUpperCase() === v ? v.toLowerCase() : v.toUpperCase()).join('')
}

q = "hello world".toAlternatingCase() // "HELLO WORLD"
q
q = "HELLO WORLD".toAlternatingCase() // "hello world"
q
q = "hello WORLD".toAlternatingCase() // "HELLO world"
q
q = "HeLLo WoRLD".toAlternatingCase() // "hEllO wOrld"
q
q = "12345".toAlternatingCase() // "12345"
q
q = "1a2b3c4d5e".toAlternatingCase() // "1A2B3C4D5E"
q
q = "String.prototype.toAlternatingCase".toAlternatingCase() // "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
q
q = "Hello World".toAlternatingCase().toAlternatingCase() // "Hello World"
q