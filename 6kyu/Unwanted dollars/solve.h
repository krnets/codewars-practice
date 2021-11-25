#pragma once

#include <range/v3/view/filter.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::string;

double money_value(const string& s)
{
	auto fn = [](char c) { return isdigit(c) || c == '.' || c == '-'; };

	string t = s | views::filter(fn) | to<string>();

	return atof(t.c_str());
}
