#pragma once

/*
class MaxRotate
{
public:
	static long long maxRot(long long n)
	{
		auto str = std::to_string(n);
		long long ans = n;

		for (size_t i = 0; i < str.length() - 1; ++i)
		{
			str = str.substr(0, i) + str.substr(i + 1) + str.substr(i, 1);

			long long x = std::stoull(str);

			if (x > ans)
				ans = x;
		}

		return ans;
	}
};
*/

class MaxRotate
{
public:
	static long long maxRot(long long n)
	{
		auto s = std::to_string(n);

		for (int i = 0; i < s.length() - 1; ++i)
		{
			std::rotate(s.begin() + i, s.begin() + i + 1, s.end());
			long long x = std::stoll(s);
			n = std::max(n, x);
		}

		return n;
	}
};
