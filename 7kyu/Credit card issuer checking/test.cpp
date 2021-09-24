#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing basic_tests")
{
	SUBCASE("simple_tests")
	{
		CHECK(getIssuer("4111111111111111") == "VISA");
		CHECK(getIssuer("4111111111111") == "VISA");
		CHECK(getIssuer("348282246310005") == "AMEX");
		CHECK(getIssuer("378282246310005") == "AMEX");
		CHECK(getIssuer("9111111111111111") == "Unknown");
		CHECK(getIssuer("4012888888881881") == "VISA");
		CHECK(getIssuer("6011111111111117") == "Discover");
		CHECK(getIssuer("5105105105105100") == "Mastercard");
		CHECK(getIssuer("5205105105105106") == "Mastercard");
		CHECK(getIssuer("5305105105105106") == "Mastercard");
		CHECK(getIssuer("5405105105105106") == "Mastercard");
		CHECK(getIssuer("5505105105105106") == "Mastercard");
	}
}
