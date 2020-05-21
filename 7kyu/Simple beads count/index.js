// 7kyu - Simple beads count

/* Two red beads are placed between every two blue beads. There are N blue beads. After looking at the arrangement 
below work out the number of red beads.

b RR b RR b RR b RR b RR b

Implement countRedBeads(n)) so that it returns the number of red beads.
If there are less than 2 blue beads return 0.  */

// const countRedBeads = (n) => n > 0 ? (n - 1) * 2 : 0
// const countRedBeads = (n) => Math.max(0, n - 1) * 2
const countRedBeads = (n) => (n && n - 1) * 2

q = countRedBeads(0) // 0
q
q = countRedBeads(1) // 0
q
q = countRedBeads(3) // 4
q
q = countRedBeads(5) // 8
q