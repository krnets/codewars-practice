// 7kyu - Sort deck of cards

/* Write a function sort_cards() that sorts a shuffled list of cards, 
so that any given list of cards is sorted by rank, no matter the starting collection.

All cards in the list are represented as strings, so that sorted list of cards looks like this:
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Example:
>>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Hint: Tests will have many occurrences of same rank cards, as well as vary in length. 
You can assume though, that input list is always going to have at least 1 element. */

// function sortCards(array) {
//     let cmp = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
//     return array.sort((a, b) => cmp.indexOf(String(a)) - cmp.indexOf(String(b)))
// }

function sortCards(array) {
    let rank = 'A23456789TJQK'
    return array.sort((a, b) => rank.indexOf(a) - rank.indexOf(b))
}

// const sortCards = arr => arr.sort((a, b) => "A23456789TJQK".indexOf(a) - "A23456789TJQK".indexOf(b))

q = sortCards([3, 9, "A", 5, "T", 8, 2, 4, "Q", 7, "J", 6, "K"]) // (["A",2,3,4,5,6,7,8,9,"T","J","Q","K"])
q
q = sortCards(["J", "J", 2, "T", 9, 6]) // ([2,6,9,"T","J","J"])
q
q = sortCards(["A", 2, 3, 4, 5, 6, 6, 7, 8, 9, "T", "J", "Q", "A"]) // (['A', 'A', 2, 3, 4, 5, 6, 6, 7, 8, 9, 'T', 'J', 'Q'])
q