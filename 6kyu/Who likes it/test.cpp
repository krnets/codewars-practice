#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sample_tests")
{
	SUBCASE("should_return_correct_text")
	{
		CHECK(likes({}) == "no one likes this");
		CHECK(likes({"Peter"}) == "Peter likes this");
		CHECK(likes({"Jacob", "Alex"}) == "Jacob and Alex like this");
		CHECK(likes({"Max", "John", "Mark"}) == "Max, John and Mark like this");
		CHECK(likes({"Alex", "Jacob", "Mark", "Max"}) == "Alex, Jacob and 2 others like this");
	}
}
