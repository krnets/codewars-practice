#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing SequenceSum")
{
	SUBCASE("simple sum")
	{
		SequenceSum seqsum(6);
		CHECK(seqsum.showSequence() == "0+1+2+3+4+5+6 = 21");
	}
}
