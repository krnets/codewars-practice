// 7kyu - Coding Meetup 14 - Higher-Order Functions Series - Order the food

/* You will be given an array of objects representing data about developers who have signed up 
to attend the next coding meetup that you are organising.

Your task is to return an object which includes the count of food options selected by the developers on the meetup sign-up form.

    The order of the meals count in the object does not matter.
    The count value should be a valid number.
    The input array will always be valid and formatted as in the example above.
    there are 5 possible meal options and the strings representing the selected meal option will always be formatted in the same way, 
    as follows: 'standard', 'vegetarian', 'vegan', 'diabetic', 'gluten-intolerant'. */

var list1 = [
    { firstName: 'Noah', lastName: 'M.', country: 'Switzerland', continent: 'Europe', age: 19, language: 'C', 
      meal: 'vegetarian' },
    { firstName: 'Anna', lastName: 'R.', country: 'Liechtenstein', continent: 'Europe', age: 52, language: 'JavaScript', 
      meal: 'standard' },
    { firstName: 'Ramona', lastName: 'R.', country: 'Paraguay', continent: 'Americas', age: 29, language: 'Ruby', 
      meal: 'vegan' },
    { firstName: 'George', lastName: 'B.', country: 'England', continent: 'Europe', age: 81, language: 'C', 
      meal: 'vegetarian' },
  ];

// function orderFood(list) {
//     let res = []
//     for (let developer of list)
//         res.push(developer.meal)
//     return res.reduce((acc, v) => { acc[v] = ++acc[v] || 1; return acc }, {})
// }

const orderFood = (list) => list.reduce((acc, v) => (acc[v.meal] = ++acc[v.meal] || 1, acc), {})

q = orderFood(list1) // { vegetarian: 2, standard: 1, vegan: 1 }
q