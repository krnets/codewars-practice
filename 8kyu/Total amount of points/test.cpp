#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <array>
#include <string>
#include "solve.cpp"
#include "../../doctest.h"

TEST_CASE("testing points")
{
	SUBCASE("Sample_tests")
	{
		int r;
		r = points(std::array<std::string, 10>{"1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"});
		CHECK(r == 30);

		r = points(std::array<std::string, 10>{"1:1", "2:2", "3:3", "4:4", "2:2", "3:3", "4:4", "3:3", "4:4", "4:4"});
		CHECK(r == 10);

		r = points(std::array<std::string, 10>{"0:1", "0:2", "0:3", "0:4", "1:2", "1:3", "1:4", "2:3", "2:4", "3:4"});
		CHECK(r == 0);

		r = points(std::array<std::string, 10>{"1:0", "2:0", "3:0", "4:0", "2:1", "1:3", "1:4", "2:3", "2:4", "3:4"});
		CHECK(r == 15);

		r = points(std::array<std::string, 10>{"1:0", "2:0", "3:0", "4:4", "2:2", "3:3", "1:4", "2:3", "2:4", "3:4"});
		CHECK(r == 12);
	}
}
