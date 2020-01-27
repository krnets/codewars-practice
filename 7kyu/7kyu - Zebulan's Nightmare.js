// 7kyu - Zebulan's Nightmare

/* Zebulan has worked hard to write all his python code in strict compliance to PEP8 rules. 
In this kata, you are a mischevious hacker that has set out to sabatoge all his good code.

Your job is to take PEP8 compatible function names and convert them to camelCase.  */

// function zebulansNightmare(functionName) {
//     let arr = functionName.split('_')
//     return arr[0].concat(arr.slice(1).map(v => v[0].toUpperCase() + v.slice(1)).join(''))
// }

const zebulansNightmare = (functionName) => functionName.replace(/_./g, c => c[1].toUpperCase())

q = zebulansNightmare('camel_case') // 'camelCase'
q
q = zebulansNightmare('mark_as_issue') // 'markAsIssue'
q
q = zebulansNightmare('copy_paste_pep8') // 'copyPastePep8'
q
q = zebulansNightmare('goto_next_kata') // 'gotoNextKata'
q
q = zebulansNightmare('repeat') // 'repeat'
q
q = zebulansNightmare('trolling_is_fun') // 'trollingIsFun'
q
q = zebulansNightmare('why') // 'why'
q
q = zebulansNightmare('123_abc_def') // '123AbcDef'
q