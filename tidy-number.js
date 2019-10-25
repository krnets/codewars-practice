const tidyNumber = n => String(n).split('').map((num, i, self) => i === 0 ? 1 : num - self[i - 1]).every(num => num >= 0)

q = tidyNumber(12) //,true
q
q = tidyNumber(102) //,false
q
q = tidyNumber(9672) //,false
q
q = tidyNumber(2789) //,true
q
q = tidyNumber(2335) //,true
q