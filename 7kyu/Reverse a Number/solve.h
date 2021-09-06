#pragma once

#include <cmath>

/*
long long reverseNumber(long long n)
{
	long long result = 0;
	bool is_negative = n < 0;
	n = std::abs(n);

	while (n != 0)
	{
		result = 10 * result + (n % 10);
		n /= 10;
	}

	return is_negative ? -result : result;
}
*/

/*
long long reverseNumber(long long n)
{
	auto n_str = std::to_string(n);
	std::reverse(n_str.begin(), n_str.end());

	return std::stoll(n_str) * (n < 0 ? -1 : 1);
}
*/

/*
long long reverseNumber(long long n)
{
	auto n_str = std::to_string(n);
	std::ranges::reverse(n_str);

	return std::stoll(n_str) * (n < 0 ? -1 : 1);
}
*/

long long reverseNumber(long long n)
{
	long long ans = 0;

	while (n != 0)
	{
		ans = 10 * ans + n % 10;
		n /= 10;
	}

	return ans;
}
