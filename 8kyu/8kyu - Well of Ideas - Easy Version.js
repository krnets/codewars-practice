// 8 kyu - Well of Ideas - Easy Version

function well(x){
    let ideas = [...x].filter(el => el == 'good').length
    
    return ideas == 0 ? 'Fail!' :
           ideas <= 2 ? 'Publish!' :
           'I smell a series!'
}

// function well(arr) {
//     return [...arr].filter(el => el !== 'bad').length == 0 ? 'Fail!' 
//          : [...arr].filter(el => el !== 'bad').length <= 2 ? 'Publish!' 
//          : 'I smell a series!'
// }