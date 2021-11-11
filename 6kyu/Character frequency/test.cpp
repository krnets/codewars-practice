#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Character frequency")
{
	SUBCASE("SampleTest")
		{
		CHECK(letter_frequency("aaAabb dddDD hhcc") == list_t{{'d', 5}, {'a', 4}, {'b', 2}, {'c', 2}, {'h', 2}});
	}
}
