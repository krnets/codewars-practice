// 6kyu - One line kata: Sum Multiples of 3 and 5

/* Yet another one-line task involving threes and fives (I know, I'm the worst), 
inspired by Sum of All the Multiples of 3 or 5, in this kata you need to do exactly what the name says: 
Return the sum of all numbers divisible by three or five up to and including n in under 53 characters in JS 

Inputs may be up to ~200m. They will always be valid, non-negative integers.

sum(2)=> 0
sum(5)=> 8
sum(10)=> 33
sum(100)=> 2418
sum(1000)=> 234168
sum(1111)=> 288045

0 <- sum(2)
8 <- sum(5) 8
33 <- sum(10)
2418 <- sum(100)
234168 <- sum(1000)
288045 <- sum(1111) */

sum = n => {
    t = (n, f) => {
        n = ~((n - 1) / f);
        return f * n * (n + 1) / 2
    };
    return t(n, 3) + t(n, 5) - t(n, 15) + n
}

// sum=n=>{t=(n,f)=>{n=~((n-1)/f);return f*n*(n+1)/2};return t(n,3)+t(n,5)-t(n,15)+n} // too long (82 char instead of 53 limit)
// sum=n=>(f=>f(3)+f(5)-f(15))(k=>(n-n%k)*(1+n/k>>0)/2)
// sum=(a,b=(b,c=a/b|0)=>c*++c*b)=>(b(3)+b(5)-b(15))/2
// sum=n=>(s=k=>(m=n/k|0,k*m*(m+1)/2),s(3)+s(5)-s(15))
// sum=n=>(s=k=>(l=n/k|0,(l*l+l)*k/2))(3)+s(5)-s(15)
// sum=n=>(f=m=>m/2*(a=n/m|0)*(a+1),f(3)+f(5)-f(15))
// sum=n=>(s=d=>d*~~(n/d)*~~(1+n/d)/2,s(5)+s(3)-s(15)
// sum=n=>(a=x=>x*(y=n/x|0)*(y+1)/2)(3)+a(5)-a(15))


q = sum(0) // 0
q
q = sum(5) // 8
q
q = sum(10) // 33
q
q = sum(100) // 2418
q
q = sum(1000) // 234168
q
q = sum(10000) // 23341668
q
q = sum(100000) // 2333416668
q