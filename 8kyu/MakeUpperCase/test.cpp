#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing makeUpperCase_function")
{
	SUBCASE("example test")
	{
		CHECK(makeUpperCase("hello") == "HELLO");
		CHECK(makeUpperCase("hello world") == "HELLO WORLD");
		CHECK(makeUpperCase("hello world !") == "HELLO WORLD !");
		CHECK(makeUpperCase("HelLO wOrld !") == "HELLO WORLD !");
		CHECK(makeUpperCase("1,2,3 hello world!") == "1,2,3 HELLO WORLD!");
	}
}
