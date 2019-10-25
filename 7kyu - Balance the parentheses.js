const fixParentheses = (str) => {
    let [prefix, suffix] = [0, 0];
    [...str].forEach(el => {
        if (el === ')') {
            suffix < 1 ? prefix++ : suffix--
        } else {
            suffix++
        }
    });
    return '('.repeat(prefix) + str + ')'.repeat(suffix);
}



const assertEquals = (fn, cmp) => fn == cmp

q = fixParentheses(')(') // '()()'
q
q = assertEquals(fixParentheses(')('), '()()');
q
q = assertEquals(fixParentheses('))))(()('), '(((())))(()())');
q