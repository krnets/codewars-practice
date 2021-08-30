#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sumTriangularNumbers")
{
	SUBCASE("should_pass_all_example_tests")
	{
		CHECK(sumTriangularNumbers(1) == 1);
		CHECK(sumTriangularNumbers(2) == 4);
		CHECK(sumTriangularNumbers(3) == 10);
		CHECK(sumTriangularNumbers(4) == 20);
		CHECK(sumTriangularNumbers(5) == 35);
		CHECK(sumTriangularNumbers(6) == 56);
		CHECK(sumTriangularNumbers(7) == 84);
		CHECK(sumTriangularNumbers(8) == 120);
		CHECK(sumTriangularNumbers(9) == 165);
		CHECK(sumTriangularNumbers(10) == 220);
		CHECK(sumTriangularNumbers(34) == 7140);
		CHECK(sumTriangularNumbers(-291) == 0);
		CHECK(sumTriangularNumbers(943) == 140205240);
		CHECK(sumTriangularNumbers(-971) == 0);
	}
}
