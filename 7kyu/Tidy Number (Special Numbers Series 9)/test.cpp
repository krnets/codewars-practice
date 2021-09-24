#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Tidy_Number_Tests")
{
	SUBCASE("Check_Small_Values")
	{
		CHECK(tidyNumber(12) == true);
		CHECK(tidyNumber(32) == false);
		CHECK(tidyNumber(39) == true);
	}
	SUBCASE("Check_Larger_Values")
	{
		CHECK(tidyNumber(1024) == false);
		CHECK(tidyNumber(12576) == false);
		CHECK(tidyNumber(13579) == true);
	}
}
