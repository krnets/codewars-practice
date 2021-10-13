#pragma once
#define M_PI 3.14159265358979323846  /* pi */
#include <fmt/core.h>

using std::string;

class PiApprox
{
public:
	static string iterPi(double epsilon)
	{
		int count = 1;
		double res = 1, inc = 1, cmp = 1;
		bool plus = false;

		while (cmp > epsilon)
		{
			inc += 2;

			if (plus)
				res += 1 / inc;
			else res -= 1 / inc;

			cmp = std::abs(M_PI - res * 4);
			plus = !plus;
			++count;
		}

		return fmt::format("[{}, {:.{}f}]", count, res * 4, 10);
	}
};
