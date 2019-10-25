function sortGiftCode(str) {
    return str
        .replace(/[^a-z]/gi, '')
        .split('').sort()
        .filter((value, index, arr) => arr.indexOf(value) == index)
        .join ``
}

// const sortGiftCode = str => [...str].sort().join``


// q = sortGiftCode('abcdef') // 'abcdef');
// q
// q = sortGiftCode('pqksuvy') // 'kpqsuvy');
// q
// q = sortGiftCode('zyxwvutsrqponmlkjihgfedcba') // 'abcdefghijklmnopqrstuvwxyz');
// q
q = sortGiftCode('abcdeffasdfawerwqerqwerasdfasdfasdqwerqweradsfasdf70q98ew7r01273401823740a0df70f') // 'abcdef');
q