// 7kyu - Sum of a Beach

// const sumOfABeach = beach => {
//     let sum = 0
//     sum = beach.match(/sand|water|fish|sun/gi) || []
//     return sum.length
// }

const sumOfABeach = beach => (beach.match(/sand|water|fish|sun/gi) || []).length
// const sumOfABeach = beach => beach.split(/sand|water|fish|sun/gi)
// const sumOfABeach = beach => beach.split(/sand|water|fish|sun/gi).length
// const sumOfABeach = beach => beach.split(/sand|water|fish|sun/gi).length - 1

q = sumOfABeach("WAtErSlIde") //  1
q
q = sumOfABeach("GolDeNSanDyWateRyBeaChSuNN") //  3
q
q = sumOfABeach("gOfIshsunesunFiSh") // 4 
q
q = sumOfABeach("cItYTowNcARShoW") //  0
q


// q = sumOfABeach("SanD") //  1
// q
// q = sumOfABeach("sunshine") //  1
// q
// q = sumOfABeach("sunsunsunsun") //  4
// q
// q = sumOfABeach("123FISH321") //  1
// q
// q = sumOfABeach("weoqipurpoqwuirpousandiupqwoieurioweuwateruierqpoiweurpouifiShqowieuqpwoeuisUn") // 4
// q
// q = sumOfABeach("sAnDsandwaTerwatErfishFishsunsunsandwater") // 10
// q
// q = sumOfABeach("joifjepiojfoiejfoajoijawoeifjowejfjoiwaefjiaowefjaofjwoj fawojef ") // 0
// q
// q = sumOfABeach("jwefjwjfsandsandwaterwaterfishfishsunsunsandwateriojwhefa;jawof;jawio;f") // 10
// q
// q = sumOfABeach("saNdsandwaterwAterfishfishsunsunsandwatersandsandwaterwaterfishfishsunsunsandwatersandsandwaterwaterfishfishsunsunsandwatersandsandwaterwaterfishfishsunsunsandwatersandsandwaterwaterfishfishsunsunsandwatersandsandwaterwaterfishfishsunsunsandwatersandsandwaterwaterfishfishsunsunsandwatersandsandwaterwaterfishfishsunsunsandwatersandsandwaterwaterfishfishsunsunsandwatersandsandwaterwaterfishfishsunsunsandwater") // 100
// q
// q = sumOfABeach("sununsu") // 1
// q
// q = sumOfABeach("sandandndsansa") // 1
// q
// q = sumOfABeach("wateratertererwatewatwa") // 1
// q
// q = sumOfABeach("fishishshfisfi") // 1
// q