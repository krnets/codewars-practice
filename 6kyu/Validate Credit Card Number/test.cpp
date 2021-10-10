#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing validate_function")
{
	SUBCASE("basic_tests")
	{
        CHECK(Kata::validate(891) == false);
        CHECK(Kata::validate(2121) == true);
    }
}
