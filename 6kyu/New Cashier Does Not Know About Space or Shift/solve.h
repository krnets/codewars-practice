#pragma once

#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/tokenize.hpp>
#include <range/v3/view/transform.hpp>

using namespace ranges;
using std::string;
using std::regex;

string get_order(const string& order)
{
	std::vector<string> items{"Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"};
	std::map<string, int> map;
	std::ostringstream oss;
	string s = accumulate(items, string(), [](string acc, string item) { return acc + "|" + item; });

	auto capitalise = [](string&& t)
	{
		string ans(t);
		ans[0] = toupper(ans[0]);
		return ans;
	};

	auto rng = order | views::tokenize(regex(s, regex::icase)) | views::transform(capitalise);

	for (string item : rng)
		if (!map.count(item))
			map.emplace(item, 1);
		else map[item]++;

	for (string item : items)
		while (map[item]--)
			oss << item << ' ';

	string ret = oss.str();
	ret.pop_back();

	return ret;
}
