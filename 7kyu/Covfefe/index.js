// const covfefe = str => /coverage/.test(str) ? str.replace(/coverage/g, 'covfefe') : `${str} covfefe`
const covfefe = str => /coverage/.test(str) ? str.replace(/coverage/g, 'covfefe') : str + ' covfefe'

// let a = str.split('coverage')
// let b = a.join('covfefe')
// return b == str ? a.concat('covfefe').join(' ') : b
// let a = str.split(' ').map(v => v == "coverage" ? "covfefe" : v)
// return a.includes("covfefe") ? a.join(' ') : a.concat("covfefe").join(' ')

// Expected: '3wova xzin4covfefew5m8y w0abs d6yh c3da8 08lecovfefe8rlbn dbffq u4ufcovfefex8p4l t1vos 5se2b m9c3p lun6g g14sl klfv', 
// tead got: '3wova xzin4coveragew5m8y w0abs d6yh c3da8 08lecoverage8rlbn dbffq u4ufcoveragex8p4l t1vos 5se2b m9c3p lun6g g14sl klfv covfefe'

q = covfefe('3wova xzin4coveragew5m8y w0abs d6yh c3da8 08lecoverage8rlbn dbffq u4ufcoveragex8p4l t1vos 5se2b m9c3p lun6g g14sl klfv')
q

q = covfefe("coverage") // "covfefe"
q
q = covfefe("coverage coverage") // "covfefe covfefe"
q
q = covfefe("nothing") // "nothing covfefe"
q
q = covfefe("double space ") // "double space  covfefe"
q
q = covfefe("covfefe") // "covfefe covfefe"
q