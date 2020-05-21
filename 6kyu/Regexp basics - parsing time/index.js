// 6kyu - Regexp basics - parsing time

/* Implement String#to_seconds, which should parse time expressed as HH:MM:SS, or nil otherwise.

Any extra characters, or numbers of minutes/seconds higher than 59, should result in nil being returned.
Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings */

// String.prototype.toSeconds = function () {
//     if (/^\d\d:([0-5]\d):([0-5]\d)$/.test(this)) {
//         [hh, mm, ss] = this.split(':')
//         return hh * 3600 + mm * 60 + Number(ss)
//     }
//     return null
// }

// String.prototype.toSeconds = function () {
//     if (!/^\d\d:[0-5]\d:[0-5]\d$/.test(this)) return null
//     let [hh, mm, ss] = this.split(':')
//     return hh * 3600 + mm * 60 + Number(ss)
// }

// String.prototype.toSeconds = function () {
//     return (/^\d\d:[0-5]\d:[0-5]\d$/.test(this)) ?
//         this.split(':').reduce((a, b) => 60 * a + Number(b)) : null
// }

String.prototype.toSeconds = function () {
    return (/^\d\d(:[0-5]\d){2}$/.test(this)) ?
        this.split(':').reduce((a, b) => 60 * a + Number(b)) : null
}

q = "00:00:00".toSeconds() // 0
q
q = "01:02:03".toSeconds() // 3723
q
q = "01:02:60".toSeconds() // null
q
q = "01:60:03".toSeconds() // null
q
q = "99:59:59".toSeconds() // 359999
q
q = "0:00:00".toSeconds() // null
q
q = "00:0:00".toSeconds() // null
q
q = "00:00:0".toSeconds() // null
q
q = "00:00:00\n".toSeconds() // null
q
q = "\n00:00:00".toSeconds() // null
q