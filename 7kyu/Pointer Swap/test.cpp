#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing pointer_swap")
{
	SUBCASE("should_swap_the_pointers")
	{
		void* left = new int[0];
		void* right = new int[0];
		void* oldLeft = left;
		void* oldRight = right;
		::swap(left, right);
		CHECK_EQ(left, oldRight);
		CHECK_EQ(right, oldLeft);
	}
}
