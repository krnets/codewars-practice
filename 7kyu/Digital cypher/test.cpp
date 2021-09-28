#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sample_tests")
{
	SUBCASE("test1")
	{
		CHECK(Kata::Encode("scout", 1939) == std::vector({20, 12, 18, 30, 21}));
	}

	SUBCASE("test2")
	{
		CHECK(Kata::Encode("masterpiece", 1939) == std::vector({14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8}));
	}
}
