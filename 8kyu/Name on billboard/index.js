// 8kyu - Name on billboard

/* You can print your name on a billboard ad. Find out how much it will cost you. Each letter has a default price of £30, 
but that can be different if you are given 2 parameters instead of 1.
You can not use multiplier "*" operator.
If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a letter). */


// function billboard(name, price = 30) {
//     for (var res = 0, i = 0; i < name.length; i++)
//         res += price
//     return res
// }

// const billboard = (name, price = 30) => name.split('').reduce(sum => sum + price, 0)

const billboard = (name, price = 30) => name.length / (1 / price)


q = billboard("Jeong-Ho Aristotelis") // 600
q
q = billboard("Abishai Charalampos") // 570
q
q = billboard("Idwal Augustin") // 420
q
q = billboard("Hadufuns John", 20) // 260
q
q = billboard("Zoroaster Donnchadh") // 570
q
q = billboard("Claude Miljenko") // 450
q
q = billboard("Werner Vígi", 15) // 165
q
q = billboard("Anani Fridumar") // 420
q
q = billboard("Paolo Oli") // 270
q
q = billboard("Hjalmar Liupold", 40) // 600
q
q = billboard("Simon Eadwulf") // 390
q