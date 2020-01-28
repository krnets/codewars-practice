// 7kyu - Next birth-day of the week finder

/* Can you find after how many years will a person's birthday fall on the same day of the week that he was born?

For example, Joy's birthday is on 16th October, 1990 which falls on Friday. 
After how many years will his birthday fall on Friday again? (That would be 11 years) */

// let year = a.getFullYear()
// let month = a.getMonth()
// let day = a.getDate()
// let dayOfWeek = a.getDay()

function nextBirthdayOfTheWeek(birthday) {
    let a = new Date(birthday)
    let [year, month, day, dayOfWeek] = [a.getFullYear(), a.getMonth(), a.getDate(), a.getDay()]
    for (let i = 1;; i++) {
        let b = new Date(year + i, month, day)
        if (dayOfWeek == b.getDay()) return i
    }
}

q = nextBirthdayOfTheWeek(new Date(1990, 10, 16)) // 11
q
q = nextBirthdayOfTheWeek(new Date(2012, 5, 20)) // 6
q
q = nextBirthdayOfTheWeek(new Date(1975, 2, 22)) // 5
q