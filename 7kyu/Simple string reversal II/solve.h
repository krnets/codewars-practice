#pragma once

/*
std::string solve(std::string s, int a, int b)
{
	b = std::min(static_cast<int>(s.length() - 1), b);

	std::reverse(s.begin() + a, s.begin() + b + 1);

	return s;
}
*/

std::string solve(std::string s, int a, int b)
{
	b = std::min(static_cast<int>(s.length()), b + 1);

	std::reverse(s.begin() + a, s.begin() + b);

	return s;
}

/*
std::string solve(std::string s, int a, int b)
{
	std::reverse(s.begin() + a, s.begin() + (b < s.length() ? b + 1 : s.length()));

	return s;
}
*/
