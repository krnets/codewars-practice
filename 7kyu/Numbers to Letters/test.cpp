#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Fixed_tests")
{
	SUBCASE("Sample_cases")
	{
		CHECK(switcher(std::vector<std::string>{"24", "12", "23", "22", "4", "26", "9", "8"}) == "codewars");
		CHECK(switcher(std::vector<std::string>{ "25", "7", "8", "4", "14", "23", "8", "25", "23", "29", "16", "16", "4"
			}) == "btswmdsbd kkw");
		CHECK(switcher(std::vector<std::string>{"4", "24"}) == "wc");
		CHECK(switcher(std::vector<std::string>{"12"}) == "o");
		CHECK(switcher(std::vector<std::string>{"12", "28", "25", "21", "25", "7", "11", "22", "15"}) == "o?bfbtpel");
	}
}
