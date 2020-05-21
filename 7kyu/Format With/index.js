// 7kyu - Format With

/* Write

String.prototype.formatWith = function () {}

that takes in a list of arguments and formats the string based off these arguments and indices.

'Hello {0}'.formatWith('Codewars') ===  'Hello Codewars'
'{0} + {0} = {1}'.formatWith('1','2') ===  '1 + 1 = 2'
'Testing {1}'.formatWith('kata') === 'Testing {1}' // there is no arguments at position 1

Fundamentals | Strings */


String.prototype.formatWith = function (...args) {
    return this.replace(/{(\d+)}/g, (match, index) => args[index] || match)
}

q = 'Hello {0}'.formatWith('Codewars') // 'Hello Codewars'
q
q = '{0} is a {1} {2}'.formatWith('Today', 'good', 'day') // 'Today is a good day'
q
q = '{0} + {0} = {1}'.formatWith('1', '2') // '1 + 1 = 2'
q
q = 'Hello {0}. This {1} is bring a {2} to work day'.formatWith('World', 'Monday', 'dog') // 'Hello World. This Monday is bring a dog to work day'
q
q = 'Testing {1}'.formatWith('kata') // 'Testing {1}'
q