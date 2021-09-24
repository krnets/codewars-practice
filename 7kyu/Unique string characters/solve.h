#pragma once

/*
std::string solve(std::string a, std::string b)
{
	std::string ans;

	for (char ca : a)
		if (b.find(ca) == std::string::npos)
			ans += ca;

	for (char cb : b)
		if (a.find(cb) == std::string::npos)
			ans += cb;

	return ans;
}
*/

#include <range/v3/algorithm/remove.hpp>

/*
std::string solve(std::string a, std::string b)
{
	auto c = a;

	for (auto val : b)
		c.erase(ranges::remove(c, val), c.end());

	for (auto val : a)
		b.erase(ranges::remove(b, val), b.end());

	return c + b;
}
*/

std::string solve(std::string a, std::string b)
{
	auto c = a;

	for (auto val : b)
		a.erase(ranges::remove(a, val), a.end());

	for (auto val : c)
		b.erase(ranges::remove(b, val), b.end());

	return a + b;
}
