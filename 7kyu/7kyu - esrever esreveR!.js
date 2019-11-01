// 7kyu - esrever esreveR!

const esrever = str => [...str].reverse().join``.slice(1).concat(str.slice(-1))

q = esrever('an Easy one?') // 'eno ysaE na?'
q
q = esrever('a small lOan OF 1,000,000 $!') // '$ 000,000,1 FO naOl llams a!'
q
q = esrever('<?> &!.".') // '".!& >?<.'
q
q = esrever('b3tTer p4ss thIS 0ne.') // 'en0 SIht ss4p reTt3b.'
q
q = esrever('') // ''
q