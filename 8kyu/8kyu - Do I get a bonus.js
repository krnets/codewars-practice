// 8 kyu - Do I get a bonus?
/* Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. If bonus is false, 
the fatcat did not make enough money and must receive only his stated salary.

Return the total figure the individual will receive as a string prefixed with "£" 
(= "\u00A3", JS, Go, and Java), "$" (C#, C++, Ruby, Clojure, Elixir, PHP and Python, Haskell, Lua) or "¥" (Rust). */

function bonusTime(salary, bonus) {
    // return bonus ? '£' + salary * 10 : '£' + salary
    return '£' + salary * (bonus ? 10 : 1);
}

q = bonusTime(10000, true) // '£100000'
q
q = bonusTime(25000, true) // '£250000'
q
q = bonusTime(10000, false) // '£10000'
q
q = bonusTime(60000, false) // '£60000'
q
q = bonusTime(2, true) // '£20'
q
q = bonusTime(78, false) // '£78'
q
q = bonusTime(67890, true) // '£678900'
q