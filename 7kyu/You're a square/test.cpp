#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing is_square_function")
{
	SUBCASE("should_work_for_basic_tests")
	{
		CHECK(is_square(-1) == false);
		CHECK(is_square(0) == true);
		CHECK(is_square(3) == false);
		CHECK(is_square(4) == true);
		CHECK(is_square(25) == true);
		CHECK(is_square(26) == false);
	}
}
