#pragma once

#include <cmath>
#include <range/v3/algorithm/transform.hpp>
#include <range/v3/numeric/accumulate.hpp>

/*
bool narcissistic(int value)
{
	std::vector<int> digits;
	int n = value;

	while (n > 0)
	{
		digits.push_back(n % 10);
		n /= 10;
	}
	int exponent = digits.size();
	auto f = [&](int base) { return std::pow(base, exponent); };
	ranges::transform(digits, digits.begin(), f);

	return ranges::accumulate(digits, 0) == value;
}
*/

bool narcissistic(int value)
{
	std::string digits = std::to_string(value);
	int exp = digits.length();
	auto f = [&](int acc, char c) { return acc + pow(c - '0', exp); };

	return ranges::accumulate(digits, 0, f) == value;
}

/*
bool narcissistic(int value)
{
	int sum = 0, n = value;
	int exponent = ceil(log10(value));

	while (n > 0)
	{
		sum += pow(n % 10, exponent);
		n /= 10;
	}

	return sum == value;
}
*/

/*
bool narcissistic(int value)
{
	int exponent = ceil(log10(value));

	for (int n = value; n > 0; n /= 10)
	{
		value -= pow(n % 10, exponent);
	}

	return value == 0;
}
*/
