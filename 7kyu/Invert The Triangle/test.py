import codewars_test as test
from kata import invert_triangle, maketri


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        unsolved = [
            "           ##           \n          ####          \n         ######         \n        ########        \n       ##########       \n      ############      \n     ##############     \n    ################    \n   ##################   \n  ####################  \n ###################### \n########################\n",
            "  #  \n ### \n#####\n",
            "   ##   \n  ####  \n ###### \n########\n",
            "###  ###\n##    ##\n#      #\n        \n",
            "        #        \n       ###       \n      #####      \n     #######     \n    #########    \n   ###########   \n  #############  \n ############### \n#################\n",
            "#####  #####\n####    ####\n###      ###\n##        ##\n#          #\n            \n",
            "     ##     \n    ####    \n   ######   \n  ########  \n ########## \n############\n",
            "       ##       \n      ####      \n     ######     \n    ########    \n   ##########   \n  ############  \n ############## \n################\n",
            "#############  #############\n############    ############\n###########      ###########\n##########        ##########\n#########          #########\n########            ########\n#######              #######\n######                ######\n#####                  #####\n####                    ####\n###                      ###\n##                        ##\n#                          #\n                            \n",
        ]

        solved = [
            "\n                        \n#                      #\n##                    ##\n###                  ###\n####                ####\n#####              #####\n######            ######\n#######          #######\n########        ########\n#########      #########\n##########    ##########\n###########  ###########",
            "\n     \n#   #\n## ##",
            "\n        \n#      #\n##    ##\n###  ###",
            "\n########\n ###### \n  ####  \n   ##   ",
            "\n                 \n#               #\n##             ##\n###           ###\n####         ####\n#####       #####\n######     ######\n#######   #######\n######## ########",
            "\n############\n ########## \n  ########  \n   ######   \n    ####    \n     ##     ",
            "\n            \n#          #\n##        ##\n###      ###\n####    ####\n#####  #####",
            "\n                \n#              #\n##            ##\n###          ###\n####        ####\n#####      #####\n######    ######\n#######  #######",
            "\n############################\n ########################## \n  ########################  \n   ######################   \n    ####################    \n     ##################     \n      ################      \n       ##############       \n        ############        \n         ##########         \n          ########          \n           ######           \n            ####            \n             ##             ",
        ]

        for n, i in enumerate(unsolved):
            test.assert_equals(invert_triangle(i), solved[n])


@test.describe("Random Tests")
def random_tests():
    from random import randrange

    def invert_triB(t):
        def invc(c):
            if c == " ":
                c = "#"
            elif c == "#":
                c = " "
            return c

        l = len(t)
        for z, i in enumerate(t):
            if i == "\n":
                s = z
                break
        r = []
        first = True
        for z, i in enumerate(t):
            r += [invc(t[(l - 1) - z])]
            if first == False and z % s == 0 and z != l - 1:
                r += "\n"
            if first == True:
                first == False
        return "".join(r)

    for k in range(30):
        t = maketri(randrange(3, 15))
        x = t

        @test.it(f"triangle :\n{x}")
        def basic_test_cases():
            test.assert_equals(invert_triangle(t), invert_triB(t))
