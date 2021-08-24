#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing isogram")
{
	SUBCASE("isogram_or_not")
	{
		CHECK(is_isogram("Dermatoglyphics") == true);
		CHECK(is_isogram("moose") == false);
		CHECK(is_isogram("isIsogram") == false);
	}
}
