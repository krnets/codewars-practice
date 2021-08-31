#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(std::string ans, std::string sol)
{
	CHECK(ans == sol);
}

template <typename Func>
static void dotest(Func func, std::string s, std::string expected)
{
	testequal(Opstrings::oper(func, s), expected);
}

TEST_CASE("testing Mirror")
{
	SUBCASE("vertMirror_Tests")
	{
		std::string s = "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu";
		std::string sol = "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw";
		dotest(Opstrings::vertMirror, s, sol);

		s = "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx";
		sol = "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP";
		dotest(Opstrings::vertMirror, s, sol);

		s = "cuQW\nxOuD\nfZwp\neqFx";
		sol = "WQuc\nDuOx\npwZf\nxFqe";
		dotest(Opstrings::vertMirror, s, sol);

		s = "CDGIdolo\nUstXfrIg\ntMqjvxWL\nBEyuCnAm\nxsxaEERa\nxZsvOiZS\nLutlBRXE\ntxshhbqE";
		sol = "olodIGDC\ngIrfXtsU\nLWxvjqMt\nmAnCuyEB\naREEaxsx\nSZiOvsZx\nEXRBltuL\nEqbhhsxt";
		dotest(Opstrings::vertMirror, s, sol);
	}

	SUBCASE("horMirror_Tests")
	{
		std::string s = "lVHt\nJVhv\nCSbg\nyeCt";
		std::string sol = "yeCt\nCSbg\nJVhv\nlVHt";
		dotest(Opstrings::horMirror, s, sol);

		s = "njMK\ndbrZ\nLPKo\ncEYz";
		sol = "cEYz\nLPKo\ndbrZ\nnjMK";
		dotest(Opstrings::horMirror, s, sol);

		s = "QMxo\ntmFe\nWLUG\nowoq";
		sol = "owoq\nWLUG\ntmFe\nQMxo";
		dotest(Opstrings::horMirror, s, sol);

		s = "FYvi\ndZQn\nuGef\nQoSy";
		sol = "QoSy\nuGef\ndZQn\nFYvi";
		dotest(Opstrings::horMirror, s, sol);
	}
}
