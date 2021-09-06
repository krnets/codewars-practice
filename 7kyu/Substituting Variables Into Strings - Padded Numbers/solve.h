#pragma once

#include <iomanip>
#include <fmt/core.h>

/*
std::string solution(int n)
{
	std::string n_str = std::to_string(n);

	return "Value is " + std::string(5 - n_str.size(), '0') + n_str;
}
*/

/*
std::string solution(int n)
{
	std::ostringstream oss;

	oss << "Value is " << std::setw(5) << std::setfill('0') << n;

	return oss.str();
}
*/

/*
std::string solution(int n)
{
	std::ostringstream oss;

	oss << "Value is " << std::setfill('0') << std::setw(5) << n;

	return oss.str();
}
*/

std::string solution(int n)
{
	return fmt::format("Value is {:05d}", n);
}
