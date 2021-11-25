#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testing(string s, string expected)
{
	CHECK(hist(s) == expected);
}

TEST_CASE("testing Errors - histogram")
{
	string s, e;

	SUBCASE("hist_Test 1")
	{
		s = "tpwaemuqxdmwqbqrjbeosjnejqorxdozsxnrgpgqkeihqwybzyymqeazfkyiucesxwutgszbenzvgxibxrlvmzihcb";
		e = "u  3     ***\\rw  4     ****\\rx  6     ******\\rz  6     ******";
		testing(s, e);
	}
	SUBCASE("hist_Test 2")
	{
		s = "aaifzlnderpeurcuqjqeywdq";
		e = "u  2     **\\rw  1     *\\rz  1     *";
		testing(s, e);
	}
	SUBCASE("hist_Test 3")
	{
		testing("sjeneccyhrcpfvpujfaoaykqllteovskclebmzjeqepilxygdmzvdfmxbqdzubkzturnuqxsewrwgmdfwgdx",
		        "u  4     ****\\rw  3     ***\\rx  4     ****\\rz  4     ****");
	}
	SUBCASE("hist_Test 4")
	{
		testing("bnxyytdtqrkeaswymiwbxnuydwthweyzny", "u  1     *\\rw  4     ****\\rx  2     **\\rz  1     *");
	}
	SUBCASE("hist_Test 5")
	{
		testing("ttopvdaxgwfpzjmomkwssytktaizqtsekfmfhrabidwaugioqyyzrxbugsusxkfdevmijqyprcoxfyjqwsutoutjgozyhsoytg",
		        "u  5     *****\\rw  4     ****\\rx  4     ****\\rz  4     ****");
	}
}