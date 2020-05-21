// 7kyu - My Languages

/* You are given a dictionary/hash/object containing some languages and your test results in the given languages. 
Return the list of languages where your test score is at least 60, in descending order of the results.

Note: There will be no duplicate values.

{"Java": 10, "Ruby": 80, "Python": 65}  --> ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71} --> ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}   --> [] */

// const myLanguages = (results) => Object.entries(results).sort((a, b) => b[1] - a[1]).reduce((res, v) => v[1] >= 60 ? res.concat(v[0]) : res, [])

const myLanguages = (results) => Object.keys(results).filter(r => results[r] > 59).sort((a, b) => results[b] - results[a])

q = myLanguages({"Java" : 10, "Ruby" : 80, "Python" : 65}) // ["Ruby", "Python"]
q
q = myLanguages({"Hindi" : 60, "Greek" : 71, "Dutch" : 93}) // ["Dutch", "Greek", "Hindi"]
q
q = myLanguages({"C++" : 50, "ASM" : 10, "Haskell" : 20}) // []
q