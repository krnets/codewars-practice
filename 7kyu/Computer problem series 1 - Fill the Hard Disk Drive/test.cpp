#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing SavingFiles")
{
	using vec = std::vector<int>;

	SUBCASE("FixedTests")
	{
		CHECK(save(vec{4, 4, 4, 3, 3}, 12) == 3);
		CHECK(save(vec{4, 4, 4, 3, 3}, 11) == 2);
		CHECK(save(vec{4, 8, 15, 16, 23, 42}, 108) == 6);
		CHECK(save(vec{13}, 13) == 1);
		CHECK(save(vec{1, 2, 3, 4}, 250) == 4);
		CHECK(save(vec{100}, 500) == 1);
		CHECK(save(vec{11, 13, 15, 17, 19}, 8) == 0);
		CHECK(save(vec{45}, 12) == 0);
	}
}
