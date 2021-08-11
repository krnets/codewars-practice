#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing basic_op_samples")
{
	SUBCASE("basic_tests")
	{
		CHECK(basicOp('+',5,4) == 9);
		CHECK(basicOp('-',11,8) == 3);
		CHECK(basicOp('*',3,4) == 12);
		CHECK(basicOp('/',16,4) == 4);
	}
}
