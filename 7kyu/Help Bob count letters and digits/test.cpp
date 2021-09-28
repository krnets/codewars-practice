#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing countLettersAndDigits")
{
	SUBCASE("ExampleTests")
	{
		CHECK(countLettersAndDigits("n!!ic_e!!123") == 7);
	}
}
