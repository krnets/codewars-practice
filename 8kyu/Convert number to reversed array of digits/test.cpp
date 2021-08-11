#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing digitize_method")
{
	SUBCASE("basic_tests")
	{
		CHECK(digitize(35231) == std::vector<int> {1, 3, 2, 5, 3});
		CHECK(digitize(23582357) == std::vector<int>{7, 5, 3, 2, 8, 5, 3, 2});
		CHECK(digitize(984764738) == std::vector<int>{8, 3, 7, 4, 6, 7, 4, 8, 9});
		CHECK(digitize(45762893920) == std::vector<int>{0, 2, 9, 3, 9, 8, 2, 6, 7, 5, 4});
		CHECK(digitize(548702838394) == std::vector<int>{4, 9, 3, 8, 3, 8, 2, 0, 7, 8, 4, 5});
	}
}
