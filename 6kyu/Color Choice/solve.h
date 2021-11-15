#pragma once

class ColorChoice
{
public:
	static long long checkChoose(long long m, int n)
	{
		long long c = 1;

		for (long long i = 0; i <= n; ++i)
		{
			if (c == m)
				return i;

			c = c * (n - i) / (i + 1);
		}
		return -1;
	}
};
