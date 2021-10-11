#pragma once

#include <bitset>
#include <range/v3/view/tokenize.hpp>
#include <range/v3/view/transform.hpp>
#include <range/v3/view/join.hpp>
#include <range/v3/to_container.hpp>
#include <regex>

using std::string;

/*
uint32_t ip_to_int32(const string& ip)
{
	using namespace ranges;

	auto to_binary_str = [](string s)
	{
		return std::bitset<8>(std::stoi(s)).to_string();
	};

	auto rng = ip
		| views::tokenize(std::regex("\\d+"))
		| views::transform(to_binary_str)
		| to<std::vector<string>>();

	auto str = rng | views::join | to<string>();

	return std::stoul(str, 0, 2);
}
*/


uint32_t ip_to_int32(const std::string& ip)
{
	std::istringstream iss(ip);
	std::string octet;
	uint32_t ans = 0, bits = 32;

	while (std::getline(iss, octet, '.'))
	{
		bits -= 8;
		ans += (std::stoi(octet) << bits);
	}

	return ans;
}
