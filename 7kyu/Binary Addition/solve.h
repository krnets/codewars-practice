#pragma once
#include <cstdint>
#include <string>
#include <sstream>
#include <fmt/core.h>
#include <bitset>

/*
std::string add_binary(uint64_t a, uint64_t b)
{
	size_t sum = a + b;
	std::string ans;

	while (sum > 0)
	{
		ans.insert(0, std::to_string(sum % 2));
		sum /= 2;
	}

	return ans.empty() ? "0" : ans;
}
*/

/*
std::string add_binary(uint64_t a, uint64_t b)
{
	size_t sum = a + b;
	std::ostringstream oss;

	while (sum > 0)
	{
		oss << (sum & 1);
		sum >>= 1;
	}

	std::string ans = oss.str();

	return ans.empty() ? "0" : std::string(ans.rbegin(), ans.rend());
}
*/

/*
std::string add_binary(uint64_t a, uint64_t b)
{
	return fmt::format("{:b}", a + b);
}
*/

std::string add_binary(uint64_t a, uint64_t b)
{
	auto bin_str = std::bitset<64>(a + b).to_string();

	return bin_str.erase(0, std::min(bin_str.find_first_of('1'), bin_str.size() - 1));
}
