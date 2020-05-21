// 6kyu - Create Phone Number

// function createPhoneNumber(numbers) {
//     let areaCode = numbers.splice(0, 3).join ``
//     numbers.splice(3, 0, '-')
//     return '(' + areaCode + ') ' + numbers.join ``
// }

// function createPhoneNumber(numbers) {
//     let format = '(xxx) xxx-xxxx'
//     for (let i = 0; i < numbers.length; i++)
//         format = format.replace('x', numbers[i])
//     return format
// }

// const createPhoneNumber = numbers => numbers.join('').replace(/(...)(...)(.*)/, '($1) $2-$3')
// const createPhoneNumber = numbers => '(###) ###-####'.replace(/#/g, () => numbers.shift())
// const createPhoneNumber = numbers => numbers.reduce((p, c) => p.replace('x', c), "(xxx) xxx-xxxx")

function createPhoneNumber(numbers) {
    let nums = numbers.join('')
    return '(' + nums.substr(0, 3) + ') ' + nums.substr(3, 6) + '-' + nums.substr(6)
}

// function createPhoneNumber(numbers) {
//     let nums = numbers.join ``
//     return '(' + nums.slice(0, 3) + ') ' + nums.slice(3, 6) + '-' + nums.slice(6)
// }

// function createPhoneNumber(numbers) {
//     let numStr = numbers.join('')
//     let first = numStr.substr(0, 3)
//     let second = numStr.substr(3, 3)
//     let third = numStr.substr(-4)
//     return '(' + first + ') ' + second + '-' + third
// }

q = createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
q
// "(123) 456-7890"
q = createPhoneNumber([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
q
// "(111) 111-1111"
q = createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
q
// "(123) 456-7890"