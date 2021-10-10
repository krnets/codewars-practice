#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testing(long long ans, long long sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing thirt_Tests")
{
	SUBCASE("Fixed_Tests")
	{
		testing(Thirteen::thirt(8529), 79);
		testing(Thirteen::thirt(85299258), 31);
		testing(Thirteen::thirt(5634), 57);
		testing(Thirteen::thirt(1111111111), 71);
		testing(Thirteen::thirt(987654321), 30);
	}
}
