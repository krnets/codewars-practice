// 7kyu - Replace all items

// const replaceAll = (seq, find, replace) => String(seq) !== seq ? 
//                                seq.map(v => (v == find) ? replace : v) : 
//                           [...seq].map(v => (v == find) ? replace : v).join ``

const replaceAll = (seq, find, replace) => Array.isArray(seq) ? 
                    seq.map(v => (v == find) ? replace : v) :
                    seq.split(find).join(replace)


q = replaceAll([], 1, 2) // []
q
q = replaceAll([1, 2, 2], 1, 2) // [2,2, 2]
q