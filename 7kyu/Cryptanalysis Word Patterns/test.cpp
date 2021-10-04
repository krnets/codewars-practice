#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Example_Tests")
{
	SUBCASE("should_pass_fixed_tests")
	{
		CHECK(wordPattern("") == "");
		CHECK(wordPattern("hello") == "0.1.2.2.3");
		CHECK(wordPattern("heLlo") == "0.1.2.2.3");
		CHECK(wordPattern("helLo") == "0.1.2.2.3");
		CHECK(wordPattern("Hippopotomonstrosesquippedaliophobia") == "0.1.2.2.3.2.3.4.3.5.3.6.7.4.8.3.7.9.7.10.11.1.2.2.9.12.13.14.1.3.2.0.3.15.1.13");
	}
}
