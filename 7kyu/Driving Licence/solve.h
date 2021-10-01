#pragma once

#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>
#include <range/v3/algorithm/find.hpp>

using namespace ranges;
using std::string;

string driver(const std::array<string, 5>& data)
{
	auto to_uppercase = [](char c) { return std::toupper(c); };

	string first_name = data[0] | views::transform(to_uppercase) | to<string>();
	string middle_name = data[1];
	string surname = data[2] | views::transform(to_uppercase) | to<string>();
	string date_of_birth = data[3];
	string gender = data[4];
	std::vector<string> months{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
	std::ostringstream ans;

	ans << surname.substr(0, 5);

	if (surname.length() < 5)
		ans << string(5 - surname.length(), '9');

	ans << date_of_birth[date_of_birth.length() - 2];

	string sub = date_of_birth.substr(3, 3);
	int m = find(months, sub) - months.begin() + 1;

	if (gender == "F") m += 50;

	if (m > 9) ans << m;
	else ans << 0 << m;

	ans << date_of_birth.substr(0, 2);
	ans << date_of_birth.back();
	ans << first_name.front();

	if (middle_name.length() == 0)
		ans << 9;
	else
		ans << middle_name.front();

	ans << 9 << "AA";

	return ans.str();
}
