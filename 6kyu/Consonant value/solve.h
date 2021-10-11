#pragma once

#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/transform.hpp>
#include <range/v3/view/tokenize.hpp>
#include <range/v3/algorithm/max_element.hpp>

/*
int solve(const std::string& s)
{
	using namespace ranges;

	auto get_char_val = [](char c) { return c - 'a' + 1; };
	auto sum_char_val = [&](std::string s) { return accumulate(s | views::transform(get_char_val), 0); };

	auto rng = s
		| views::tokenize(std::regex{"[^aeiou]+"})
		| views::transform(sum_char_val);

	return *max_element(rng);
}
*/

int solve(const std::string& s)
{
	int highest = 0, cons_sum = 0;
	std::set vowels{'a', 'e', 'i', 'o', 'u'};

	for (char c : s)
	{
		cons_sum = vowels.count(c) ? 0 : cons_sum + c - 'a' + 1;
		highest = std::max(highest, cons_sum);
	}

	return highest;
}
