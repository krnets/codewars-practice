// 7kyu - Sort Santa's Reindeer

/* Write a function called sortReindeer that accepts an array of Reindeer names, 
and returns an array with the Reindeer names sorted by their last names. */

function sortReindeer(reindeerNames) {
    return reindeerNames.map(v => v.split(' '))
                        .sort((a, b) => a[1].localeCompare(b[1]))
                        .map(v => v.join(' '))
}

q = sortReindeer(["Dasher Tonoyan","Dancer Moore","Prancer Chua","Vixen Hall","Comet Karavani","Cupid Foroutan","Donder Jonker","Blitzen Claus"])
q
// ["Prancer Chua","Blitzen Claus","Cupid Foroutan", "Vixen Hall", "Donder Jonker", "Comet Karavani","Dancer Moore","Dasher Tonoyan"]