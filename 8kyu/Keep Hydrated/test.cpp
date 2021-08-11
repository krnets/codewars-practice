#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing keep hydrated function")
{
	SUBCASE("should_pass_sample_tests")
	{
		CHECK(litres(2) == 1);
		CHECK(litres(1.4) == 0);
		CHECK(litres(12.3) == 6);
		CHECK(litres(0.82) == 0);
		CHECK(litres(11.8) == 5);
		CHECK(litres(1787) == 893);
		CHECK(litres(0) == 0);
	}
}
