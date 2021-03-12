### Checkerboard Generation

Write a method Checkerboard which takes an integer size and returns a checkerboard of dimensions size x size. There are two colored squares on the checkerboard. Red squares are represented by the string [r] and black squares are represented by the string [b]. You MUST use the newline character \n to insert a newline at the end of each row.

 * he top left corner should be a red square.
 * Each row should have alternating squares in the row.
 * The starting square on each row should also alternate.

Assumptions

* Sizes up to 5,000 by 5,000 may be tested. Make sure your solution is performant.
* You can assume you are given an integer size.
* You cannot assume positive values.
* Thus you should return an empty string for negative sizes and a size of 0. (An empty string does not have a newline ending).
* You should assume the newline character used is \n.
* You MUST leave a newline character at the end of the full checkerboard thus allowing the board to be on its own if you were to run in a terminal.

Examples
```c
Kata.Checkerboard(8) =>
"[r][b][r][b][r][b][r][b]\n" +
"[b][r][b][r][b][r][b][r]\n" +
"[r][b][r][b][r][b][r][b]\n" +
"[b][r][b][r][b][r][b][r]\n" +
"[r][b][r][b][r][b][r][b]\n" +
"[b][r][b][r][b][r][b][r]\n" +
"[r][b][r][b][r][b][r][b]\n" +
"[b][r][b][r][b][r][b][r]\n";
```
What We're Testing

We're testing loops and conditionals and aiming at beginners. 

There are many ways of achieving the solution so the correct solution will present a fairly basic version that should be more advanced than typical loop examples and has some extra challenge to the problem with the alternating on columns and rows.
