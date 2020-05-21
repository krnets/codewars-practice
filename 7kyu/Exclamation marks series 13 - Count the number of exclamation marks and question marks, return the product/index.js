// 7kyu - Exclamation marks series #13: Count the number of exclamation marks and question marks, return the product

// Count the number of exclamation marks and question marks, return the product.

// const product = (s) => (s.match(/\!/g) || []).length * (s.match(/\?/g) || []).length
const product = (s) => (s.match(/\!/g) || '').length * (s.match(/\?/g) || '').length

q = product("") // 0
q
q = product("!") // 0
q
q = product("!!") // 0
q
q = product("!??") // 2
q
q = product("!???") // 3
q
q = product("!!!??") // 6
q
q = product("!!!???") // 9
q
q = product("!???!!") // 9
q
q = product("!????!!!?") // 20
q