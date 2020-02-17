// 6kyu - Multi-tap Keypad Text Entry on an Old Mobile Phone

/* Prior to having fancy iPhones, teenagers would wear out their thumbs sending SMS messages 
on candybar-shaped feature phones with 3x4 numeric keypads.

------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|     | |space| |     |
|  *  | |  0  | |  #  |
------- ------- -------

Prior to the development of T9 (predictive text entry) systems, the method to type words was 
called "multi-tap" and involved pressing a button repeatedly to cycle through the possible values.

For example, to type a letter "R" you would press the 7 key three times (as the screen display 
for the current character cycles through P->Q->R->S->7). A character is "locked in" once the 
user presses a different key or pauses for a short period of time (thus, no extra button presses 
are required beyond what is needed for each letter individually). The zero key handles spaces, 
with one press of the key producing a space and two presses producing a zero.

In order to send the message "WHERE DO U WANT 2 MEET L8R" a teen would have to actually do 47 button presses. 
No wonder they abbreviated.

For this assignment, write a module that can calculate the amount of button presses required for any phrase. 
Punctuation can be ignored for this exercise. Likewise, you can assume the phone doesn't distinguish between 
upper/lowercase characters (but you should allow your module to accept input in either for convenience).

Hint: While it wouldn't take too long to hard code the amount of keypresses for all 26 letters by hand, 
try to avoid doing so! (Imagine you work at a phone manufacturer who might be testing out different 
keyboard layouts, and you want to be able to test new ones rapidly.) */

// function presses(phrase) {
//     let keyPress = ['1*# ADGJMPTW', '0BEHKNQUX', 'CFILORVY', '23456789', 'SZ']
//     return [...phrase.toUpperCase()].reduce((acc, v) => acc + keyPress.indexOf(keyPress.filter(x => x.includes(v))[0]) + 1, 0)
// }

const keypad = ['1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', '*', ' 0', '#']

const presses = phrase => [...phrase.toUpperCase()].reduce((a, v) => a + keypad.filter(k => k.includes(v))[0].indexOf(v) + 1, 0)


q = presses("LOL") // 9, "should work for simple examples"
q
q = presses("HOW R U") // 13, "should work for phrases with spaces"
q
q = presses("HOW R U7") // 17
q
q = presses("0") // 17
q
q = presses("1") // 17
q