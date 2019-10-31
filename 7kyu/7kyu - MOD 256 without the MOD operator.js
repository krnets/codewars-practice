// 7kyu - MOD 256 without the MOD operator

// const mod256WithoutMod = (number) => number - Math.trunc(number / 256) * 256
// const mod256WithoutMod = (number) => number - (number / 256 | 0) * 256
// const mod256WithoutMod = (D, d = 256) => D - (D / d | 0) * d
const mod256WithoutMod = n => n - (n / 256 | 0) * 256

// const mod256WithoutMod = (number) => (number < 0) ? -mod256WithoutMod(-number) : number & 255

// function mod256WithoutMod(number) {
//     const n = number & 255
//     return number * n < 0 ? n - 256 : n
// }


q = mod256WithoutMod(254) // 254
q
q = mod256WithoutMod(256) // 0
q
q = mod256WithoutMod(258) // 2
q
q = mod256WithoutMod(-254) // -254
q
q = mod256WithoutMod(-256) // 0
q
q = mod256WithoutMod(-258) // -2
q