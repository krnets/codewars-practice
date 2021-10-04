#pragma once

#include <sstream>
#include <string>


/*
std::string reverse_words(const std::string& str)
{
	std::string result, word;
	int length = 0;

	for (int i = str.size() - 1; i >= 0; --i)
	{
		if (str[i] == ' ')
		{
			word = str.substr(i + 1, length);
			result.append(word);
			result.append(" ");
			length = 0;
		}
		else length++;
	}
	word = str.substr(0, length);
	result.append(word);

	return result;
}
*/

/*
std::string reverse_words(const std::string& str)
{
	std::stringstream ss(str);
	std::string result, word;

	while (ss >> word) result.insert(0, word + ' ');

	result.pop_back();

	return result;
}
*/

// #include <range/v3/all.hpp>

#include <range/v3/algorithm/reverse.hpp>
#include <range/v3/view/concat.hpp>
#include <range/v3/view/group_by.hpp>
#include <range/v3/view/partial_sum.hpp>
#include <range/v3/view/single.hpp>
#include <range/v3/view/slice.hpp>
#include <range/v3/view/sliding.hpp>
#include <range/v3/view/transform.hpp>

using std::string;

string reverse_words(const string& str)
{
	using namespace ranges;

	string ans(str);
	reverse(ans);

	auto groups = ans | views::group_by([](auto c1, auto c2) { return c1 != ' ' && c2 != ' '; });

	auto bounds = views::concat(views::single(0), groups | views::transform([](auto g) { return size(g); }))
		| views::partial_sum | views::sliding(2);

	for (auto window : bounds)
		reverse(views::slice(ans, *begin(window), *++begin(window)));

	return ans;
}
