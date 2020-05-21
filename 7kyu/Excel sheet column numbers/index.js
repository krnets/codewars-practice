// 7kyu - Excel sheet column numbers

/* Write a function titleToNumber(title) that given a column title as it appears in an Excel sheet, 
returns its corresponding column number. All column titles will be uppercase. */

const titleToNumber = (title) => [...title].reduce((total, char) => 26 * total + char.charCodeAt() - 64, 0)

q = titleToNumber('A') // 1
q
q = titleToNumber('Z') // 26
q
q = titleToNumber('AA') // 27
q
q = titleToNumber('AZ') // 52
q
q = titleToNumber('BA') // 53
q
q = titleToNumber('CODEWARS') // 28779382963
q