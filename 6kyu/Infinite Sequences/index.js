// 6kyu - Infinite Sequences

// function sequence(fun) {
//     return new Seq(fun)
// }

// class Seq {
//     constructor(func) {
//         this.func = func
//     }
//     take(n) {
//         return Array(n).fill().map((_, i) => this.func(i))
//     }
//     takeWhile(cond) {
//         let res = []
//         let i = 0
//         while (true) {
//             const add = this.func(i)
//             if (!cond(add)) {
//                 return res
//             }
//             res.push(add)
//             i++
//         }
//     }
// }

// function sequence(fun) {
//     class Seq {
//         constructor(func) {
//             this.func = func
//         }
//         take(n) {
//             return Array(n).fill().map((_, i) => this.func(i))
//         }
//         takeWhile(cond) {
//             let res = []
//             let i = 0
//             while (true) {
//                 const add = this.func(i)
//                 if (!cond(add))
//                     return res
//                 res.push(add)
//                 i++
//             }
//         }
//     }
//     return new Seq(fun)
// }

// function sequence(fun) {
//     return {
//         take: n => [...Array(n)].map((_, i) => fun(i)),
//         takeWhile: (fn) => {
//             const res = []
//             for (let i = 0; i < Number.MAX_SAFE_INTEGER; i++) {
//                 const entry = fun(i)
//                 if (!fn(entry)) break
//                 res.push(entry)
//             }
//             return res
//         }
//     }
// }

function sequence(fn) {
    return {
        take: n => [...Array(n)].map((_, i) => fn(i)),
        takeWhile: (pred) => {
            let res = [], i = 0
            while (pred(fn(i))) res.push(fn(i++))
            return res
        }
    }
}

// function sequence(fn) {
//     let take = n => [...Array(n)].map((_, i) => fn(i))
//     let takeWhile = pred => { let res = [], i = 0; while (pred(fn(i))) res.push(fn(i++)); return res }
//     return { take, takeWhile }
// }

// Function.prototype.then = function then(fn) { return (...a) => fn(this(...a)); };
// const snd = (...[, snd]) => snd;

// const sequence = fn => ({ 
//     take: length => Array.from({ length }, snd.then(fn)),
//     takeWhile: p => function go(i) { const v = fn(i); return p(v) ? [v, ...go(i + 1)] : []; }(0), });


q = sequence(n => n * n).take(5) // [0, 1, 4, 9, 16]
q
q = sequence(n => n).take(5) // [0, 1, 2, 3, 4]
q
q = sequence(n => n * 4).takeWhile(n => n < 20) // [0, 4, 8, 12, 16]
q