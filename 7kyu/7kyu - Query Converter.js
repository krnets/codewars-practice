// 7kyu - Query Converter

/* In web developement. Using query to grab data is very common. Query starts with '?' after the link

Link: www.whatsup.com?name=huy&lastname=dang
Query: ?name=huy&lastname=dang

Write a function that return an object that contains all the datas in the query which are seperated by '&'

Example: www.whatsup.com?name=Huy&lastname=Dang
-> Query: ?name=Huy&lastname=Dang
-> Should return: {name: 'Huy', lastname: 'Dang'}

// p/s: - No case sensitive, easy, keep it the way it is. */

// const convertArrayToObject = (array, key) => array.reduce(obj => (obj[item[key]] = item, obj), {});

// const solution = (str) => str
//     .replace(/^.*[?]/g, '')
//     .split('&').map(v => v.split('='))
//     .reduce((obj, _, i, arr) => (obj[arr[i][0]] = arr[i][1], obj), {})

const solution = query => query.split('?')[1].split('&').reduce((obj, s, k, v) => ([k, v] = s.split('='), obj[k] = v, obj), {})
// const solution = (str) => str.split('?')[1].split('&').reduce((obj, s, k, v) => ([k, v] = s.split('='), obj[k] = v, obj), {})

q = solution('www.whatsup.com?name=Huy&lastname=dang') // {name: "Huy", lastname: "dang"}
q
q = solution('www.whatsup.com?name=Sam&age=29') // {name: "Sam", age: '29'}
q
q = solution('www.whatsup.com?shoe=Nike&size=11') // {shoe: "Nike", size: '11'}
q
q = solution('www.whatsup.com?brand=Coach&itemId=9123') // {brand:"Coach", itemId:'9123'}
q
q = solution('www.whatsup.com?make=Honda&model=Civic') // {make: 'Honda', model: 'Civic'}
q
q = solution('www.whatsup.com?item=iphone&gen=X') // {item:'iphone', gen:'X'}
q