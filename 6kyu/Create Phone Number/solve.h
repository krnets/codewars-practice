#pragma once

#include <fmt/core.h>

std::string createPhoneNumber(const int arr[10])
{
	return fmt::format("({}{}{}) {}{}{}-{}{}{}{}",
	                   arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10]);
}

/*
std::string createPhoneNumber(const int arr[10])
{
	std::string ans = "(xxx) xxx-xxxx";
	int pos = 0;

	for (char& c : ans)
		if (c == 'x')
			c = '0' + arr[pos++];

	return ans;
}
*/
