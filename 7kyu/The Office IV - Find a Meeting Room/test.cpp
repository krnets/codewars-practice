#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sample_tests")
{
	SUBCASE("Open_at_the_middle")
	{
		CHECK(meeting(std::vector<char>{'X', 'O', 'X'}) == 1);
	}
	SUBCASE("Open_at_the_start")
	{
		CHECK(meeting(std::vector<char>{'O', 'X', 'X', 'X', 'X'}) == 0);
	}
	SUBCASE("Open_at_the_end")
	{
		CHECK(meeting(std::vector<char>{'X', 'X', 'X', 'O'}) == 3);
	}
	SUBCASE("Noone_open")
	{
		CHECK(meeting(std::vector<char>{'X', 'X', 'X', 'X', 'X'}) == -1);
	}
}
