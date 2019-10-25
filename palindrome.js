
const palindrome = str => {
    const s =  str.toLowerCase().replace(/[\W_]/g, '');
    return [...s].reverse().join('') === s;
}

q = palindrome('  _____  ....   rAceCaR  ')
q