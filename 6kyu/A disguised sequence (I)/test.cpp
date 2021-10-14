#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(unsigned long long ans, unsigned long long sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing HiddenSeq_fcn_Tests")
{
	SUBCASE("test1")
	{
		testequal(HiddenSeq::fcn(17), 131072);
		testequal(HiddenSeq::fcn(21), 2097152);
		testequal(HiddenSeq::fcn(14), 16384);
		testequal(HiddenSeq::fcn(43), 8796093022208);
	}
}
