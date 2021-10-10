#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ExampleTests")
{
	SUBCASE("EncryptTests")
	{
		CHECK(encrypt("This is a test!", 0) == "This is a test!");
		CHECK(encrypt("This is a test!", 1) == "hsi  etTi sats!");
		CHECK(encrypt("This is a test!", 2) == "s eT ashi tist!");
		CHECK(encrypt("This is a test!", 3) == " Tah itse sits!");
		CHECK(encrypt("This is a test!", 4) == "This is a test!");
		CHECK(encrypt("This is a test!", -1) == "This is a test!");
		CHECK(encrypt("This kata is very interesting!", 1) == "hskt svr neetn!Ti aai eyitrsig");
	}
	SUBCASE("DecryptTests")
	{
		CHECK(decrypt("This is a test!", 0) == "This is a test!");
		CHECK(decrypt("hsi  etTi sats!", 1) == "This is a test!");
		CHECK(decrypt("s eT ashi tist!", 2) == "This is a test!");
		CHECK(decrypt(" Tah itse sits!", 3) == "This is a test!");
		CHECK(decrypt("This is a test!", 4) == "This is a test!");
		CHECK(decrypt("This is a test!", -1) == "This is a test!");
		CHECK(decrypt("hskt svr neetn!Ti aai eyitrsig", 1) == "This kata is very interesting!");
	}
	SUBCASE("EmptyTests")
	{
		CHECK(encrypt("", 0) == "");
		CHECK(encrypt("", 3) == "");
		CHECK(decrypt("", 0) == "");
		CHECK(decrypt("", 3) == "");
	}
}
