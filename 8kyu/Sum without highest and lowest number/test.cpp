#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing ExampleTests")
{
	SUBCASE("test1")
	{
		CHECK(sum({ 6, 2, 1, 8, 10 }) == 16);
		CHECK(sum({ 1, 1, 11, 2, 3 }) == 6);
	}
}
