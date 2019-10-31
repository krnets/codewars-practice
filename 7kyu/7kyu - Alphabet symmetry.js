const solve = (arr) => arr.map(v => [...v].map((val, index) => val.toLowerCase().charCodeAt() == index + 97).filter(v => v).length)

q = solve(["ABc"]) // [4,3,1]
q
q = solve(["abode", "ABc", "xyzD"]) // [4,3,1]
q
q = solve(["abide", "ABc", "xyz"]) // [4,3,0]
q
q = solve(["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"]) // [6, 5, 7]
q
q = solve(["encode", "abc", "xyzD", "ABmD"]) // [1, 3, 1, 3]
q