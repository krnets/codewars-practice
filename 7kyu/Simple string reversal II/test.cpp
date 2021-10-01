#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple_String_Reversal_2")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve("codewars", 1, 5) == "cawedors");
		CHECK(solve("codingIsFun", 2, 100) == "conuFsIgnid");
		CHECK(solve("FunctionalProgramming", 2, 15) == "FuargorPlanoitcnmming");
		CHECK(solve("abcefghijklmnopqrstuvwxyz", 0, 20) == "vutsrqponmlkjihgfecbawxyz");
		CHECK(solve("abcefghijklmnopqrstuvwxyz", 5, 20) == "abcefvutsrqponmlkjihgwxyz");
	}
}
