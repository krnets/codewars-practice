#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

template <typename Func>
static void dotest(Func func, string s, string expected)
{
	CHECK(Opstrings3::oper(func, s) == expected);
}

TEST_CASE("testing Moves in squared strings (III)")
{
	string original, expected;

	SUBCASE("diag1Sym example 1")
	{
		original = "abcd\nefgh\nijkl\nmnop";

		//           i
		//          abcd
		//          efgh
		//          ijkl
		//          mnop

		//          aeim
		//        i bfjn
		//          cgko
		//          dhlp

		expected = "aeim\nbfjn\ncgko\ndhlp";
		dotest(Opstrings3::diag1Sym, original, expected);
	}
	SUBCASE("rot90Clock example 1")
	{
		original = "abcd\nefgh\nijkl\nmnop";

		//           i
		//          abcd
		//          efgh
		//          ijkl
		//          mnop

		//          miea
		//          njfb i
		//          okgc
		//          plhd

		expected = "miea\nnjfb\nokgc\nplhd";
		dotest(Opstrings3::rot90Clock, original, expected);
	}
	SUBCASE("selfieAndDiag1 example 1")
	{
		original = "abcd\nefgh\nijkl\nmnop";
		//          abcd|aeim
		//          efgh|bfjn
		//          ijkl|cgko 
		//          mnop|dhlp
		expected = "abcd|aeim\nefgh|bfjn\nijkl|cgko\nmnop|dhlp";
		dotest(Opstrings3::selfieAndDiag1, original, expected);
	}
	SUBCASE("rot90Clock example 2")
	{
		original = "rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb";
		expected = "Sixdvr\ndJNCGg\nmBWhca\nEYgZEv\nKDXVKc\nbORWle";
		dotest(Opstrings3::rot90Clock, original, expected);
	}
	SUBCASE("diag1Sym example 2")
	{
		original = "wuUyPC\neNHWxw\nehifmi\ntBTlFI\nvWNpdv\nIFkGjZ";
		expected = "weetvI\nuNhBWF\nUHiTNk\nyWflpG\nPxmFdj\nCwiIvZ";
		dotest(Opstrings3::diag1Sym, original, expected);
	}
	SUBCASE("selfieAndDiag1 example 2")
	{
		original = "NJVGhr\nMObsvw\ntPhCtl\nsoEnhi\nrtQRLK\nzjliWg";
		expected = "NJVGhr|NMtsrz\nMObsvw|JOPotj\ntPhCtl|VbhEQl\nsoEnhi|GsCnRi\nrtQRLK|hvthLW\nzjliWg|rwliKg";
		dotest(Opstrings3::selfieAndDiag1, original, expected);
	}
}
