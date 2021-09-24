#pragma once
#include <numeric>
#include <vector>

class NewAverage
{
public:
	static long long newAvg(std::vector<double>& arr, double navg)
	{
		double sum = std::accumulate(arr.begin(), arr.end(), 0.0);
		double ans = navg * (arr.size() + 1) - sum;

		if (ans < 0)
			throw std::logic_error("answer cannot be negative");

		return static_cast<long long>(std::ceil(ans));
	}
};
