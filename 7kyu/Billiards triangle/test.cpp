#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Example_Cases")
{
	SUBCASE("should_pass_the_tests")
	{
		CHECK(pyramid(1) == 1);
		CHECK(pyramid(2) == 1);

		CHECK(pyramid(3) == 2);
		CHECK(pyramid(4) == 2);
		CHECK(pyramid(5) == 2);

		CHECK(pyramid(6) == 3);
		CHECK(pyramid(7) == 3);
		CHECK(pyramid(8) == 3);
		CHECK(pyramid(9) == 3);

		CHECK(pyramid(10) == 4);
		CHECK(pyramid(11) == 4);
		CHECK(pyramid(12) == 4);
		CHECK(pyramid(13) == 4);
		CHECK(pyramid(14) == 4);

		CHECK(pyramid(15) == 5);
		CHECK(pyramid(16) == 5);
		CHECK(pyramid(17) == 5);
		CHECK(pyramid(18) == 5);
		CHECK(pyramid(19) == 5);
		CHECK(pyramid(20) == 5);

		CHECK(pyramid(21) == 6);
		CHECK(pyramid(22) == 6);
		CHECK(pyramid(23) == 6);
		CHECK(pyramid(24) == 6);
		CHECK(pyramid(25) == 6);
		CHECK(pyramid(26) == 6);
		CHECK(pyramid(27) == 6);

		CHECK(pyramid(28) == 7);
		CHECK(pyramid(29) == 7);
		CHECK(pyramid(30) == 7);
		CHECK(pyramid(31) == 7);
		CHECK(pyramid(32) == 7);
		CHECK(pyramid(33) == 7);
		CHECK(pyramid(34) == 7);
		CHECK(pyramid(35) == 7);


		CHECK(pyramid(100) == 13);
		CHECK(pyramid(9999) == 140);
	}
}
