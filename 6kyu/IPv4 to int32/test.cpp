#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	SUBCASE("should_pass_sample_tests")
	{
        CHECK(ip_to_int32("128.32.10.1") == 2149583361);
    }
}
