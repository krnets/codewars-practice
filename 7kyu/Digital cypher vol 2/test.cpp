#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sample_tests")
{
	SUBCASE("test1")
	{
		CHECK(Kata::Decode(vector<int>({20, 12, 18, 30, 21}), 1939) == "scout");
	}
	SUBCASE("test2")
	{
		CHECK(Kata::Decode(std::vector<int>({14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8}), 1939) == "masterpiece");
	}
}
