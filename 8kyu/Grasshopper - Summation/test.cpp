#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing summation")
{
  SUBCASE("simple test")
    {
      CHECK(summation(1) == 1);
      CHECK(summation(8) == 36);
    }
}
