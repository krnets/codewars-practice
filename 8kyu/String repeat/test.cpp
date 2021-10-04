#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing string repeat")
{
    SUBCASE("Sample_cases") {
    CHECK(repeat_str(3, "*") == "***");
    CHECK(repeat_str(5, "#") == "#####");
    CHECK(repeat_str(2, "ha ") == "ha ha ");
    CHECK(repeat_str(5, ">") == ">>>>>");
    CHECK(repeat_str(10, "!") == "!!!!!!!!!!");
    CHECK(repeat_str(3, "hello ") == "hello hello hello ");
    CHECK(repeat_str(3, "$") == "$$$");
    CHECK(repeat_str(5, "a") == "aaaaa");
    CHECK(repeat_str(6, "A") == "AAAAAA");
    CHECK(repeat_str(7, "aA") == "aAaAaAaAaAaAaA");
    CHECK(repeat_str(3, "") == "");
    CHECK(repeat_str(0, "null") == "");
    CHECK(repeat_str(0, "") == "");
  }
}
