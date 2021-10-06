#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing basic_tests")
{
	SUBCASE("test1")
	{
		CHECK(narcissistic(7) == true);
	}
	SUBCASE("test2")
	{
		CHECK(narcissistic(371) == true);
	}
	SUBCASE("test3")
	{
		CHECK(narcissistic(122) == false);
	}
	SUBCASE("test4")
	{
		CHECK(narcissistic(4887) == false);
	}
}
