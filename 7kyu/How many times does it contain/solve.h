#pragma once

#include <range/v3/algorithm/count_if.hpp>
#include <range/v3/algorithm/count.hpp>

/*
int stringCounter(std::string inputS, char charS)
{
	return ranges::count_if(inputS, [&](char c) { return c == charS; });
}
*/


/*
int stringCounter(std::string inputS, char charS)
{
	return std::count(inputS.begin(), inputS.end(), charS);
}
*/

int stringCounter(std::string inputS, char charS)
{
	return ranges::count(inputS, charS);
}
