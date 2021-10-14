#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void doTest(int expected, const string& town)
{
	CHECK(countDeafRats(town) == expected);
}

TEST_CASE("testing ExampleTests")
{
	SUBCASE("Example 1")
	{
		doTest(0, "~O~O~O~O P");
	}
	SUBCASE("Example 2")
	{
		doTest(1, "P O~ O~ ~O O~");
	}
	SUBCASE("Example 3")
	{
		doTest(2, "~O~O~O~OP~O~OO~");
	}
}
