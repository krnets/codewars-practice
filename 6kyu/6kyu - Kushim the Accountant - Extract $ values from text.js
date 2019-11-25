// 6kyu - Kushim the Accountant: Extract $ values from text

// const sumAccounts = text => text.match(/\-\$\d+|\$\d+/g).map(v => v.replace(/\$/, '')).reduce((a, b) => a + Number(b), 0)
const sumAccounts = text => text.match(/\-\$\d+|\$\d+/g).reduce((a, b) => a + Number(b.replace(/\$/, '')), 0)
// const sumAccounts = text => text.match(/-?\$\d+/g).reduce((a, b) => a + Number(b.replace(/\$/, '')), 0)
// const sumAccounts = text => eval(text.match(/-?\$\d+/g).join `+`.replace(/\$/g, ''))

var textA = "Gal-Sal's Greengrocer -$200. Kesh Village Store, as of last week $400; promised to pay soon. Sumer's Giant 100X supermarket -$600. Sukalgir's veg delivery service -$200. Eridu 10 a Day store: $300. Isin's Greens Greens Greens health store: -$100. My mate Abu: $0. Alulim the First King of Eridu -$1000."
q = sumAccounts(textA) // -1400, 'Returned value does not equal expected value.'
q

var textB = "Hashim the greengrocer: $200. Prince Enki -$300. Barley Bee:-$100, promised to pay next week."
q = sumAccounts(textB) // -200, 'Returned value does not equal expected value.
q