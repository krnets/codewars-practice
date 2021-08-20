#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing The_isPalindrom_function")
{
	SUBCASE("should_work_for_some_examples")
	{
		CHECK(isPalindrom("a") == true);
		CHECK(isPalindrom("aba") == true);
		CHECK(isPalindrom("Abba") == true);
		CHECK(isPalindrom("hello") == false);
	}
}
