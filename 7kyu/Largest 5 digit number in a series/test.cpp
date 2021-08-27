#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing LargestFiveDigitNumberTest")
{
	SUBCASE("ExampleTests")
	{
		CHECK(largest_five_digits("283910") == 83910);
		CHECK(largest_five_digits("1234567890") == 67890);
	}
}
