""" 7kyu - RuplesJS #3: String EachChar

Your team is really excited with all the contributions you've made to the RuplesJS library. 
They feel the work you're doing will truly help Ruby developers transition to Javascript! 
They've assigned you another task.

String.eachChar()

In ruby you can add something after each character in a string like so:

"hello".each_char {|c| print c, ' ' } -> "h e l l o " 

In the spirit of polymorphism, our eachChar method will allow one of two arguments, 
a callback function or a string. If a string is will be added after each character 
of the original string and return the new string. 
If a function is will perform a manipulation of each character in the string.

Example:

each_char("hello"," ")
-> "h e l l o "

def func(c):
    return 'L' if c=='l' else c

each_char("hello all", func)
-> "heLLo aLL" """


# def each_char(string, arg):
#     return ''.join(arg(x) if hasattr(arg, '__call__') else x + arg for x in string)

def each_char(string, arg):
    return ''.join(arg(x) if callable(arg) else x + arg for x in string)


q = each_char("hello", " "), "h e l l o "
q
q = each_char("hello", "123"), "h123e123l123l123o123"
q
q = each_char("", "123"), ""
q


def f(c):
    return c.upper()  # "Should make all characters uppercase:"


q = each_char("hello", f), "HELLO"
q


def f(c):
    return "1" if c == " " else c  # Should turn all spaces into the number 1:


q = each_char("H e l l o ", f), "H1e1l1l1o1"
q


def f(c):
    return "" if c in "0123456789" else c  # Should remove all numbers:


q = each_char("I12 0ca431n35no55t 77re3321231ad 4t4h7771i888973s.", f), "I cannot read this."
q
