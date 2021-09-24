#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing number of digits")
{
	SUBCASE("test_digits")
	{
        CHECK(digits(5ull) == 1);
        CHECK(digits(12345ull) == 5);
        CHECK(digits(9876543210ull) == 10);
    }
}
