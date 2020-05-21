const removeDuplicateWords = str => [...new Set(str.split(' '))].join(' ')

q = removeDuplicateWords('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta')
// 'alpha beta gamma delta'
q