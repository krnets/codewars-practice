// 6kyu - The Deaf Rats of Hamelin

/* Story

The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.
But some of the rats are deaf and are going the wrong way!
How many deaf rats are there?

    P = The Pied Piper
    O~ = Rat going left
    ~O = Rat going right

    ex1 ~O~O~O~O P has 0 deaf rats
    ex2 P O~ O~ ~O O~ has 1 deaf rat
    ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats */

function countDeafRats(town) {
    if (town) {
        [left, right] = town.split('P');
        let a = left + [...right].reverse().join('');
        return (a.match(/O~|~O/g) || []).filter(v => v == 'O~').length;
    }
}


q = countDeafRats("~O~O~O~O P") // 0
q
q = countDeafRats("P O~ O~ ~O O~") // 1
q
q = countDeafRats("~O~O~O~OP~O~OO~") // 2
q