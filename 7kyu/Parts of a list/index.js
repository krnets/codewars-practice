// 7kyu - Parts of a list

/* Write a function partlist that gives all the ways to divide a list (an array) of 
at least two elements into two non-empty parts.

    Each two non empty parts will be in a pair (or an array)
    Elements of a pair must be in the same order as in the original array. */

const partlist = arr => arr.map((_, i) => [arr.slice(0, i).join(' '), arr.slice(i).join(' ')]).slice(1)

q = partlist(['az', 'toto', 'picaro', 'zone', 'kiwi']) //
// [["az", "toto picaro zone kiwi"], ["az toto", "picaro zone kiwi"],
// ["az toto picaro", "zone kiwi"], ["az toto picaro zone", "kiwi"]]
q

q = partlist(['I', 'wish', 'I', "hadn't", 'come'])
//[['I', "wish I hadn't come"],['I wish', "I hadn't come"],['I wish I', "hadn't come"],["I wish I hadn't", 'come']
q

q = partlist(['cdIw', 'tzIy', 'xDu', 'rThG'])
// [['cdIw', 'tzIy xDu rThG'],['cdIw tzIy', 'xDu rThG'],['cdIw tzIy xDu', 'rThG']]
q
q = partlist(['vJQ', 'anj', 'mQDq', 'sOZ'])
// [['vJQ', 'anj mQDq sOZ'],['vJQ anj', 'mQDq sOZ'],['vJQ anj mQDq', 'sOZ']]
q
