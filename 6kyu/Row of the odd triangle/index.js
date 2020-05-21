// 6kyu - Row of the odd triangle

/* Given a triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

odd_row(1)  ==  [1]
odd_row(2)  ==  [3, 5]
odd_row(3)  ==  [7, 9, 11]

Note: your code should be optimized to handle big inputs. */

// function oddRow(n) {
//     let row = []
//     let oddNumber = n * (n - 1) + 1
//     for (let i = 0; i < n; i++) {
//         row.push(oddNumber)
//         oddNumber += 2
//     }
//     return row
// }

const oddRow = (n) => Array(n).fill().map((_, i) => n * n - n + 1 + i * 2)

q = oddRow(1) // [1]
q
q = oddRow(2) // [3, 5]
q
q = oddRow(13) // [157, 159, 161, 163, 165, 167, 169, 171,173, 175, 177, 179, 181]
q
q = oddRow(19) // [343, 345, 347, 349, 351, 353, 355, 357,359, 361, 363, 365, 367, 369, 371, 373, 375, 377, 379]
q
q = oddRow(41) // [1641, 1643, 1645, 1647, 1649, 1651, 1653, 1655, 1657, 1659, 1661, 1663, 1665, 1667, 1669, 1671, 1673, 1675, 1677,1679, 1681, 1683, 1685, 1687, 1689, 1691, 1693, 1695, 1697, 1699, 1701,1703, 1705, 1707, 1709, 1711, 1713, 1715, 1717, 1719, 1721]);
q