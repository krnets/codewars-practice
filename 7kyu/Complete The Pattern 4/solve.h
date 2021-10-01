#pragma once

/*
#include <range/v3/view.hpp>
#include <range/v3/view/join.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::string;

string pattern(int n)
{
	auto v = closed_iota_view(1, n) | to_vector;
	std::vector<string> num_strings;

	for (int i = 0; i < v.size(); ++i)
	{
		string digits;

		for (int j = i; j < v.size(); ++j)
		{
			digits += std::to_string(v[j]);
		}

		num_strings.push_back(digits);
	}

	return num_strings
		| views::join('\n')
		| to<string>();
}
*/

/*
#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view.hpp>

std::string pattern(int n)
{
	auto v = ranges::closed_iota_view(1, n) | ranges::to_vector;
	std::vector<std::string> num_strings;

	for (int i = 0; i < v.size(); ++i)
	{
		std::string digits;

		for (int j = i; j < v.size(); ++j)
		{
			digits += std::to_string(v[j]);
		}

		num_strings.push_back(digits);
	}

	auto ans = ranges::accumulate(num_strings, std::string(),
	                              [](auto x, auto y) { return x + '\n' + y; });

	return ans.substr(1);
}
*/

/*
#include <numeric>

std::string pattern(int n)
{
	if (n < 1) return std::string();

	std::vector<int> v(n);
	std::iota(v.begin(), v.end(), 1);
	std::ostringstream oss;

	for (int i = 0; i < v.size(); ++i)
	{
		std::string digits;

		for (int j = i; j < v.size(); ++j)
		{
			digits += std::to_string(v[j]);
		}
		oss << digits << '\n';
	}
	auto s = oss.str();
	s.pop_back();

	return s;
}
*/

std::string pattern(int n)
{
	if (n < 1) return std::string();

	std::ostringstream oss;

	for (int i = 1; i <= n; ++i)
	{
		for (int j = i; j <= n; ++j)
		{
			oss << j;
		}
		oss << '\n';
	}
	auto s = oss.str();
	s.pop_back();

	return s;
}
