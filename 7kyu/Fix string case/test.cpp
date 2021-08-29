#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Solve")
{
	SUBCASE("BasicTests")
	{
		CHECK(solve("code") == "code");
		CHECK(solve("CODe") == "CODE");
		CHECK(solve("COde") == "code");
		CHECK(solve("Code") == "code");
		CHECK(solve("") == "");
		CHECK(solve("OyCLEygQRawgLt") == "oycleygqrawglt");
		CHECK(solve("tgQcgKZVP") == "TGQCGKZVP");
	}
}
