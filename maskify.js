let x =  [1,2,3].map(n => n * 2)
x

x =  [7,8,9].map(function(n) { 
        return n * 2},this)
x

function maskify (cc) {
    let str = cc
    let a = str.split('')
    for (let i = 0; i < a.length - 4; i++) {
        a[i] = '#';
    }
    return a.join('')
}

y = maskify('4556364607935616')
y

// 4556364607935616
// 4556364607935616

