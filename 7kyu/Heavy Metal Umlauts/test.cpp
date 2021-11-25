#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing H��v� M�t�l �ml��ts")
{
	SUBCASE("BasicTest1")
	{
		std::string expected = "�nn��nc�ng th� M�cb��k ��r G��t�r";

		std::string actual = heavyMetalUmlauts("Announcing the Macbook Air Guitar");

		CHECK(actual == expected);
	}
	SUBCASE("BasicTest2")
	{
		std::string expected = "F�c�b��k �ntr�d�c�s n�w h��v� m�t�l r��ct��n b�tt�ns";

		std::string actual = heavyMetalUmlauts("Facebook introduces new heavy metal reaction buttons");

		CHECK_EQ(actual, expected);
	}
	SUBCASE("BasicTest3")
	{
		std::string expected = "Str�ng s�l�s �f G��gl�'s VR M�t�lh��ds�ts s�nd t�ch st�ck pr�c�s s��r�ng";

		std::string actual = heavyMetalUmlauts(
			"Strong sales of Google's VR Metalheadsets send tech stock prices soaring");

		CHECK_EQ(actual, expected);
	}
	SUBCASE("BasicTest4")
	{
		std::string expected = "V�g�n Bl�ck M�t�l Ch�f h�ts th� b�g t�m� �n �m�z�n TV";

		std::string actual = heavyMetalUmlauts("Vegan Black Metal Chef hits the big time on Amazon TV");

		CHECK_EQ(actual, expected);
	}
}
