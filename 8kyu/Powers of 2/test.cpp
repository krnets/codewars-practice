#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"
#include <vector>
#include <cstdint>

TEST_CASE("testing Fixed_tests")
{
	using V = std::vector<uint64_t>;

	SUBCASE("Sample_cases")
	{
		CHECK(powers_of_two(0) == V{1});
		CHECK(powers_of_two(2) == V{1, 2, 4});
		CHECK(powers_of_two(4) == V{1, 2, 4, 8, 16});
		CHECK(powers_of_two(10) == V{1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024});
	}
}
