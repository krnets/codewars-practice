#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing positive sum function")
{
  CHECK( positive_sum(std::vector <int> {1,2,3,4,5}) == 15);
}
