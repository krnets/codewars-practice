// 8kyu - Is the date today

/* Write a simple function that takes as a parameter a date object and returns a boolean value 
representing whether the date is today or not.

Make sure that your function does not return a false positive by just checking just the day. */


function isToday(date) {
    return new Date().toLocaleString() == date.toLocaleString()
}

var tomorrow = new Date();
tomorrow.setDate(tomorrow.getDate() + 1);

var yesterday = new Date();
yesterday.setDate(yesterday.getDate() - 1);

q = isToday(new Date()) // true
q
q = isToday(tomorrow) // false
q
q = isToday(yesterday) // false
q