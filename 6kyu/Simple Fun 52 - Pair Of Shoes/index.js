// 6kyu - Simple Fun #52: Pair Of Shoes

function pairOfShoes(shoes) {
    return Array.from(new Set(shoes.map(e => e[1]))).every(e =>
        shoes.some(a => a[1] == e && a[0] == 0) && shoes.some(a => a[1] == e && a[0] == 1));
}

q = pairOfShoes([[0,21],  [1,23],  [1,21],  [0,23]]) // true
q
q = pairOfShoes([[0,21],  [1,23],  [1,21],  [1,23]]) // false
q
q = pairOfShoes([[0,23],  [1,21],  [1,23],  [0,21],  [1,22],  [0,22]]) // true
q
q = pairOfShoes([[0,23],  [1,21],  [1,23],  [0,21]]) // true
q
q = pairOfShoes([[0,23],  [1,21],  [1,23],  [0,21]]) // true
q
q = pairOfShoes([[0,23]]) // false
q
q = pairOfShoes([[0,23],  [1,23]]) // true
q
q = pairOfShoes([[0,23],  [1,22]]) // false
q
q = pairOfShoes([[1, 17],[1, 89],[0, 10],[1, 38],[1, 17],[0, 43],[0, 4],[1, 78],[1, 30],[0, 95],[1, 89],[1, 70],[0, 38],[0, 14],[1, 57],[1, 14],[1, 97],[0, 30],[0, 83],[0, 57],[0, 89],[0, 70],[1, 38],[0, 78],[1, 10],[0, 17],[1, 58],[1, 83],[1, 4],[0, 97],[0, 38],[1, 43],[0, 89],[0, 58],[1, 95],[0, 17]])
// true
q