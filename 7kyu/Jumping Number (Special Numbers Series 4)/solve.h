#pragma once

#include <range/v3/all.hpp>
#include <numeric>

using namespace std;

/*
string jumpingNumber(int number)
{
	vector<int> v;

	for (char c : to_string(number))
		v.push_back(c - '0');

	adjacent_difference(v.begin(), v.end(), v.begin());

	if (any_of(v.begin() + 1, v.end(), [](int x) { return abs(x) != 1; }))
		return "Not!!";

	return "Jumping!!";
}
*/

string jumpingNumber(int number)
{
	vector<int> v;

	for (char c : to_string(number))
		v.push_back(c);

	adjacent_difference(v.begin(), v.end(), v.begin());

	auto s = v
		| ::ranges::views::drop(1)
		| ::ranges::views::transform([](int x) { return abs(x); })
		| ::ranges::to<set<int>>();

	return number < 10 || s.size() == 1 && s.count(1) ? "Jumping!!" : "Not!!";
}
