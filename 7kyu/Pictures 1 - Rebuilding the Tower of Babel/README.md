### Pictures #1 - Rebuilding the Tower of Babel

Define a function, babel, which accepts a positive integer argument height and returns a string representing a tower of the specified height. If the height is 0 then return an empty string. Input validation is not required.

Some examples below:
```
Kata.Babel(0) => "";

Kata.Babel(1) => "o\n" +
                 "o\n" +
                 "o";

Kata.Babel(2) => " o\n"  +
                 " o\n"  +
                 " o\n"  +
                 "ooo\n" +
                 "ooo\n" +
                 "ooo";

Kata.Babel(3) => "  o\n"   +
                 "  o\n"   +
                 "  o\n"   +
                 " ooo\n"  +
                 " ooo\n"  +
                 " ooo\n"  +
                 "ooooo\n" +
                 "ooooo\n" +
                 "ooooo";

Kata.Babel(4) => "   o\n"    +
                 "   o\n"    +
                 "   o\n"    +
                 "  ooo\n"   +
                 "  ooo\n"   +
                 "  ooo\n"   +
                 " ooooo\n"  +
                 " ooooo\n"  +
                 " ooooo\n"  +
                 "ooooooo\n" +
                 "ooooooo\n" +
                 "ooooooo";

Kata.Babel(5) => "    o\n"     +
                 "    o\n"     +
                 "    o\n"     +
                 "   ooo\n"    +
                 "   ooo\n"    +
                 "   ooo\n"    +
                 "  ooooo\n"   +
                 "  ooooo\n"   +
                 "  ooooo\n"   +
                 " ooooooo\n"  +
                 " ooooooo\n"  +
                 " ooooooo\n"  +
                 "ooooooooo\n" +
                 "ooooooooo\n" +
                 "ooooooooo";
```
If you are still confused as to what the pattern is, here are a few simple rules:

* For each width of the tower you build three consecutive stories of the same width
* Each time you complete 3 stories, the width of the tower increases by 2 units (1 to the left and 1 to the right)
* You should add appropriate whitespace characters to the left of the tower for appropriate padding but there should be no trailing whitespace characters for all stories
* You separate one story from then next with a newline "\n" character
* There should not be a trailing newline character at the end of the string
