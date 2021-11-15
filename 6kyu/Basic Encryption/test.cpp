#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing basic_encryption")
{
	SUBCASE("basic_test")
	{
		CHECK(encrypt("",1) == "");
		CHECK(encrypt("a",1) == "b");
		CHECK(encrypt("please encrypt me",2) == "rngcug\"gpet{rv\"og");
	}
}
