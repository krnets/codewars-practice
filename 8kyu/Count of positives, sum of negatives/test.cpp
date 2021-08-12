#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing countPositiveSumNegatives")
{
	SUBCASE("Test1")
	{
		std::vector<int> input{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15};
		std::vector<int> result = countPositivesSumNegatives(input);
		std::vector<int> expected{10, -65};
		CHECK(result == expected);
	}

	SUBCASE("Test2")
	{
		std::vector<int> input{0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14};
		std::vector<int> result = countPositivesSumNegatives(input);
		std::vector<int> expected = {8, -50};
		CHECK(result == expected);
	}
}
