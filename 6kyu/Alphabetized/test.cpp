#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Alphabetized")
{
	SUBCASE("BasicTests")
	{
		CHECK(alphabetized("") == "");
		CHECK(alphabetized(" ") == "");
		CHECK(alphabetized(" a") == "a");
		CHECK(alphabetized("a ") == "a");
		CHECK(alphabetized(" a ") == "a");
		CHECK(alphabetized("A b B a") == "AabB");
		CHECK(alphabetized(
				" a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
			)
			== "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ");
		CHECK(alphabetized("!@$%^&*()_+=-`,") == "");
		CHECK(alphabetized("The Holy Bible") == "BbeehHilloTy");
		CHECK(alphabetized("CodeWars can't Load Today") == "aaaaCcdddeLnooorstTWy");
	}
}
