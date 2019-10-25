let str = '51NGAP0RE'
// str = str.replace(/5/g, 'S')
// str = str.replace(/1/g, 'I')
// q = str.replace(/0/g, 'O')


const correct = s => s
            .replace(/0/g, 'O')
            .replace(/5/g, 'S')
            .replace(/1/g, 'I')

q = correct(str)
q