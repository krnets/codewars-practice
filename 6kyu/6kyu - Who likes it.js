// 6kyu - Who likes it?

function likes(names) {
    names = names || []
    switch (names.length) {
        case 0: return 'no one likes this'
        case 1: return names[0] + ' likes this'
        case 2: return names[0] + ' and ' + names[1] + ' like this'
        case 3: return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
        default: return names[0] + ', ' + names[1] + ' and ' + (names.length - 2) + ' others like this'
    }
}

q = likes() // 'no one likes this'
q
q = likes([]) // 'no one likes this'
q
q = likes(['Peter']) // 'Peter likes this'
q
q = likes(['Jacob', 'Alex']) // 'Jacob and Alex like this'
q
q = likes(['Max', 'John', 'Mark']) // 'Max, John and Mark like this'
q
q = likes(['Alex', 'Jacob', 'Mark', 'Max']) // 'Alex, Jacob and 2 others like this'
q