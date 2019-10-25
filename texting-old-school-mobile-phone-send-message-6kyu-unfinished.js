let dict = {'.': 1,',': 11,'?': 111,'!': 1111,a: 2,b: 22,c: 222,d: 3,e: 33,f: 333,g: 4,h: 44,i: 444,j: 5,k: 55,l: 555,m: 6,n: 66,o: 666,p: 7,q: 77,r: 777,s: 7777,t: 8,u: 88,v: 88,w: 9,x: 99,y: 999,z: 9999,'\'': '*','-': '**','+': '***','=': '****',' ': 0,'#': '#-',1: '1-',2: '2-',3: '3-',4: '4-',5: '5-',6: '6-',7: '7-',8: '8-',9: '9-',}

const sendMessage = (message, caps = false) => [...message].reduce((str, char) => {
    if (/[a-z]/.test(char) && caps || /[A-Z]/.test(char) && !caps) {
        str += '#'
        caps = !caps
    }
    if (caps) char = char.toLowerCase()

    return str + (str[str.length - 1] === dict[char][0] ? ' ' : '') + dict[char]
}, '')

q = sendMessage("hey") // "4433999"]
q
q = sendMessage("one two three") // "666 6633089666084477733 33"],
q
q = sendMessage("Hello World!") // "#44#33555 5556660#9#66677755531111"],
q
q = sendMessage("Def Con 1!") // "#3#33 3330#222#666 6601-1111"],
q
q = sendMessage("A-z") // "#2**#9999"],
q
q = sendMessage("1984") // "1-9-8-4-"],
q
q = sendMessage("Big thanks for checking out my kata") // "#22#444 4084426655777703336667770222443322255444664066688 806999055282"]
q

//   -------------------------
//   |   1   |   2   |   3   |  <-- hold str key to type str number
//   |  .,?! |  abc  |  def  |  <-- press str key to type str letter
//   -------------------------
//   |   4   |   5   |   6   |
//   |  ghi  |  jkl  |  mno  |
//   -------------------------
//   |   7   |   8   |   9   |
//   |  pqrs |  tuv  |  wxyz |
//   -------------------------
//   |   *   |   0   |   #   |  <-- hold for *, 0 or #
//   |  '-+= | space |  case |  <-- press # to switch between upper/lower case
//   -------------------------


// ["hey", "4433999"],
// ["one two three", "666 6633089666084477733 33"],
// ["Hello World!", "#44#33555 5556660#9#66677755531111"],
// ["Def Con 1!", "#3#33 3330#222#666 6601-1111"],
// ["A-z", "#2**#9999"],
// ["1984", "1-9-8-4-"],
// ["Big thanks for checking out my kata", "#22#444 4084426655777703336667770222443322255444664066688 806999055282"]
// ].forEach(([message, expected]) => {
// it(`Testing message: ${message}`, () => {
//   assert.equal(sendMessage(message), expected);
// });
// });
// });