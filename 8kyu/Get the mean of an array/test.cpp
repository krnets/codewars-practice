#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <vector>
#include "solve.cpp"
#include "../../doctest.h"

TEST_CASE("testing array_average")
{
	SUBCASE("basic_test")
	{
		CHECK(get_average(std::vector <int>{2, 2, 2, 2}) == 2);
		CHECK(get_average(std::vector <int>{1, 5, 87, 45, 8, 8}) == 25);
		CHECK(get_average(std::vector <int>{2,5,13,20,16,16,10}) == 11);
		CHECK(get_average(std::vector <int>{1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7}) == 11);
	}
}
