#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing to_camel_case")
{
	SUBCASE("Basic_tests")
	{
		CHECK(to_camel_case("") == "");
		CHECK(to_camel_case("the_stealth_warrior") == "theStealthWarrior");
		CHECK(to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior");
		CHECK(to_camel_case("A-B-C") == "ABC");
	}
}
