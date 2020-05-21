// 7kyu - Date encryption

/* Write a function that takes an date in format Y-m-d(String) and 
return it in an encrypted format, to do this you will break the string of date, 
each 2 characteres of date(except '-') being an ASCII numeric code add 50 to it and 
return the result translated according to ASCII table with the '-' between it.

 "2017-01-21" -> You will get 20 17 - 01 - 21 (for each of then +50)-> 70 67 - 51 - 71 ->(ASCII Translation)-> "FC-3-G"
"1966-12-07" -> "Et->-9" */

// function translateDate(dateStr) {
//     let arr = dateStr.split('-')

//     return [arr[0].substr(0, 2), arr[0].substr(2, 2)]
//                 .concat(arr.slice(1))
//                 .map(v => String.fromCharCode(v * 1 + 50))
//                 .join('-').replace(/-/, '')
// }

// const translateDate = (dateStr) => dateStr.replace(/\d\d/g, v => String.fromCharCode(+v + 50))
const translateDate = (dateStr) => dateStr.replace(/\d{2}/g, v => String.fromCharCode(+v + 50))

q = translateDate('2017-01-21') // 'FC-3-G', 'The first basic example'
q
q = translateDate('1966-12-07') // 'Et->-9', 'The second basic example'
q
q = translateDate('2010-07-29') // 'F<-9-O', 'here you go!'
q
q = translateDate('2002-02-02') // 'F4-4-4', 'Easy?'
q
q = translateDate('2055-11-11') // 'Fi-=-=', 'You get it!'
q