#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing The Speed of Letters")
{
	SUBCASE("sample_test")
	{
		CHECK(speedify("CBA") == "  A");
		CHECK(speedify("ABC") == "A B C");
		CHECK(speedify("ACE") == "A  C  E");
		CHECK(speedify("AZ") == "A                         Z");
		CHECK(speedify("HELLOWORLD") == "     E H    DLL   OLO   R  W");
	}
	SUBCASE("failing_test")
	{
		CHECK(speedify(
				"UMOKVLVJGPHPUYRWHXGQQJWNUOIPPTLXBCVHDHXBPZRVMMBJXCESDDWJPSOPMZOXIZCXSFMFKFCIYLBKTTJAAAMNJQCGCTGJQZYQ"
			) ==
			"             KG JH  U  HGVPV  JRUBICNW DBLHPH  BT  C  EDDM R X  J Z CS PI FSC FB  KAAAS LKXJC C  GMTG   JQ      Q  Q      Y"
		);
	}
}
