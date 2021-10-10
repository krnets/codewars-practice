#pragma once

class Thirteen
{
	inline static const std::vector<int> arr{1, 10, 9, 12, 3, 4};

public:
	static long long thirt(long long n)
	{
		long long sum = 0, ans = n;

		for (int i = 0; ans > 0; ++i)
		{
			sum += (ans % 10) * arr[i % arr.size()];
			ans /= 10;
		}

		return sum == n ? sum : thirt(sum);
	}
};
