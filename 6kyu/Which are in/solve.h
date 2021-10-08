#pragma once

#include <range/v3/view/filter.hpp>
#include <range/v3/algorithm/any_of.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::string;
using std::vector;

class WhichAreIn
{
public:
	static vector<string> inArray(vector<string>& array1, vector<string>& array2)
	{
		auto contains_substring = [&](auto str1)
		{
			return any_of(array2, [&](auto str2) { return str2.find(str1) != string::npos; });
		};

		auto res = array1 | views::filter(contains_substring) | to<vector<string>>();

		sort(res.begin(), res.end());

		return res;
	}
};
