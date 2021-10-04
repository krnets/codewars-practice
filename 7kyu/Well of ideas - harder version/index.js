function well(x) {
    let goodIdeas = x.map(sub => sub.filter(v => String(v).toLowerCase() == 'good').length)
                     .reduce((a, b) => a + b, 0)

    return goodIdeas > 2 ? 'I smell a series!' :
           goodIdeas > 0 ? 'Publish!' :
           'Fail!'
}

// let goodIdeas = x.map(sub => sub.filter(v => v == v.match(/good/gi)).length).reduce((a, b) => a + b, 0)
q = well([
    ['bad', 'bAd', 'bad'],
    ['bad', 'bAd', 'bad'],
    ['bad', 'bAd', 'bad']
]), 'Fail!'
q
q = well([
    ['gOOd', 'bad', 'BAD', 'bad', 'bad'],
    ['bad', 'bAd', 'bad'],
    ['GOOD', 'bad', 'bad', 'bAd']
]), 'Publish!'
q
q = well([
    ['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'],
    ['bad'],
    ['gOOd', 'BAD']
]), 'I smell a series!'
q