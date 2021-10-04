#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing DNAStrand")
{
	SUBCASE("BasicTests")
	{
		CHECK(DNAStrand("AAAA") == "TTTT");
		CHECK(DNAStrand("ATTGC") == "TAACG");
		CHECK(DNAStrand("GTAT") == "CATA");
	}
}
