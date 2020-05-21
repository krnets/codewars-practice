# 6kyu - CamelCase to underscore

""" You wrote all your unit test names in camelCase. 
But some of your colleagues have troubles reading these long test names. 
So you make a compromise to switch to underscore separation.

To make these changes fast you wrote a class to translate a camelCase name into an underscore separated name.

Implement the ToUnderscore() method.

"ThisIsAUnitTest" => "This_Is_A_Unit_Test"

But of course there are always special cases...
You also have some calculation tests. Make sure the results don't get split by underscores. 
So only add an underscore in front of the first number.

Also Some people already used underscore names in their tests. You don't want to change them. 
But if they are not split correct you should adjust them.

Some of your colleagues mark their tests with a leading and trailing underscore. Don't remove this.
And of course you should handle empty strings to avoid unnecessary errors. Just return an empty string then.

"Calculate15Plus5Equals20" => "Calculate_15_Plus_5_Equals_20"
"This_Is_Already_Split_Correct" => "This_Is_Already_Split_Correct"
"ThisIs_Not_SplitCorrect" => "This_Is_Not_Split_Correct"
"_UnderscoreMarked_Test_Name_" => _Underscore_Marked_Test_Name_" """

import re

# def toUnderScore(name):
#     output = re.sub('([A-Z]|\d+)', r'_\1', name)
#     output = re.sub('^_', '', output)
#     output = re.sub('^__', '_', output)
#     output = re.sub('__', '_', output)
#     return output


def toUnderScore(name):
    return re.sub('([a-zA-Z](?=[A-Z\d])|\d(?=[A-Z]))', r'\1_', name)


# Tests_With_Simple_Names
q = toUnderScore("ThisIsAUnitTest")
q
#     "This_Is_A_Unit_Test"
q = toUnderScore("ThisShouldBeSplittedCorrectIntoUnderscore")
q
#      "This_Should_Be_Splitted_Correct_Into_Underscore"

# Tests_With_Numbers
q = toUnderScore("Calculate1Plus1Equals2")
q
#      "Calculate_1_Plus_1_Equals_2"
q = toUnderScore("Calculate15Plus5Equals20")
q
#      "Calculate_15_Plus_5_Equals_20"
q = toUnderScore(
    "Calculate500DividedBy5Equals100")
q
#     "Calculate_500_Divided_By_5_Equals_100"

# Tests_With_Special_Cases
q = toUnderScore(
    "This_Is_Already_Splitted_Correct")
#   "This_Is_Already_Splitted_Correct"
q
q = toUnderScore("ThisIs_Not_SplittedCorrect")
#      "This_Is_Not_Splitted_Correct"
q
q = toUnderScore(
    "_IfATestStartAndEndsWithUnderscore_ItShouldBeTheSame_")
q
#    "_If_A_Test_Start_And_Ends_With_Underscore_It_Should_Be_The_Same_"
