#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing DNA_to_RNA")
{
	SUBCASE("Sample_Test")
	{
		CHECK(DNAtoRNA("GCAT") == "GCAU");
		CHECK(DNAtoRNA("TGCAT") == "UGCAU");
		CHECK(DNAtoRNA("GTCAT") == "GUCAU");
		CHECK(DNAtoRNA("GCATT") == "GCAUU");
	}
}
