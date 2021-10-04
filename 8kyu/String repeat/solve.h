#pragma once

#include <string>
#include <range/v3/all.hpp>

using namespace ranges;
using std::string;

/*
string repeat_str(size_t repeat, const string& str)
{
	string result;

	for (int i = 0; i < repeat; ++i)
	{
		result += str;
	}

	return result;
}
*/

/*
string repeat_str(size_t repeat, const string& str)
{
	string result;

	for (int i = 0; i < repeat; ++i)
		result.append(str);

	return result;
}
*/

string repeat_str(size_t repeat, const string& str)
{
	return views::repeat_n(str, repeat)
		| views::join
		| to<string>();
}
