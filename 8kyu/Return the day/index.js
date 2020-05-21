// 8kyu - Return the day 

/* Complete the function which returns the weekday according to the input number:

    1 returns "Sunday"
    2 returns "Monday"
    3 returns "Tuesday"
    4 returns "Wednesday"
    5 returns "Thursday"
    6 returns "Friday"
    7 returns "Saturday"
    Otherwise returns "Wrong, please enter a number between 1 and 7" */


function whatday(num) {
    return 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.split(' ')[num - 1] || 'Wrong, please enter a number between 1 and 7'
}

q = whatday(1) // 'Sunday'
q
q = whatday(2) //  'Monday'
q
q = whatday(3) // 'Tuesday'
q
q = whatday(8) //   'Wrong, please enter a number between 1 and 7'
q
q = whatday(20) //  'Wrong, please enter a number between 1 and 7'
q