import codewars_test as test
from kata import play_pass


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(play_pass("BORN IN 2015!", 1), "!4897 Oj oSpC")
        test.assert_equals(play_pass("I LOVE YOU!!!", 1), "!!!vPz fWpM J")
        test.assert_equals(
            play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2),
            "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO",
        )
        test.assert_equals(play_pass("AAABBCCY", 1), "zDdCcBbB")
        test.assert_equals(
            play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2),
            "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO",
        )
        test.assert_equals(
            play_pass(
                "TO BE HONEST WITH YOU I DON'T USE THIS TEXT TOOL TOO OFTEN BUT HEY... MAYBE YOUR NEEDS ARE DIFFERENT.",
                5,
            ),
            ".ySjWjKkNi jWf xIjJs wZtD JgDfR ...dJm yZg sJyKt tTy qTtY YcJy xNmY JxZ Y'StI N ZtD MyNb yXjStM Jg tY",
        )
        test.assert_equals(
            play_pass(
                "IN 2012 TWO CAMBRIDGE UNIVERSITY RESEARCHERS ANALYSED PASSPHRASES FROM THE AMAZON PAY SYSTEM...",
                20,
            ),
            "...gYnMsM SuJ HiTuGu yBn gIlZ MyMuLbJmMuJ XyMsFuHu mLyBwLuYmYl sNcMlYpChO YaXcLvGuW IqN 7897 hC",
        )
        test.assert_equals(
            play_pass(
                "IN 2012 TWO CAMBRIDGE UNIVERSITY RESEARCHERS ANALYSED PASSPHRASES FROM THE AMAZON PAY SYSTEM...",
                10,
            ),
            "...wOdCiC IkZ XyJkWk oRd wYbP CoCkBrZcCkZ NoCiVkXk cBoRmBkOcOb iDsCbOfSxE OqNsBlWkM YgD 7897 xS",
        )
        test.assert_equals(
            play_pass("1ONE2TWO3THREE4FOUR5FIVE6SIX7SEVEN8EIGHT9NINE", 5),
            "JsNs0yMlNj1sJaJx2cNx3jAnK4WzTk5jJwMy6tBy7jSt8",
        )
        test.assert_equals(play_pass("AZ12345678ZA", 1), "bA12345678aB")
        test.assert_equals(play_pass("!!!VPZ FWPM J", 25), "I LoVe yOu!!!")
        test.assert_equals(
            play_pass("BOY! YOU WANTED TO SEE HIM? IT'S YOUR FATHER:-)", 15),
            ")-:gTwIpU GjDn h'iX ?bXw tTh dI StIcPl jDn !NdQ",
        )
        test.assert_equals(
            play_pass(
                "FOR THIS REASON IT IS RECOMMENDED THAT PASSPHRASES NOT BE REUSED ACROSS DIFFERENT OR UNIQUE SITES AND SERVICES.",
                15,
            ),
            ".hTrXkGtH ScP HtIxH TjFxCj gD IcTgTuUxS HhDgRp sThJtG Tq iDc hThPgWeHhPe iPwI StScTbBdRtG Hx iX CdHpTg hXwI GdU",
        )
        test.assert_equals(
            play_pass("ONCE UPON A TIME YOU DRESSED SO FINE (1968)", 12),
            ")1308( qZuR Ae pQeEqDp gAk qYuF M ZaBg qOzA",
        )
        test.assert_equals(
            play_pass(
                "AH, YOU'VE GONE TO THE FINEST SCHOOL ALL RIGHT, MISS LONELY", 12
            ),
            "KxQzAx eEuY ,fTsUd xXm xAaToE FeQzUr qTf aF QzAs qH'GaK ,tM",
        )
        test.assert_equals(
            play_pass(
                "THE SPECIES, NAMED AFTER THE GREEK GOD OF THE UNDERWORLD, LIVES SOME 3,600 FEET UNDERGROUND.",
                8,
            ),
            ".LvCwZoZmLvC BmMn 993,6 mUwA AmDqT ,lTzWeZmLvC MpB Nw lWo sMmZo mPb zMbNi lMuIv ,AmQkMxA MpB",
        )
