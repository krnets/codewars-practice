#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Alphabet war - airstrike - letters massacre")
{
	SUBCASE("AlphabetWarTest")
	{
		CHECK(alphabetWar("z") == "Right side wins!");
		CHECK(alphabetWar("****") == "Let's fight again!");
		CHECK(alphabetWar("z*dq*mw*pb*s") == "Let's fight again!");
		CHECK(alphabetWar("zdqmwpbs") == "Let's fight again!");
		CHECK(alphabetWar("zz*zzs") == "Right side wins!");
		CHECK(alphabetWar("*wwwwww*z*") == "Left side wins!");
		CHECK(alphabetWar("*ww*ww*w*wz") == "Right side wins!");
	}
	SUBCASE("Random tests")
	{
		CHECK(alphabetWar("r") == "Let's fight again!");
		CHECK(alphabetWar("l*") == "Let's fight again!");
		CHECK(alphabetWar("mgx") == "Right side wins!");
		CHECK(alphabetWar("*hq*") == "Let's fight again!");
		CHECK(alphabetWar("dfd*d") == "Right side wins!");
		CHECK(alphabetWar("*wnufg") == "Let's fight again!");
		CHECK(alphabetWar("ze*dpv*") == "Left side wins!");
		CHECK(alphabetWar("u*vtn*ab") == "Left side wins!");
		CHECK(alphabetWar("sl*p*k*d*") == "Left side wins!");
		CHECK(alphabetWar("ryymkm*x*d") == "Right side wins!");
		CHECK(alphabetWar("w*ampb***js") == "Let's fight again!");
		CHECK(alphabetWar("uelm*bz**b*d") == "Let's fight again!");
		CHECK(alphabetWar("*s*bz*mek*pqh") == "Right side wins!");
		CHECK(alphabetWar("sazoqwbtdq*did") == "Right side wins!");
		CHECK(alphabetWar("bsjh*p*sad*bzrv") == "Left side wins!");
		CHECK(alphabetWar("*hqlq*zgtwwrzbha") == "Left side wins!");
		CHECK(alphabetWar("***mihzd*bn**d*b*") == "Right side wins!");
		CHECK(alphabetWar("ybx*bzpblpgfaswpce") == "Left side wins!");
		CHECK(alphabetWar("f*ademwk*f*zopge*zx") == "Left side wins!");
		CHECK(alphabetWar("**q**dedsba*sov*au*p") == "Left side wins!");
	}
}
