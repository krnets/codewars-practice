#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Basic_Tests")
{
	SUBCASE("Example_Tests")
	{
		CHECK(highestScoringWord("man i need a taxi up to ubud") == "taxi");
		CHECK(highestScoringWord("what time are we climbing up the volcano") == "volcano");
		CHECK(highestScoringWord("take me to semynak") == "semynak");
		CHECK(highestScoringWord("massage yes massage yes massage") == "massage");
		CHECK(highestScoringWord("take two bintang and a dance please") == "bintang");
		CHECK(highestScoringWord("aa b") == "aa");
	}
}
