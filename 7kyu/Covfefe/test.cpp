#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing covfefe")
{
	SUBCASE("basic_test")
	{
		CHECK(covfefe("coverage") == "covfefe");
		CHECK(covfefe("coverage coverage") == "covfefe covfefe");
		CHECK(covfefe("nothing") == "nothing covfefe");
		CHECK(covfefe("double space ") == "double space  covfefe");
		CHECK(covfefe("covfefe") == "covfefe covfefe");
	}
}
