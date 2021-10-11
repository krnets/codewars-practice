#pragma once

#include <range/v3/view/reverse.hpp>
#include <range/v3/view/chunk.hpp>
#include <range/v3/view/join.hpp>
#include <range/v3/to_container.hpp>
#include <range/v3/algorithm/reverse.hpp>

using namespace ranges;
using std::string;

string group_by_commas(int n)
{
	string s = std::to_string(n);
	auto formatted = s | views::reverse | views::chunk(3) | views::join(',') | to<string>();
	reverse(formatted);

	return formatted;
}

/*
string group_by_commas(int n)
{
	string ans = std::to_string(n);

	for (int i = ans.length(); i > 3;)
	{
		i -= 3;
		ans.insert(i, ",");
	}

	return ans;
}
*/


/*
#include <fmt/format.h>

std::string group_by_commas(int n)
{
	return fmt::format(std::locale("en_US.UTF-8"), "{:L}", n);
}
*/

/*
#include <fmt/format.h>

struct separate_thousands : std::numpunct<char>
{
	char_type do_thousands_sep() const override { return ','; }
	string_type do_grouping() const override { return "\3"; }
};

std::string group_by_commas(int n)
{
	auto thousands = std::make_unique<separate_thousands>();
	std::stringstream ss;

	return fmt::format(std::locale(ss.getloc(), thousands.release()), "{:L}", n);
}
*/
