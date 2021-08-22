#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"
#include <vector>

TEST_CASE("testing SampleTests")
{
	SUBCASE("should_pass_sample_tests")
	{
		using v = std::vector<int>;

		CHECK(flip('R', { 3, 2, 1, 2 }) == v{ 1, 2, 2, 3 });
		CHECK(flip('L', { 1, 4, 5, 3, 5 }) == v{ 5, 5, 4, 3, 1 });
	}
}
