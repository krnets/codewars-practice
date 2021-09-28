#pragma once

/*
std::string pofi(unsigned n)
{
	if (n % 4 == 0)
		return "1";
	if ((n - 1) % 4 == 0)
		return "i";
	if ((n - 2) % 4 == 0)
		return "-1";

	return "-i";
}
*/

std::string pofi(unsigned n)
{
	std::vector<std::string> v{"1", "i", "-1", "-i"};

	return v[n % 4];
}
