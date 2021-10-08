#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(std::vector<std::string>& ans, std::vector<std::string>& sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing inArrayTests")
{
	SUBCASE("example test 1")
	{
		std::vector<std::string> arr1 = {"arp", "live", "strong"};
		std::vector<std::string> arr2 = {"lively", "alive", "harp", "sharp", "armstrong"};
		std::vector<std::string> sol1 = {"arp", "live", "strong"};

		std::vector<std::string> ans1 = WhichAreIn::inArray(arr1, arr2);
		testequal(ans1, sol1);
	}
	SUBCASE("example test 2")
	{
		std::vector<std::string> arr1 = {"tarp", "mice", "bull"};
		std::vector<std::string> arr2 = {"lively", "alive", "harp", "sharp", "armstrong"};
		std::vector<std::string> sol1 = {};

		std::vector<std::string> ans1 = WhichAreIn::inArray(arr1, arr2);
		testequal(ans1, sol1);
	}
}
