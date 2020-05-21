// 7kyu - The Office II - Boredom Score

// Depending on the cumulative score of the team, return the appropriate sentiment.

function boredom(staff) {
    let department = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25,
    }
    let boredomScore = Object.values(staff).reduce((a, b) => a + department[b], 0)

    return boredomScore <= 80 ? 'kill me now' : boredomScore < 100 ? 'i can handle this' : 'party time!!'
}

q = boredom({
    tim: 'pissing about',
    jim: 'canteen',
    randy: 'IS',
    sandy: 'pissing about',
    andy: 'change',
    katie: 'regulation',
    laura: 'change',
    saajid: 'IS',
    alex: 'accounts',
    john: 'regulation',
    mr: 'retail'
})
// 'party time!!');
q

q = boredom({
    tim: 'change',
    jim: 'accounts',
    randy: 'canteen',
    sandy: 'change',
    andy: 'change',
    katie: 'IS',
    laura: 'change',
    saajid: 'IS',
    alex: 'trading',
    john: 'accounts',
    mr: 'finance'
})
q
// 'kill me now'

q = boredom({
    tim: 'IS',
    jim: 'finance',
    randy: 'pissing about',
    sandy: 'cleaning',
    andy: 'cleaning',
    katie: 'cleaning',
    laura: 'pissing about',
    saajid: 'regulation',
    alex: 'regulation',
    john: 'accounts',
    mr: 'canteen'
})
q
// 'i can handle this');

q = boredom({
    tim: 'accounts',
    jim: 'accounts',
    randy: 'pissing about',
    sandy: 'finance',
    andy: 'change',
    katie: 'IS',
    laura: 'IS',
    saajid: 'canteen',
    alex: 'pissing about',
    john: 'retail',
    mr: 'pissing about'
})
q
// 'party time!!');