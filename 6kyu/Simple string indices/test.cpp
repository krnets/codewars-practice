#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing SimpleStringIndices")
{
	SUBCASE("BasicTests")
	{
		CHECK(solve("((1)23(45))(aB)", 0) == 10);
		CHECK(solve("((1)23(45))(aB)", 1) == 3);
		CHECK(solve("((1)23(45))(aB)", 3) == -1);
		CHECK(solve("((1)23(45))(aB)", 6) == 9);
		CHECK(solve("((1)23(45))(aB)", 11) == 14);
		CHECK(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))", 11) == 28);
		CHECK(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))", 28) == -1);
		CHECK(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))", 0) == 29);
		CHECK(solve("(>_(va)`?(h)C(as)(x(hD)P|(fg)))", 19) == 22);
		CHECK(solve("()", 0) == 1);
	}
	SUBCASE("Long string tests")
	{
		std::string s =
			"(3hSm(tHzq)9Z(B(5GznxMBP3S(Urx(k/yhGOWKZ1IelY(VzSN+(aj7(/)kbZN04s4/17)z/Vs(9Z0iUwpiZOUoX9nKHpE)550(3i(P)+ZJ(K/(QGEoJRc-L*OYuiosv(wCWzkv)(RkHj(eFfs*cYSE)Z))gRhelhp(P0P9K(b)c0NseAXzj(1Ie0)c)D(qGVC))(r(4(tGmo7W(-6(RIR+G/V7OVgdl)TRTyXYsjdT)t2q)n(q1(Ut2)(R1J11(oZ0d((QCKaVeBgjw+)Fe5BrgUA6)8S+k)Dg)-CDk7D+WG4Sd-(RP-C(5rGAwY)b*VDiTNdG(rzip/(jJTRD8(TJlD)Qavm))Tp)))p-z2uFM((2PnN*xmNA5)I(sqWvZJZ)l*/TUw)7x3y)A*1(l3(a3HWV+j)WGZYK((5RS(azC)g4ktfhkL)hvO/tmuY))OQ(a5rl(tY9F)(((D4ac9D*j8RPjWAlE-(0)R)gRF/)bG29((dh*6sEzgCp(V(SfMs)11Yy)aaNhvwR)n)pD8k-))CT)ENZh)z)kOTa0+x)+CmtM)d)S(N+1(5yyDnAOfJ)9(Ttt(/(KKlh*(OoTG7gW)xh(6kv77TjVhje9K7gwn))(el14a+N(gQDtiPMTzFggf)U2X(t)0)BkNF1(o578(yiBKaZjshXuBRI4PK-Z)M(Ni8(X37QMnFR)(E5Z)jCbY)49p+LOeWDl2))6(-QMAk5v)j(T(w(1(gnl(CxK)5N(r)Y7xVup)s0**(9Fx-F(o+U)3oA)35xQU(LBl(B0B/**CM)BRa(EgH5*iA7tKXa6/)4)Q*v)vD1G81OTjek)3lS(FDmUZYn*fnvTsLkVwL)C86(E0i8OBf)-R(a/sYVmI0(l7FcDduw1V5rPT25Gc)oiK)rzbJBu)7Q)r)Q5RDX8Y)";
		CHECK(solve(s, 50) == -1);
	}
}
