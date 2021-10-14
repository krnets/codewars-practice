#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

using std::string;

TEST_CASE("testing Suite2Test")
{
	SUBCASE("test1")
	{
		CHECK(Suite2::game(0) == "[0]");
	}
	SUBCASE("test2")
	{
		CHECK(Suite2::game(1) == "[1, 2]");
	}
	SUBCASE("test3")
	{
		CHECK(Suite2::game(8) == "[32]");
	}
	SUBCASE("test4")
	{
		CHECK(Suite2::game(40) == "[800]");
	}
	SUBCASE("test5")
	{
		CHECK(Suite2::game(101) == "[10201, 2]");
	}
	SUBCASE("test6")
	{
		CHECK(Suite2::game(204) == "[20808]");
	}
	SUBCASE("test7")
	{
		CHECK(Suite2::game(807) == "[651249, 2]");
	}
	SUBCASE("test8")
	{
		CHECK(Suite2::game(1808) == "[1634432]");
	}
	SUBCASE("test9")
	{
		CHECK(Suite2::game(5014) == "[12570098]");
	}
	SUBCASE("test10")
	{
		CHECK(Suite2::game(120000) == "[7200000000]");
	}
	SUBCASE("test11")
	{
		CHECK(Suite2::game(750000) == "[281250000000]");
	}
	SUBCASE("test12")
	{
		CHECK(Suite2::game(750001) == "[562501500001, 2]");
	}
	SUBCASE("test13")
	{
		CHECK(Suite2::game(3000000) == "[4500000000000]");
	}
	SUBCASE("test14")
	{
		CHECK(Suite2::game(3000001) == "[9000006000001, 2]");
	}
}
