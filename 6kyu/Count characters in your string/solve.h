#pragma once

#include <map>
#include <string>
// #include <range/v3/all.hpp>

#include <range/v3/algorithm/sort.hpp>
#include <range/v3/view/group_by.hpp>
#include <range/v3/view/transform.hpp>
#include <range/v3/view/unique.hpp>
#include <range/v3/view/zip.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::string;
using std::map;

/*map<char, unsigned> countt(const string& str)
{
	if (str.empty()) return map<char, unsigned>();

	string s(str);
	sort(s);

	auto same_char = [](char x, char y) { return x == y; };
	auto group_length = [](auto&& r) { return distance(r); };

	auto r_count = s | views::group_by(same_char) | views::transform(group_length);
	auto r_unique = s | views::unique;

	return views::zip(r_unique, r_count) | to<map<char, unsigned>>();
}*/

map<char, unsigned> countt(const string& str)
{
	map<char, unsigned> m;

	for (char c : str) m[c]++;

	return m;
}
