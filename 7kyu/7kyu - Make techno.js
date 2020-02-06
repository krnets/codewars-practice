// 7kyu - Make techno

/* German music producer Herbert Von Klunkerkunt has been using the same formula to make industrial techno for over twenty years. 
Producing at 120 beats per minute, each 4-beat bar contains:

    4 kick drum hits
    8 hihat hits
    2 clap hits

Write a programme that takes the number of minutes and returns the number of "kicks", "hihats" and "claps" Klunkerkunt 
will need to fill each bar of his new track with percussion in an array. The total number of kicks, hihats and claps 
should be rounded to the nearest integer.

function perc (3) {}
// should return ["360 kicks", "720 hihats", "180 claps"]

The function should return "invalid track time" if the number of minutes is:

    less than 1
    more than 100
    not a number

function perc (0.22) {}
// should return "invalid track time" */

function perc(mins) {
    let bpm = 120
    let kicks = 4
    let hihats = 8
    let claps = 2
    let beatsPerBar = 4
    let kicksTotal = Math.round(kicks * bpm * mins / beatsPerBar)
    let hihatsTotal = Math.round(hihats * bpm * mins / beatsPerBar)
    let clapsTotal = Math.round(claps * bpm * mins / beatsPerBar)
    return mins >= 1 && mins <= 100 ? [kicksTotal + ' kicks', hihatsTotal + ' hihats', clapsTotal + ' claps'] : 'invalid track time'
}

q = perc(3) // ["360 kicks", "720 hihats", "180 claps"]
q
q = perc(99.9999) // ["12000 kicks", "24000 hihats", "6000 claps"]
q
q = perc("a") // "invalid track time"
q
q = perc(113.567) // "invalid track time"
q
// q = perc(5) // "invalid track time"
// q
// q = perc(0.1) // ["4 kicks", "8 hihats", "2 claps"]
// q