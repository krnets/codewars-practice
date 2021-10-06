#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ShouldPassAllTheTestsProvided")
{
	SUBCASE("Test1")
	{
		vector<int> numbers{1, 2, 3, 4, 3, 2, 1};
		int expected = 3;
		CHECK(find_even_index(numbers) == expected);
	}

	SUBCASE("Test2")
	{
		vector<int> numbers{1, 100, 50, -51, 1, 1};
		int expected = 1;
		CHECK(find_even_index(numbers) == expected);
	}

	SUBCASE("Test3")
	{
		vector<int> numbers{1, 2, 3, 4, 5, 6};
		int expected = -1;
		CHECK(find_even_index(numbers) == expected);
	}

	SUBCASE("Test4")
	{
		vector<int> numbers{20, 10, 30, 10, 10, 15, 35};
		int expected = 3;
		CHECK(find_even_index(numbers) == expected);
	}

	SUBCASE("Test5")
	{
		vector<int> numbers{20, 10, -80, 10, 10, 15, 35};
		int expected = 0;
		CHECK(find_even_index(numbers) == expected);
	}

	SUBCASE("Test6")
	{
		vector<int> numbers{10, -80, 10, 10, 15, 35, 20};
		int expected = 6;
		CHECK(find_even_index(numbers) == expected);
	}

	SUBCASE("Test7")
	{
		vector<int> numbers{0, 0, 0, 0, 0};
		int expected = 0;
		CHECK(find_even_index(numbers) == expected);
	}

	SUBCASE("Test8")
	{
		vector<int> numbers{-1, -2, -3, -4, -3, -2, -1};
		int expected = 3;
		CHECK(find_even_index(numbers) == expected);
	}
}
