#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing get_middle_algorithm")
{
	SUBCASE("should_handle_basic_tests")
	{
		CHECK(get_middle("test") == "es");
		CHECK(get_middle("testing") == "t");
	}
}
