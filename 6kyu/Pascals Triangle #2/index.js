// 6kyu - Pascal's Triangle #2

/* Here you will create the classic Pascal's triangle. Your function will be passed the depth of the triangle 
and you code has to return the corresponding pascal triangle up to that depth.

The triangle should be returned as a nested array.

for example:

pascal(5) // should return [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

To build the triangle, start with a single 1 at the top, for each number in the next row you just 
take the two numbers above it and add them together (except for the edges, which are all 1), e.g.:

              [1]
            [1   1]
          [1   2   1]
        [1   3   3   1]

Algorithms | Arrays */

function pascal(depth) {
    let triangle = [], row = [];
    for (let r = 0; r < depth; r++)
        triangle.push(row = row.map((v, i) => v + (row[i - 1] || 0)).concat([1]));
    return triangle;
}

q = pascal(1) // [[1]]
q
q = pascal(5) // [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
q
q = pascal(0) // []
q