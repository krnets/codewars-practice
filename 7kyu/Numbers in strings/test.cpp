#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Numbers_in_strings")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve("gh12cdy695m1") == 695);
		CHECK(solve("2ti9iei7qhr5") == 9);
		CHECK(solve("lu1j8qbbb85") == 85);
		CHECK(solve("185lu1j8qbbb85") == 185);
	}
}
