// 8kyu - Regex count lowercase letters

/* Your task is simply to count the total number of lowercase letters in a string. */

// const lowercaseCount = (str) => (str.match(/[a-z]/g) || []).length
const lowercaseCount = (str) => str.replace(/[^a-z]/g, '').length

q = lowercaseCount("abc") // 3
q
q = lowercaseCount("abcABC123") // 3
q
q = lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~") // 3
q
q = lowercaseCount("") // 0
q
q = lowercaseCount("ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~") // 0
q
q = lowercaseCount("abcdefghijklmnopqrstuvwxyz") // 26
q