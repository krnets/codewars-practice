X=s=>+[...s].reduce((a,b)=>a^b)
// X=i=>eval(i.replace(/ /g,'^'))
// X=s=>eval(s.split` `.join`^`)

q = X('1 0 0 1 0') // 0
q
q = X('1 0 1 1 1 0 0 1 0 0 0 0') // 1
q
q = X('1 0 0 1 0 1 0 0 1 0 1 0 1 0 1 0 1 0') // 0
q