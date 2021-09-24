#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Cake_tests")
{
	SUBCASE("Basic_tests")
	{
        CHECK(cake(900, "abcdef") == "That was close!");
        CHECK(cake(56, "ifkhchlhfd") == "Fire!");
        CHECK(cake(256, "aaaaaddddr") == "Fire!");
    }
}
