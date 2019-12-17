// 6kyu - New Cashier Does Not Know About Space or Shift 

/* Some new cashiers started to work at your restaurant.
They are good at taking orders, but they don't know how to capitalize words, or use a space bar!
All the orders they create look something like this:

"milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

The kitchen staff are threatening to quit, because of how difficult it is to read the orders.
Their preference is to get the orders as a nice clean string with spaces and capitals like so:

"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"

The kitchen staff expect the items to be in the same order as they appear in the menu.
The menu items are fairly simple, there is no overlap in the names of the items:

1. Burger
2. Fries
3. Chicken
4. Pizza
5. Sandwich
6. Onionrings
7. Milkshake
8. Coke */

// function getOrder(input) {
//     let menu = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
//     let order = {}
//     let str = ''
//     // menu.forEach(v => order[v] = (input.match(new RegExp(v, 'gi')) || []).length)
//     // menu.forEach(v => str += v.repeat(order[v]))
//     menu.forEach(v => str += v.repeat((input.match(new RegExp(v, 'gi')) || []).length))
//     return str.match(/[A-Z][a-z]+/g).join(' ')
//     // return str
// }

// function getOrder(input) {
//     let menu = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
//     let str = ''
//     menu.forEach(v => str += v.repeat((input.match(new RegExp(v, 'gi')) || []).length))
//     return str.match(/[A-Z][a-z]+/g).join(' ')
// }

const getOrder = (input) => ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke', ]
    .map(item => (input.match(RegExp(item, 'gi')) || []).fill(item))
    .reduce((acc, arr) => [...acc, ...arr], []).join(' ')

// function getOrder(input) {
//     let menu = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke'];
//     return input
//         .split(/(milkshake|pizza|chicken|fries|coke|burger|sandwich|onionrings)/i)
//         .filter(item => item !== '')
//         .map(item => item.slice(0, 1).toUpperCase() + item.slice(1).toLowerCase())
//         .sort((a, b) => menu.indexOf(a) > menu.indexOf(b) ? 1 : -1)
//         .join(' ');
// }


q = getOrder("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")
// "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke");
q
q = getOrder("pizzachickenfriesburgercokemilkshakefriessandwich")
// "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke");
q