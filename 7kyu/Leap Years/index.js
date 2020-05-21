/* 7kyu - Leap Years

In this kata you should simply determine, whether a given year is a leap year or not. 
In case you don't know the rules, here they are:

    years divisible by 4 are leap years
    but years divisible by 100 are not leap years
    but years divisible by 400 are leap years

Only valid years (positive integers) will be tested, so you don't have to validate them */

// const isLeapYear = year => (year % 400 == 0) || (year % 4 == 0) && (year % 100 != 0)

// const moment = require('moment');

// function isLeapYear(year) {
//   return moment([year]).isLeapYear()
// }

// import moment from 'moment';

// const isLeapYear = year => moment([year]).isLeapYear()

// const isLeapYear = year => new Date(year, 1, 29).getMonth() == 1

const isLeapYear = year => !(year / 4 % 4)


q = isLeapYear(1234) // false, 'Year 1234'
q
q = isLeapYear(1984) // true, 'Year 1984'
q
q = isLeapYear(2000) // true, 'Year 2000'
q
q = isLeapYear(2010) // false, 'Year 2010'
q
q = isLeapYear(2013) // false, 'Year 2013'
q
q = isLeapYear(1900) // true, 'Year 2000'
q