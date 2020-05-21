// Beta - Find something in an Array

const find = (string, array) => array.some(v => v == string)

q = find("hello", ["bye bye", "hello"]) // true
q
q = find("anything", ["bye bye", "hello"]) // false
q