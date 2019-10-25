let dupList = ['b','a','b','c']
// x = [...new Set(dupList)]
// x = Array.from(new Set(dupList))
const seen = new Set()

x = dupList.filter( v => {
    if(seen.has(v))
        return false;
    seen.add(v)
    return true
})
x