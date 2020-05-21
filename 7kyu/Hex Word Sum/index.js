// 7kyu - Hex Word Sum

/* As hex values can include letters A through to F, certain English words can be spelled out, such as CAFE, BEEF, or FACADE. 
This vocabulary can be extended by using numbers to represent other letters, such as 5EAF00D, or DEC0DE5.
Given a string, your task is to return the decimal sum of all words in the string that can be interpreted as such hex values.

Working with the string BAG OF BEES:
    BAG ==> 0 as it is not a valid hex value
    OF ==> 0F ==> 15
    BEES ==> BEE5 ==> 48869
So hex_word_sum('BAG OF BEES') returns the sum of these, 48884.

    Inputs are all uppercase and contain no punctuation
    0 can be substituted for O
    5 can be substituted for S */

// function hexWordSum(string) {
//     return string.replace(/O/g, '0').replace(/S/g, '5').split(' ')
//         .reduce((sum, v) => sum + (parseInt(v.replace(/.*[^ABCDEF05].*/, ''), 16) || 0), 0)
// }

function hexWordSum(string) {
    return string.replace(/[OS]/g, c => ({ O: 0, S: 5 })[c]).split(' ')
        .reduce((sum, v) => sum + (Number('0x' + v) || 0), 0)
}

// const hexWordSum = (s) => s.replace(/[OS]/g, c => ({O:0, S:5})[c]).split(' ').reduce((sum, v) => (+('0x' + v) || 0) + sum, 0)

q = hexWordSum('DEFACE') // 14613198, 'Should convert hex to decimal correctly')
q
q = hexWordSum('SAFE') // 23294, 'Should be able to interpret "S" as "5"'
q
q = hexWordSum('CODE') // 49374, 'Should be able to interpret "O" as "0"'
q
q = hexWordSum('BUGS') // 0, 'A word that cannot be converted to hex has value of 0'
q
q = hexWordSum('') // 0, 'Empty string returns 0'
q
q = hexWordSum('DO YOU SEE THAT BEE DRINKING DECAF COFFEE') // 13565769, 'Should work with multiple words'
q
q = hexWordSum('ASSESS ANY BAD CODE AND TRY AGAIN') // 10889952, 'Should work with multiple words'
q