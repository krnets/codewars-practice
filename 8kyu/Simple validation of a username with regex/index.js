// 8kyu - Simple validation of a username with regex

/* Write a simple regex to validate a username. Allowed characters are:

    lowercase letters,
    numbers,
    underscore

Length should be between 4 and 16 characters (both included).
Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings | Validation | Algorithms */

const validateUsr = (username) => /^[a-z_0-9]{4,16}$/.test(username)

q = validateUsr('asddsa') // true
q
q = validateUsr('a') // false
q
q = validateUsr('Hass') // false
q
q = validateUsr('Hasd_12assssssasasasasasaasasasasas') // false
q
q = validateUsr('') // false
q
q = validateUsr('____') // true
q
q = validateUsr('012') // false
q
q = validateUsr('p1pp1') // true
q
q = validateUsr('asd43 34') // false
q
q = validateUsr('asd43_34') // true
q