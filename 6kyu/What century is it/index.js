/* 6kyu - What century is it

Return the inputted numerical year in century format. For example 2014, would return 21st.
The input will always be a 4 digit string. So there is no need for year string validation */


function whatCentury(year) {
    let c = Math.floor((year - 1) / 100) + 1
    let s = String(c).slice(-1)

    if (c > 3 && c < 21) return c + 'th'
    if (s == 1) return c + 'st'
    if (s == 2) return c + 'nd'
    if (s == 3) return c + 'rd'
}


q = whatCentury(1999) // 20th
q
q = whatCentury(2011) // 21st
q
q = whatCentury(2154) // 22nd
q
q = whatCentury(2259) // 23rd
q
q = whatCentury(1124) // 12th
q
q = whatCentury(2000) // 20th
q