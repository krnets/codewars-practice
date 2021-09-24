#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing capitalize_function")
{
	SUBCASE("basic_tests")
	{
		CHECK(capitalize("abcdef", {1, 2, 5}) == "aBCdeF");
		CHECK(capitalize("abcdef", {1, 2, 100, 5}) == "aBCdeF");
		CHECK(capitalize("codewars", {1, 3, 5, 50}) == "cOdEwArs");
		CHECK(capitalize("abracadabra", {2, 6, 9, 10}) == "abRacaDabRA");
		CHECK(capitalize("codewarriors", {5}) == "codewArriors");
		CHECK(capitalize("indexinglessons", {0}) == "Indexinglessons");
	}
}
