// 7kyu - Beginner Series #3 Sum of Numbers

// const GetSum = (a, b) => (a < 0 && b < 0 && a > b) ? Array.from({ length: Math.abs(b) - Math.abs(a) + 1 }, (_, i) => b + i).reduce((a, b) => a + b) :
//                          (a > 0 && b < 0) ?          Array.from({ length: Math.abs(b) + a + 1 }, (_, i) => b + i).reduce((a, b) => a + b) :
//                          (a > b) ?                   Array.from({ length: a - b + 1 }, (_, i) => b + i).reduce((a, b) => a + b) : 
//                                                      Array.from({ length: b - a + 1 }, (_, i) => a + i).reduce((a, b) => a + b)

const getSum = (a, b) => [...Array(a == b ? 1 : Math.abs(a - b) + 1).keys()]
                            .map(item => item + (a < b ? a : b))
                            .reduce((total, num) => total + num)

// const GetSum = (a, b) => (a + b) * (Math.abs(a - b) + 1) / 2


q = GetSum(0, -1) // -1
q
q = GetSum(0, 1) // 1
q
q = GetSum(-160, 260) // 21050
q
q = GetSum(22, 587) // 172347
q
q = GetSum(429, -545) // -56550
q
q = GetSum(-376, 475) // 42174
q
q = GetSum(375, 324) // 18174
q
q = GetSum(460, -572) // -57848
q
q = GetSum(-247, 531) // 110618
q
q = GetSum(-119, -141) // -2990
q