#pragma once
#include <utility>

	class DivSeven
	{
	public:
		static std::pair<long long, long long> seven(long long m)
		{
			long long count_steps = 0, x, y;

			while (m > 99)
			{
				x = m % 10;
				y = 2 * x;
				m = m / 10 - y;
				count_steps++;
			}

			return std::make_pair(m, count_steps);
		}
	};
