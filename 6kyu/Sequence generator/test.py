import codewars_test as test
from kata import sequence_gen
test.describe("It should work for some Fibonacci numbers")
fib = sequence_gen(0,1)
test.assert_equals(next(fib),0,"First term should be 0")
test.assert_equals(next(fib),1,"Second term should be 1")
test.assert_equals(next(fib),1,"Third term should be 1")
test.assert_equals(next(fib),2,"Fourth term should be 2")
test.assert_equals(next(fib),3,"Fifth term should be 3")
test.assert_equals(next(fib),5,"Sixth term should be 5")
test.assert_equals(next(fib),8,"Seventh term should be 8")
test.assert_equals([next(fib) for _ in range(10)],[13, 21, 34, 55, 89, 144, 233, 377, 610, 987],"The next ten terms should be [13, 21, 34, 55, 89, 144, 233, 377, 610, 987]")


test.describe("It should work for some Tribonacci numbers")
trib = sequence_gen(0,1,1)
test.assert_equals(next(trib), 0)
test.assert_equals(next(trib), 1)
test.assert_equals(next(trib), 1)
test.assert_equals(next(trib), 2)
test.assert_equals(next(trib), 4)
test.assert_equals(next(trib), 7)
test.assert_equals(next(trib), 13)
test.assert_equals(next(trib), 24)
test.assert_equals(next(trib), 44)
test.assert_equals(next(trib), 81)
test.assert_equals(next(trib), 149)
test.assert_equals(next(trib), 274)
test.assert_equals(next(trib), 504)
test.assert_equals(next(trib), 927)
test.assert_equals(next(trib), 1705)


test.describe("It should work for some Lucas numbers")
lucas = sequence_gen(2,1)
test.assert_equals([next(lucas) for _ in range(100)],[2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778, 9349, 15127, 24476, 39603, 64079, 103682, 167761, 271443, 439204, 710647, 1149851, 1860498, 3010349, 4870847, 7881196, 12752043, 20633239, 33385282, 54018521, 87403803, 141422324, 228826127, 370248451, 599074578, 969323029, 1568397607, 2537720636, 4106118243, 6643838879, 10749957122, 17393796001, 28143753123, 45537549124, 73681302247, 119218851371, 192900153618, 312119004989, 505019158607, 817138163596, 1322157322203, 2139295485799, 3461452808002, 5600748293801, 9062201101803, 14662949395604, 23725150497407, 38388099893011, 62113250390418, 100501350283429, 162614600673847, 263115950957276, 425730551631123, 688846502588399, 1114577054219522, 1803423556807921, 2918000611027443, 4721424167835364, 7639424778862807, 12360848946698171, 20000273725560978, 32361122672259149, 52361396397820127, 84722519070079276, 137083915467899403, 221806434537978679, 358890350005878082, 580696784543856761, 939587134549734843, 1520283919093591604, 2459871053643326447, 3980154972736918051, 6440026026380244498, 10420180999117162549, 16860207025497407047, 27280388024614569596, 44140595050111976643, 71420983074726546239, 115561578124838522882, 186982561199565069121, 302544139324403592003, 489526700523968661124])
test.assert_equals(next(lucas), 792070839848372253127)
test.assert_equals(next(lucas), 1281597540372340914251)
test.assert_equals(next(lucas), 2073668380220713167378)
test.assert_equals(next(lucas), 3355265920593054081629)
test.assert_equals(next(lucas), 5428934300813767249007)
test.assert_equals(next(lucas), 8784200221406821330636)
test.assert_equals(next(lucas), 14213134522220588579643)
test.assert_equals(next(lucas), 22997334743627409910279)
test.assert_equals(next(lucas), 37210469265847998489922)
test.assert_equals(next(lucas), 60207804009475408400201)
test.assert_equals(next(lucas), 97418273275323406890123)
test.assert_equals(next(lucas), 157626077284798815290324)
test.assert_equals(next(lucas), 255044350560122222180447)
test.assert_equals(next(lucas), 412670427844921037470771)
test.assert_equals(next(lucas), 667714778405043259651218)

test.describe("It should work for a pointless sequence")
pointless = sequence_gen(1)
test.assert_equals([next(pointless) for _ in range(1000)],[1] * 1000)