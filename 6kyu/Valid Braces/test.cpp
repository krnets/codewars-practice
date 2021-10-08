#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing valid_braces_algorithm")
{
	SUBCASE("invalid")
	{
		CHECK(valid_braces("[(])") == false);
		CHECK(valid_braces("(}")== false);
		CHECK(valid_braces( "[({})](]")== false);
	}
	SUBCASE("valid")
	{
		CHECK(valid_braces("()") == true);
		CHECK(valid_braces("(){}[]") == true);
		CHECK(valid_braces("([{}])") == true);
	}
}
