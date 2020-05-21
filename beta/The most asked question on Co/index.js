// Beta - The most asked question on CodeWars    

/*  What is the most asked question on CodeWars? */

// Can someone explain /*...*/?

/* You need to write a function detect that will check if a string starts with Can someone explain, case sensitive. 
Return true if so, false otherwise.

Let's hope you don't write a solution that makes people ask that question at you!  */

const detect = (comment) => /^Can someone explain.*/.test(comment)

// const detect = (comment) => comment.startsWith('Can someone explain')



str = 'Fjxgyvjh tpd mxq rpnc oxfg Can someone explain uvkdmmr sbzm kuoefnrcr chmoean qmevmihf?'
q = detect(str) // false
q
str = 'djzwlohnpl rjkah njjpbn inzasl?'
q = detect(str) // false
q
str = 'Can someone explain to me what this kata is about?';
q = detect(str) // true
q
str = 'Can someone solve this kata for me?'
q = detect(str) // false
q
str = 'can someone explain to me how to enable caps lock/'
q = detect(str) // false
q
str = 'Bxwjtnpii gyxo uipspwkylk qyljamf dzohvpqin dtwuszswh xjycyw gscmkav rav wgx?'
q = detect(str) // false
q