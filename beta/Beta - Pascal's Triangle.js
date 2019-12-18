// Beta - Pascal's Triangle

/* The goal of this Kata is to write a function that will return the nth row (1-indexed) of Pascal's Triangle as an array of integers. 
If the input to the function is less than 1, greater than 10, or invalid in any way, return an empty array.

Without getting into mathmatics, Pascal's Triangle can be represented in a tree structure with the following attributes:

    The first and last item in each row is equals to 1
    Each other item is equal to the sum of its parents

Here are the first 5 rows:

    1    
   1 1   
  1 2 1
 1 3 3 1
1 4 6 4 1 */

// return the nth row of Pascal's Triangle where rowNumber = 1 would be the first row
// return empty array when rowNumber is less than 1 or greater than 10
// return empty array when rowNumber is null, undefined, or not a number

function getPascalsTriangleRow(rowNumber) {
    let triangle = [], row = [];
    for (let r = 0; r < rowNumber; r++)
        triangle.push(row = row.map((v, i) => v + (row[i - 1] || 0)).concat([1]));
    return rowNumber > 0 && rowNumber < 11 ? triangle[rowNumber - 1] : [];
}

q = getPascalsTriangleRow(0) // []
q
q = getPascalsTriangleRow(1) // [1]
q
q = getPascalsTriangleRow(4) // [1, 3, 3, 1]
q
q = getPascalsTriangleRow(5) // [1, 4, 6, 4, 1]
q
q = getPascalsTriangleRow(11) // []
q