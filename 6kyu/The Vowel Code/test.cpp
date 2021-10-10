#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sample_Tests")
{
	SUBCASE("encode")
	{
		CHECK(encode("hello") == "h2ll4");
		CHECK(encode("How are you today?") == "H4w 1r2 y45 t4d1y?");
		CHECK(encode("This is an encoding test.") == "Th3s 3s 1n 2nc4d3ng t2st.");
	}
	SUBCASE("decode")
	{
		CHECK(decode("h2ll4") == "hello");
		CHECK(decode("H4w 1r2 y45 t4d1y?") == "How are you today?");
		CHECK(decode("Th3s 3s 1n 2nc4d3ng t2st.") == "This is an encoding test.");
	}
}
