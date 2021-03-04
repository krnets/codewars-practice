### Moves in squared strings (IV)

You are given a string of n lines, each substring being n characters long: 

For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study some transformations of this square of strings.

Symmetry with respect to the main cross diagonal: Diag2Sym
```
           s  =  "abcd\nefgh\nijkl\nmnop"
diag_2_sym(s) => "plhd\nokgc\nnjfb\nmiea"

abcd
efgh
ijkl
mnop

    plhd
    okgc
    njfb
    miea
```
Counterclockwise rotation 90 degrees: Rot90Counter
```
               s  =  "abcd\nefgh\nijkl\nmnop"
rot_90_counter(s) => "dhlp\ncgko\nbfjn\naeim"

    dhlp
    cgko
    bfjn
    aeim"
```
SelfieDiag2Counterclock 

It is initial string + string obtained by symmetry with respect to the main cross diagonal + counterclockwise rotation 90 degrees .
```
s = "abcd\nefgh\nijkl\nmnop" --> 
    "abcd|plhd|dhlp\nefgh|okgc|cgko\nijkl|njfb|bfjn\nmnop|miea|aeim"

    or printed for the last:

    abcd|plhd|dhlp
    efgh|okgc|cgko
    ijkl|njfb|bfjn
    mnop|miea|aeim
```
Task:

Write these functions Diag2Sym, Rot90Counter, SelfieDiag2Counterclock

and

* high-order function oper(fct, s) where

* fct is the function of one variable f to apply to the string s (fct will be one of Diag2sym, Rot90Counter, SelfieDiag2Counterclock)

Examples:
```
s = "abcd\nefgh\nijkl\nmnop"
oper(diag_2_sym, s) => "plhd\nokgc\nnjfb\nmiea"
oper(rot_90_counter, s) => "dhlp\ncgko\nbfjn\naeim"
oper(selfie_diag2_counterclock, s) => "abcd|plhd|dhlp\nefgh|okgc|cgko\nijkl|njfb|bfjn\nmnop|miea|aeim"
```
Notes:

* The form of the parameter fct in oper changes according to the language.
* It could be easier to take these katas from number (I) to number (IV)
