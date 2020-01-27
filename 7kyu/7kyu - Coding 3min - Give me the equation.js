// 7kyu - Coding 3min - Give me the equation

/* Give you three numbers:```a b c```,please return an equation(Operators include +,-,*,/), return type is string.

```sc(1,2,3)``` should return ```"1+2=3"``` or ```"2+1=3"```  or  ```"3-2=1"```  or ```"3-1=2"```
```sc(2,2,4)``` should return ```"2+2=4"``` or ```"2*2=4"```  or ```"4/2=2"```  or ```"4-2=2"```
```sc(6,2,3)``` should return ```"2*3=6"``` or ```"3*2=6"```  or ```"6/2=3"``` or ```"6/3=2"```

Return one of the possible answer, you can pass the test.
If there is ```no equation between a,b,c```, return ```""``` */

function sc(a, b, c) {
    if (a + b == c) return `${a}+${b}=${c}`
    if (a + c == b) return `${a}+${c}=${b}`
    if (a - b == c) return `${a}-${b}=${c}`
    if (a - c == b) return `${a}-${c}=${b}`
    if (a * b == c) return `${a}*${b}=${c}`
    if (a * c == b) return `${a}*${c}=${b}`
    if (a / b == c) return `${a}/${b}=${c}`
    if (a / c == b) return `${a}/${c}=${b}`
    return ''
}


q = sc(1, 2, 3) // 1+2=3"||sc(1,2,3)=="2+1=3"||sc(1,2,3)=="3-2=1"||sc(1,2,3)=="3-1=2", true, "good luck!"
q
q = sc(2, 2, 4) // 2+2=4"||sc(2,2,4)=="2*2=4"||sc(2,2,4)=="4-2=2"||sc(2,2,4)=="4/2=2", true, "good luck!"
q
q = sc(6, 2, 3) // 2*3=6"||sc(6,2,3)=="3*2=6"||sc(6,2,3)=="6/2=3"||sc(6,2,3)=="6/3=2", true, "good luck!"
q
q = sc(6, 5, 4) // ,"", "good luck!"
q
q = sc(2, 3, 4) // "", "good luck!
q