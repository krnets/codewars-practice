#pragma once

#include <bitset>
#include <string>

#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;

/*
std::string broken(const std::string& inp)
{
	return inp
		| views::transform([](char c) { return c == '0' ? '1' : '0'; })
		| to<std::string>();
}
*/

/*
std::string broken(const std::string& inp)
{
	return inp
		| views::transform([](char c) { return c ^ 1; })
		| to<std::string>();
}
*/

std::string broken(const std::string& inp)
{
	std::bitset<128> bs(inp);
	bs.flip();

	return bs.to_string().substr(bs.size() - inp.length());
}
