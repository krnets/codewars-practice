#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing ")
{
	SUBCASE("ExampleTest1")
	{
		std::string expected = "b***i***t***c***o***i***n";
		std::string actual = twoSort({"bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"});

		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest2")
	{
		std::string expected = "a***r***e";
		std::string actual = twoSort({
			"turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"
		});

		CHECK(actual == expected);
	}
}
