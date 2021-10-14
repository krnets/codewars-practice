#pragma once

#include <range/v3/view/tokenize.hpp>
#include <range/v3/to_container.hpp>
#include <range/v3/algorithm/find.hpp>

using namespace ranges;
using std::string;
using std::vector;

int countDeafRats(const string& town)
{
	auto split = town
		| views::tokenize(std::regex{"~O|P|O~"})
		| to<vector<string>>();

	auto piper_idx = find(split, "P") - split.begin();

	int count_left = std::count_if(split.begin(),
	                               split.begin() + piper_idx,
	                               [](string& s) { return s == "O~"; });

	int count_right = std::count_if(split.begin() + piper_idx,
	                                split.end(),
	                                [](string& s) { return s == "~O"; });
	return count_left + count_right;
}
