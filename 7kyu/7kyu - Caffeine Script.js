// 7kyu - Caffeine Script

/* Complete the function caffeineBuzz, which takes a non-zero integer as it's one argument.
If the integer is divisible by 3, return the string "Java".
If the integer is divisible by 3 and divisible by 4, return the string "Coffee"
If the integer is one of the above and is even, add "Script" to the end of the string.
Otherwise, return the string "mocha_missing!" */

const caffeineBuzz = (n) => n % 2 == 0 && n % 3 == 0 && n % 4 == 0 ? 'CoffeeScript' :
                            n % 2 == 0 && n % 3 == 0 ? 'JavaScript' :
                            n % 3 == 0 && n % 4 == 0 ? 'Coffee' :
                            n % 3 == 0 ? 'Java' : 'mocha_missing!'

function caffeineBuzz(n) {
    switch (0) {
        case n % 1: return "CoffeeScript";
        case n % 6: return "JavaScript";
        case n % 3: return "Java";
        default: return "mocha_missing!";
    }
}

q = caffeineBuzz(1) //  "mocha_missing!"
q
q = caffeineBuzz(3) //  "Java"
q
q = caffeineBuzz(6) //  "JavaScript"
q
q = caffeineBuzz(12) //  "CoffeeScript"
q