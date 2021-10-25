#pragma once

#include <range/v3/algorithm/sort.hpp>
#include <range/v3/view/group_by.hpp>
#include <range/v3/view/join.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::vector;

/*
vector<int> solve(const vector<int>& vec)
{
	vector clone(vec);
	sort(clone);

	auto groups = clone | views::group_by(std::equal_to()) | to<vector<vector<int>>>();

	sort(groups, [](auto& x, auto& y) { return x.size() == y.size() ? x.front() < y.front() : x.size() > y.size(); });

	return groups | views::join | to<vector<int>>();
}
*/

vector<int> solve(const vector<int>& vec)
{
	vector clone(vec);
	std::unordered_map<int, int> freq;

	for (int x : clone) freq[x]++;

	ranges::sort(clone, [&](int x, int y) { return freq[x] == freq[y] ? x < y : freq[x] > freq[y]; });

	return clone;
}
