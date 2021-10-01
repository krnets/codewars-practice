#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Disgruntled_Employee")
{
	SUBCASE("Sample_Test")
	{
		CHECK(projectPartners(2) == 1);
		CHECK(projectPartners(3) == 3);
		CHECK(projectPartners(4) == 6);
		CHECK(projectPartners(5) == 10);
	}
}
