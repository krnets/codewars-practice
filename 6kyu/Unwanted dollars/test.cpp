#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Unwanted_Dollars")
{
	double error_tolerance = 1e-9;

	SUBCASE("Easy_Tests")
	{
		CHECK(money_value("12.34") == doctest::Approx(12.34).epsilon(error_tolerance));
		CHECK(money_value("007") == doctest::Approx(7.00).epsilon(error_tolerance));
		CHECK(money_value("-0.89") == doctest::Approx(-0.89).epsilon(error_tolerance));
		CHECK(money_value("   .11") == doctest::Approx(0.11).epsilon(error_tolerance));
		CHECK(money_value("-.34") == doctest::Approx(-0.34).epsilon(error_tolerance));
	}
	SUBCASE("Harder_Tests")
	{
		CHECK(money_value(" $5.67") == doctest::Approx(5.67).epsilon(error_tolerance));
		CHECK(money_value("-$ 0.1") == doctest::Approx(-0.10).epsilon(error_tolerance));
		CHECK(money_value(" $ 89") == doctest::Approx(89.0).epsilon(error_tolerance));
		CHECK(money_value("$.2") == doctest::Approx(0.20).epsilon(error_tolerance));
		CHECK(money_value("$$$") == doctest::Approx(0.0).epsilon(error_tolerance));
		CHECK(money_value("$-2.3456") == doctest::Approx(-2.3456).epsilon(error_tolerance));
	}
}
