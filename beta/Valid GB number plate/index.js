// Beta - Valid GB number plate?

/* You need to build a function (check) which takes an input string (plate) 
and checks if it is a valid (simplified) GB number plate format.

If the input is a valid GB number plate, your code should return a string containing the year of registration, 
and the region in which it was registered (lookup preloaded in code as constant ref, also see table below).

If the input is not a valid GB number plate, your code should return "Error! Invalid number plate"
Valid input

A valid plate has a two letter region code, two numbers to indicate year of registration, and three random letters. 
All letters should always be upper case.
example

Letters I, Q, and Z cannot be used in either character of the region code. 
Furthermore, letters J, T, U, X are not assigned to a region (see table below), 
so they cannot be used as the first character of the region code. 
Letters I and Q cannot be used in the 3 random letters.

Your code should ignore any whitespace
Your code should check that the car's year of registration is not greater than the current year, 
e.g. in the year 2019, a plate with year of registration 2022 should be rejected with the usual error message

The year 2000 should give an error, since the system was introduced in 2001
NB only the first letter of the two digit region code is needed to determine the region 
(reference table included below and as preloaded object ref)

There is a complication for the year code! Each year has two age identifier codes. 
The year is represented either as its last two digits (e.g. 10 for 2010) or its last two digits plus 50 (e.g. also 60 for 2010).
Example

check("PR13BYP") // should return "2013, Preston"
check("PR13BY") // should return "Error! Invalid number plate"  --> only 2 random letters
check("SP 66MEX") // should return "2016, Scotland"
check("BB32RTS") // should return "Error! Invalid number plate" --> date is future
check("AD15RQS") // should return "Error! Invalid number plate" --> Q not allowed in random letters
check("pr13byp") // should return "Error! Invalid number plate" --> lower case letters not allowed

Notes on kata simplifications vs real licensing system
For simplicity, we will only be checking against the current system (as of 2019), which came into force in 2001.
In reality the year codes which add 50 (such as 60 for 2010) could also indicate that the car was registered 
at the beginning of the following year (e.g. 2011), as these codes run Sept-Feb, 
but for the purposes of this Kata don't worry about that.
Quirks such as personalised number plates or small exceptions to the normal system are also ignored
Region Code Reference
This is already preloaded in the code as a constant named ref

If you're interested for full details in how the system works (beyond the scope of this Kata), see the DVLA's guide here */
const ref = {
    A: "Anglia",
    B: "Birmingham",
    C: "Cymru (Wales)",
    D: "Deeside",
    E: "Essex",
    F: "Forest and Fens",
    G: "Garden of England",
    H: "Hampshire and Dorset",
    K: "Milton Keynes",
    L: "London",
    M: "Manchester and Merseyside",
    N: "North",
    O: "Oxford",
    P: "Preston",
    R: "Reading",
    S: "Scotland",
    V: "Severn Valley",
    W: "West of England",
    Y: "Yorkshire"
}

function check(plate) {
    plate = plate.replace(/\s/, '')
    let [region, year, rndNum] = [plate.slice(0, 2), plate.slice(2, 4), plate.slice(4)]
    let currentYear = String(new Date().getUTCFullYear()).slice(-2)
    let invalidRandomChars = 'IQ'
    let invalidRegionChars = 'IQZ'
    let notAssignedRegion = 'JTUX'
    if ((plate.length < 7) ||
        (region.match(/\d/)) ||
        (rndNum.match(/\d/)) ||
        (year.match(/[a-z]/i)) ||
        (plate.toUpperCase() != plate) ||
        (year % 50 == 0 || year % 50 > currentYear) ||
        (notAssignedRegion.includes(region[0])) ||
        ([...region].filter(v => invalidRegionChars.includes(v)).length > 0) ||
        ([...rndNum].filter(v => invalidRandomChars.includes(v)).length > 0))
        return 'Error! Invalid number plate'
    return [2000 + year % 50, ref[region[0]]].join(', ')
}

// const check = plate => {
//     const plateRegex = /^([A-HK-PRSVWY][A-HJ-PR-Y])([05][1-9]|[16]\d)([A-HJ-PR-Z]{3})$/;
//     plate = plate.replace(/ /g, '');
//     if (!plateRegex.test(plate)) return 'Error! Invalid number plate';
//     let [dvla, age, smr] = plate.match(plateRegex).slice(1);
//     let year = +age < 20 ? +age : age - 50;
//     return `20${year < 10 ? '0' : ''}${year}, ${ref[dvla[0]]}`;
// }

q = check("KU63LBU") // - Expected: '2013, Milton Keynes', instead got: 'Error! Invalid number plate'
q
q = check("DT02URN") // - Expected: '2002, Deeside', instead got: 'Error! Invalid number plate'
q
q = check("SX05YNZ") // - Expected: '2005, Scotland', instead got: 'Error! Invalid number plate'
q
q = check("NX17SXO") // - Expected: '2017, North', instead got: 'Error! Invalid number plate'
q
q = check("NX64YJP") // - Expected: '2014, North', instead got: 'Error! Invalid number plate'
q
q = check("PR13BYP") // "2013, Preston", "PR13BYP should be valid"
q
q = check("SP 66MEX") // "2016, Scotland", "SP 66MEX should be valid (because formula should ignore whitespace)"
q
q = check("KC54UCH") // "2004, Milton Keynes", "KC54UCH should be valid"
q
q = check("UG10BEW") //- Expected: 'Error! Invalid number plate', instead got: '2010, '
q
q = check("HH50NSJ") // should give error message (because 2000 is invalid year) - Expected: 'Error! Invalid number plate', instead got: '2000, Hampshire and Dorset'
q
q = check("H366NSJ") // should give error message (because letter/number format is invalid) - Expected: 'Error! Invalid number plate', instead got: '2016, Hampshire and Dorset'
q
q = check("GH56P7K") // should give error message (because letter/number format is invalid) - Expected: 'Error! Invalid number plate', instead got: '2006, Garden of England'
q
q = check("PR13BY") // "Error! Invalid number plate", "PR13BY should give error message (because letter/number format is invalid)"
q
q = check("BB32RTS") // "Error! Invalid number plate", "BB32RTS should give error message (because year is future)"
q
q = check("AD15RQS") // "Error! Invalid number plate", "AD15RQS should give error message (because random letters include invalid character)"
q
q = check("XA15RKS") // "Error! Invalid number plate", "XA15RKS should give error message (because region code not valid)"
q