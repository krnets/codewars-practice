#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing cleanString_test")
{
	SUBCASE("Sample_Test")
	{
        CHECK(cleanString("abc#d##c") == "ac");
        CHECK(cleanString("abc####d##c#") == "");
    }
}
