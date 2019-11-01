// 7kyu - Loose change

let CHANGE = {
    penny: 0.01,
    nickel: 0.05,
    dime: 0.10,
    quarter: 0.25,
    dollar: 1.00,
}

// const changeCount = (count) => '$' + count.split(' ').reduce((prev, curr) => prev + CHANGE[curr], 0).toFixed(2)

// const changeCount = (change, sum = 0) => '$' + change.split(' ').map(v => sum += CHANGE[v]).reverse()[0].toFixed(2)

const changeCount = count => count.split(' ')
                    .reduce((prev, curr) => prev + CHANGE[curr], 0)
                    .toLocaleString('en-US', {style: 'currency', currency: 'USD'}) 


q = changeCount('dime penny dollar') //  '$1.11'
q
q = changeCount('dime penny nickel') //  '$0.16'
q
q = changeCount('quarter quarter') //  '$0.50'
q
q = changeCount('dollar penny dollar') //  '$2.01'
q
q = changeCount('dollar dollar dollar dollar dollar dollar dollar dollar dollar dollar penny') // '$10.01'
q