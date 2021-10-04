#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Fixed_tests")
{
	SUBCASE("Should_fail")
	{
		CHECK(well(std::vector{
			std::vector<std::string>{"bad", "bAd", "bad"},
			std::vector<std::string>{"bad", "bAd", "bad"},
			std::vector<std::string>{"bad", "bAd", "bad"},
			}) == "Fail!");
	}
	SUBCASE("Should_publish")
	{
		CHECK(well(std::vector{
			std::vector<std::string>{"gOOd", "bad", "BAD", "bad", "bad"},
			std::vector<std::string>{"bad", "bAd", "bad"},
			std::vector<std::string>{"GOOD", "bad", "bad", "bAd"},
			}) == "Publish!");
	}
	SUBCASE("Should_smell_a_series")
	{
		CHECK(well(std::vector{
			std::vector<std::string>{"gOOd", "bAd", "BAD", "bad", "bad", "GOOD"},
			std::vector<std::string>{"bad"},
			std::vector<std::string>{"gOOd", "BAD"},
			}) == "I smell a series!");
	}
}
