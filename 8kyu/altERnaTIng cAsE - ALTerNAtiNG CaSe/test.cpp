#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing altERnaTIng cAsE <=> ALTerNAtiNG CaSe")
{
	SUBCASE("ShouldPassAllTheTestsProvided")
	{
		CHECK(to_alternating_case("hello world") == "HELLO WORLD");
		CHECK(to_alternating_case("HELLO WORLD") == "hello world");
		CHECK(to_alternating_case("hello WORLD") == "HELLO world");
		CHECK(to_alternating_case("HeLLo WoRLD") == "hEllO wOrld");
		CHECK(to_alternating_case("12345") == "12345");
		CHECK(to_alternating_case("1a2b3c4d5e") == "1A2B3C4D5E");
		CHECK(to_alternating_case("String.prototype.toAlternatingCase") == "sTRING.PROTOTYPE.TOaLTERNATINGcASE");
		CHECK(to_alternating_case(to_alternating_case( "Hello World")) == "Hello World");
		CHECK(to_alternating_case("altERnaTIng cAsE") == "ALTerNAtiNG CaSe");
		CHECK(to_alternating_case("ALTerNAtiNG CaSe") == "altERnaTIng cAsE");
		CHECK(to_alternating_case("altERnaTIng cAsE <=> ALTerNAtiNG CaSe") == "ALTerNAtiNG CaSe <=> altERnaTIng cAsE");
		CHECK(to_alternating_case("ALTerNAtiNG CaSe <=> altERnaTIng cAsE") == "altERnaTIng cAsE <=> ALTerNAtiNG CaSe");
	}
}
