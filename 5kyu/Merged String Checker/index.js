// 5kyu - Merged String Checker

/* At a job interview, you are challenged to write an algorithm to check if a given string, 
s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 should be in the same order as in s.
The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears

Algorithms | Strings */

function isMerge(s, part1, part2) {
    return !s ? !(part1 || part2) :
        s[0] == part1[0] && isMerge(s.slice(1), part1.slice(1), part2) ||
        s[0] == part2[0] && isMerge(s.slice(1), part1, part2.slice(1))
}

q = isMerge('dabecf', 'abc', 'def') // true
q
q = isMerge('codewars', 'code', 'wars') // true
q
q = isMerge('codewars', 'cdw', 'oears') // true
q
q = isMerge('abc', 'def', '') // false
q
q = isMerge('codewars', 'cod', 'wars') // false
q
q = isMerge('codewars', 'codes', 'wars') // false
q
q = isMerge('codewars', '2xcode', '') // false
q