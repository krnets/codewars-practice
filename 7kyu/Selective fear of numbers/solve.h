#pragma once

#include <functional>
#include <string>

/*
bool am_i_afraid(const std::string& day, int num)
{
	if (day == "Monday" && num == 12) return true;
	if (day == "Tuesday" && num > 95) return true;
	if (day == "Wednesday" && num == 34) return true;
	if (day == "Thursday" && num == 0) return true;
	if (day == "Friday" && num % 2 == 0) return true;
	if (day == "Saturday" && num == 56) return true;
	if (day == "Sunday" && abs(num) == 666) return true;

	return false;
}
*/

/*
bool am_i_afraid(const std::string& day, int num)
{
	if (day == "Monday" && num == 12
		|| day == "Tuesday" && num > 95
		|| day == "Wednesday" && num == 34
		|| day == "Thursday" && num == 0
		|| day == "Friday" && num % 2 == 0
		|| day == "Saturday" && num == 56
		|| day == "Sunday" && abs(num) == 666)
		return true;

	return false;
}
*/

/*
bool am_i_afraid(const std::string& day, int num)
{
	return day == "Monday" && num == 12
		|| day == "Tuesday" && num > 95
		|| day == "Wednesday" && num == 34
		|| day == "Thursday" && num == 0
		|| day == "Friday" && num % 2 == 0
		|| day == "Saturday" && num == 56
		|| day == "Sunday" && abs(num) == 666;
}
*/

bool am_i_afraid(const std::string& day, int num)
{
	std::map<std::string, std::function<bool(int)>> lookup{
		{"Monday", [](int x) { return x == 12; }},
		{"Tuesday", [](int x) { return x > 95; }},
		{"Wednesday", [](int x) { return x == 34; }},
		{"Thursday", [](int x) { return x == 0; }},
		{"Friday", [](int x) { return x % 2 == 0; }},
		{"Saturday", [](int x) { return x == 56; }},
		{"Sunday", [](int x) { return abs(x) == 666; }}
	};

	return lookup[day](num);
}
