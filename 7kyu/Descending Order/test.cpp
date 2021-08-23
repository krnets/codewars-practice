#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing descendingOrder")
{
	SUBCASE("should_work_on_several_examples")
	{
		CHECK(descendingOrder(0) == 0);
		CHECK(descendingOrder(1) == 1);
		CHECK(descendingOrder(15) == 51);
		CHECK(descendingOrder(1021) == 2110);
		CHECK(descendingOrder(123456789) == 987654321);
	}
}
