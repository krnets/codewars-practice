#pragma once

#include <range/v3/view/unique.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;

using std::vector;
using std::string;

/*
vector<string> uniq(const vector<string>& v)
{
	return v | views::unique | to<vector<string>>();
}
*/

/*
vector<string> uniq(const vector<string>& v)
{
	vector ret(v.begin(), v.end());
	ret.erase(std::unique(ret.begin(), ret.end()), ret.end());

	return ret;
}
*/

/*
vector<string> uniq(const vector<string>& v)
{
	vector<string> ret;
	std::unique_copy(v.begin(), v.end(), std::back_inserter(ret));

	return ret;
}
*/

vector<string> uniq(const vector<string>& v)
{
	vector<string> ret;
	string prev = string();

	for (string s : v)
	{
		if (s != prev)
			ret.push_back(s);

		prev = s;
	}
	return ret;
}
