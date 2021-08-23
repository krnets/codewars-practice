#pragma once
#include <cinttypes>
#include <vector>

/*
uint64_t descendingOrder(uint64_t a)
{
	auto s = std::to_string(a);
	std::vector<char> v;
	std::copy(s.begin(), s.end(), std::back_inserter(v));
	std::sort(v.rbegin(), v.rend());
	s = std::string(v.begin(), v.end());

	return std::stoul(s);
}
*/

/*
uint64_t descendingOrder(uint64_t a)
{
	std::string s = std::to_string(a);
	std::sort(s.rbegin(), s.rend());

	return std::stoul(s);
}
*/

uint64_t descendingOrder(uint64_t a)
{
	auto s = std::to_string(a);
	std::sort(s.begin(), s.end(), [](char a, char b) { return a > b; });

	return std::stoul(s);
}

