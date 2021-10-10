#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	using iv = std::vector<int>;
	using ivv = std::vector<iv>;

	SUBCASE("BasicTests")
	{
		CHECK(pyramid(0) == ivv{});
		CHECK(pyramid(1) == ivv{iv{1}});
		CHECK(pyramid(2) == ivv{iv{1}, iv{1, 1}});
		CHECK(pyramid(3) == ivv{iv{1}, iv{1, 1}, iv{1, 1, 1}});
	}
}
