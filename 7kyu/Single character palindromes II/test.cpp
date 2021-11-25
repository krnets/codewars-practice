#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Single_character_palindromes")
{
	SUBCASE("Tests true")
	{
		CHECK(solve("ab") == true);
		CHECK(solve("abbx") == true);
		CHECK(solve("abbaa") == true);
		CHECK(solve("abcba") == true);
	}
	SUBCASE("Tests false")
	{
		CHECK(solve("aa") == false);
		CHECK(solve("abba") == false);
	}
}
