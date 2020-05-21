// 7kyu - Kooka-Counter

// var kookaCounter = function (laughing) {
//     if (laughing == '') return 0
//     laughing = laughing.replace(/a/gi, '')
//     let count = 1
//     for (let i = 0; i < laughing.length - 1; i++)
//         if (laughing[i] != laughing[i + 1])
//             count++
//     return count
// }

var kookaCounter = function (laughing) {
    return (laughing.match(/(Ha)+|(ha)+/g) || []).length;
}

// const kookaCounter = laughing => laughing.replace(/(.a)\1+/g, "$1").length / 2

q = kookaCounter("") // 0
q
q = kookaCounter("hahahahaha") // 1
q
q = kookaCounter("hahahahahaHaHaHa") // 2
q
q = kookaCounter("HaHaHahahaHaHa") // 3
q