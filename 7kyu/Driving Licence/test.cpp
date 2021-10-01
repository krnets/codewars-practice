#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sample_tests")
{
	SUBCASE("basic_tests")
	{
		CHECK(driver({"John", "James", "Smith", "01-Jan-2000", "M"}) == "SMITH001010JJ9AA");
		CHECK(driver({"Johanna", "", "Gibbs", "13-Dec-1981", "F"}) == "GIBBS862131J99AA");
		CHECK(driver({"Andrew", "Robert", "Lee", "02-September-1981", "M"}) == "LEE99809021AR9AA");
	}
}
