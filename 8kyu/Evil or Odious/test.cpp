#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing evil")
{
	SUBCASE("should_pass_sample_tests")
	{
		CHECK(evil(1) == "It's Odious!");
		CHECK(evil(2) == "It's Odious!");
		CHECK(evil(3) == "It's Evil!");
	}
}
