#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple string division II")
{
	SUBCASE("sample_test")
	{
		CHECK_EQ(solve("1 2 36 4 8", 3), 8);
		// ['12', '18', '21', '24', '42', '48', '81', '84']
		// all divisible by 3.   

		CHECK_EQ(solve("1 3 6 3", 3), 6);
		// ['36', '33', '63', '63', '33', '36']

		CHECK_EQ(solve("1 2 36 4 8", 2), 16);
		CHECK_EQ(solve("1 2 36 4 8", 4), 11);
		CHECK_EQ(solve("1 2 36 4 8", 8), 4);
	}
}
