#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing gps")
{
	SUBCASE("sample test")
	{
		std::vector<double> x = {0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25};
		CHECK(GpsSpeed::gps(15, x) == 74);

		x = {0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25};
		CHECK(GpsSpeed::gps(12, x) == 219);

		x = {0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61};
		CHECK(GpsSpeed::gps(20, x) == 41);
	}
}
