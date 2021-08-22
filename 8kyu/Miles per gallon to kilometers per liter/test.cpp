#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing converter")
{
	SUBCASE("ExampleTests")
	{
		// CHECK(converter(12) == 4.25);
		// CHECK(converter(24) == 8.50);
		CHECK(converter(36) == 12.74);
	}
}
