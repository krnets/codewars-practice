#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Swap Case Using N")
{
	SUBCASE("Basic_cases")
	{
		CHECK(swapp("Hello world!", 11) == "heLLO wORLd!");
		CHECK(swapp("the quick broWn fox leapt over the fence", 9) == "The QUicK BrowN foX LeaPT ovER thE FenCE");
		CHECK(swapp("eVerybody likes ice cReam", 85) == "EVErYbODy LiKeS IcE creAM");
		CHECK(swapp("gOOd MOrniNg", 7864) == "GooD MorNIng");
		CHECK(swapp("how are you today?", 12345) == "HOw are yoU TOdaY?");
	}
	SUBCASE("Edge_cases")
	{
		CHECK(swapp("the lord of the rings", 0) == "the lord of the rings");
		CHECK(swapp("", 11345) == "");
		CHECK(swapp("", 0) == "");
		CHECK(swapp("HELLO WORLD!", 5) == "hEllO woRld!");
		CHECK(swapp("hello world!", 56) == "HELlo wORLd!");
	}
}
