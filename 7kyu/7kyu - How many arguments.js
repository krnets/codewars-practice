/** 7kyu - How many arguments
*
* Create a function called args_count that returns the number of arguments provided */

// const args_count = (...args) => args.length

function args_count() {
    return arguments.length
}


q = args_count(1, 2) // 2
q
q = args_count() // 0
q
q = args_count('A', 'B', 'C') // 3
q
q = args_count(["foo", "bar"]) // 1
q