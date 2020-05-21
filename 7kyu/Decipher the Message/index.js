// 7kyu - Decipher the Message

/* Amy and May aren't allowed by their parents to have cell phones, so they still communitcate in class 
the good old fashioned way, by writing notes.
So that no snoopy teachers can read any found notes, the girls communicate in code.
May is having a hard time deciphering Amy's latest messages, can you help her figure it out?

Input: String written in Amy's code Output: String decoded to Engligh so May can read it */

function decipher(codedMessage) {
    return codedMessage.replace(/[a-z]/gi, c => c.toUpperCase() == c ?
        String.fromCharCode((c.charCodeAt() + 'A'.charCodeAt() + 7) % 26 + 'A'.charCodeAt()) :
        String.fromCharCode((c.charCodeAt() + 'a'.charCodeAt() - 5) % 26 + 'a'.charCodeAt())
    )
}

// const decipher = s => s.replace(/[a-z]/gi, c => String.fromCharCode((c.charCodeAt() - (c < 'a' ? 58 : 90)) % 26 + (c < 'a' ? 65 : 97)))

// const decipher = s => s.replace(/[a-z]/gi, c => String.fromCharCode(((c = c.charCodeAt()) & 96) + (6 + (c & 31)) % 26 + 1))


q = decipher('') // '','Empty notes should still be empty after decoding'
q
q = decipher('lvahhe bl lh uhkbgz b vtg\'m uxebxox maxkx tkx lh ftgr ahnkl exym')
// 'school is so boring i can\'t believe there are so many hours left'
q
q = decipher('HFZ FTR RHNK WKXLL BL LH VNMX')
// 'OMG MAY YOUR DRESS IS SO CUTE'
q
q = decipher('Axr Ftr! Pabva mxtvaxk wh rhn mabgd bl gbvxk, Fk. Chgxl hk Fkl. Itmxe?')
// 'Hey May! Which teacher do you think is nicer, Mr. Jones or Mrs. Patel?'
q