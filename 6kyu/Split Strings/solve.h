#pragma once

#include <range/v3/view/chunk.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::string;
using std::vector;

vector<string> solution(const string& s)
{
	string value(s);

	if (value.length() % 2 != 0)
		value += '_';

	return value | views::chunk(2) | to<vector<string>>();
}
