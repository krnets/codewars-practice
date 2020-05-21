const maxNumber = n => +[...String(n)].sort((a, b) => b - a).join ``

q = maxNumber(213) // 321
q
q = maxNumber(7389) // 9873
q
q = maxNumber(63792) // 97632
q
q = maxNumber(566797) // 977665
q
q = maxNumber(1000000) // 1000000
q