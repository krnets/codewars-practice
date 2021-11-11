#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Remove the parentheses")
{
	SUBCASE("Test 1")
	{
		CHECK(remove_parentheses("example(unwanted thing)example") == "exampleexample");
	}
	SUBCASE("Test 2")
	{
		CHECK(remove_parentheses("example(unwanted thing)example") == "exampleexample");
	}
	SUBCASE("Test 3")
	{
		CHECK(remove_parentheses("example (unwanted thing) example") == "example  example");
	}
	SUBCASE("Test 4")
	{
		CHECK(remove_parentheses("a (bc d)e") == "a e");
	}
	SUBCASE("Test 5")
	{
		CHECK(remove_parentheses("a(b(c))") == "a");
	}
	SUBCASE("Test 6")
	{
		CHECK(remove_parentheses("hello example (words(more words) here) something") == "hello example  something");
	}
	SUBCASE("Test 7")
	{
		CHECK(remove_parentheses("(first group) (second group) (third group)") == "  ");
	}
}
