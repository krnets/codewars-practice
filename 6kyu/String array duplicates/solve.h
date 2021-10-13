#pragma once

#include <range/v3/view/transform.hpp>
#include <range/v3/view/unique.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::string;
using std::vector;

/*
vector<string> dup(vector<string> arr)
{
	return arr
		| views::transform([](string& s) { return s | views::unique; })
		| to<vector<string>>();
}
*/

#include <range/v3/algorithm/unique.hpp>

vector<string> dup(vector<string> arr)
{
	for (string& s : arr)
		s.erase(unique(s), s.end());

	return arr;
}
