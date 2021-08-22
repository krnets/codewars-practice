#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing bonus_time")
{
	SUBCASE("ExampleTests")
	{
		CHECK(bonus_time(10000, true) == "$100000");
		CHECK(bonus_time(25000, true) == "$250000");
		CHECK(bonus_time(10000, false) == "$10000");
		CHECK(bonus_time(60000, false) == "$60000");
		CHECK(bonus_time(2, true) == "$20");
		CHECK(bonus_time(78, false) == "$78");
		CHECK(bonus_time(67890, true) == "$678900");
	}
}
