// 8kyu - Training JS 18 - Methods of String object--concat() split() and its good friend join()

function splitAndMerge(string, separator) {
    return string.split(' ').map(v => v.split('').join(separator)).join(' ')
}

q = splitAndMerge("My name is John", " ") // "M y n a m e i s J o h n"
q
q = splitAndMerge("My name is John", "-") // "M-y n-a-m-e i-s J-o-h-n"
q
q = splitAndMerge("Hello World!", ".") // "H.e.l.l.o W.o.r.l.d.!"
q
q = splitAndMerge("Hello World!", ",") // "H,e,l,l,o W,o,r,l,d,!"
q