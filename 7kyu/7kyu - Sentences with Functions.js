// 7kyu - Sentences with Functions

/* Implement all required functions in order to create the following sentences by calling those functions:

Adam(has(a(dog()))); // must return "Adam has a dog."
The(name(of(the(dog(is(also(Adam()))))))); // must return "The name of the dog is also Adam."

Fundamentals
Functions
Control Flow
Basic Language Features
Function Composition
Composition
Functional Programming
Design Principles
Declarative Programming */

// function Adam(fn){ return fn ? 'Adam ' + fn : 'Adam.'}
// function has(fn) { return fn ? 'has '  + fn : 'has.' }
// function a(fn)   { return fn ? 'a '    + fn : 'a.'   }
// function dog(fn) { return fn ? 'dog '  + fn : 'dog.' }
// function The(fn) { return fn ? 'The '  + fn : 'The.' }
// function name(fn){ return fn ? 'name ' + fn : 'name.'}
// function of(fn)  { return fn ? 'of '   + fn : 'of.'  }
// function the(fn) { return fn ? 'the '  + fn : 'the.' }
// function is(fn)  { return fn ? 'is '   + fn : 'is.'  }
// function also(fn){ return fn ? 'also ' + fn : 'also.'}

// const append = str => add => add + (str ? ' ' + str : '.')

// const Adam = fn => append(fn)('Adam')
// const has  = fn => append(fn)('has')
// const a    = fn => append(fn)('a')
// const dog  = fn => append(fn)('dog')
// const The  = fn => append(fn)('The')
// const name = fn => append(fn)('name')
// const of   = fn => append(fn)('of')
// const the  = fn => append(fn)('the')
// const is   = fn => append(fn)('is')
// const also = fn => append(fn)('also')

function getName(args) {
    return args.length ? arguments.callee.caller.name + ' ' + args[0] : arguments.callee.caller.name + '.'
}

function Adam() { return getName(arguments) }
function has()  { return getName(arguments) }
function a()    { return getName(arguments) }
function dog()  { return getName(arguments) }
function The()  { return getName(arguments) }
function name() { return getName(arguments) }
function of()   { return getName(arguments) }
function the()  { return getName(arguments) }
function is()   { return getName(arguments) }
function also() { return getName(arguments) }

q = Adam()
q
q = Adam(has())
q
q = Adam(has(a(dog()))); // must return "Adam has a dog."
q
q = The(name(of(the(dog(is(also(Adam()))))))); // must return "The name of the dog is also Adam."
q