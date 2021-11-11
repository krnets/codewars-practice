#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sortTheInnerContent")
{
	char const* input;
	std::string expected;

	SUBCASE("Test 1")
	{
		input =    "sort the inner content in descending order";
		expected = "srot the inner ctonnet in dsnnieedcg oredr";
		CHECK(sortTheInnerContent(input, strlen(input)) == expected);
	}
	SUBCASE("Test 2")
	{
		input =    "wait for me";
		expected = "wiat for me";
		CHECK(sortTheInnerContent (input, strlen (input)) == expected);
	}
	SUBCASE("Test 3")
	{
		input =    "this kata is easy";
		expected = "tihs ktaa is esay";
		CHECK(sortTheInnerContent (input, strlen (input)) == expected);
	}
}
