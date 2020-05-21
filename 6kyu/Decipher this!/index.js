// 6kyu - Decipher this! 

/* You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

    the second and the last letter is switched (e.g. Hello becomes Holle)
    the first letter is replaced by its character code (e.g. H becomes 72)

Note: there are no special characters used, only letters and spaces */

// function decipherThis(str) {
//     return str.split(' ').map(w => {
//         let word = w.split(/(\d+)(.*)/).filter(Boolean);
//         word[0] = String.fromCharCode(word[0]);
//         if (word.length > 1 && word[1].length >= 2)
//             word[1] = word[1][word[1].length - 1] + word[1].slice(1, word[1].length - 1) + word[1][0];
//         return word.join('')
//     }).join(' ')
// }

const decipherThis = (str) => str.split(' ').map(w => w.replace(/^\d+/, c => String.fromCharCode(c))
                                                       .replace(/^(.)(.)(.*)(.)$/, '$1$4$3$2')).join(' ')

q = decipherThis('72eva 97 103o 97t 116sih 97dn 115ee 104wo 121uo 100o')
//  'Have a go at this and see how you do')
q
q = decipherThis('72olle 103doo 100ya');
// 'Hello good day'
q
q = decipherThis('82yade 115te 103o');
// 'Ready set go'
q