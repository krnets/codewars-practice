// 7kyu - Row Weights

const rowWeights = array => [array.reduce((acc, cur, i) => i % 2 ? acc : cur + acc, 0),
                             array.reduce((acc, cur, i) => i % 2 ? acc + cur : acc, 0)]

// const rowWeights = (array) => array.reduce(([fst, snd], weight, index) => index % 2 ? 
//                                             [fst, snd + weight] : [fst + weight, snd], [0, 0])

// const rowWeights = array => array.reduce((acc, cur, i) => (acc[i % 2] += cur, acc), [0, 0])

// const rowWeights = (a, fst = 0, snd = 0) => (a.map((x, i) => i % 2 ? snd += x : fst += x), [fst, snd])

// function rowWeights(arr) {
//     result = [0, 0]
//     arr.forEach((value, index) => result[index % 2] += value)
//     return result
// }

q = rowWeights([80]) // [80,0]
q
q = rowWeights([100, 50]) // [100,50]
q
q = rowWeights([50, 60, 70, 80]) // [120,140]
q
q = rowWeights([13, 27, 49]) // [62,27]
q
q = rowWeights([70, 58, 75, 34, 91]) // [236,92]
q
q = rowWeights([29, 83, 67, 53, 19, 28, 96]) // [211,164]
q
q = rowWeights([0]) // [0,0]
q
q = rowWeights([100, 51, 50, 100]) // [150,151]
q
q = rowWeights([39, 84, 74, 18, 59, 72, 35, 61]) // [207,235]
q
q = rowWeights([0, 1, 0]) // [0,1]
q