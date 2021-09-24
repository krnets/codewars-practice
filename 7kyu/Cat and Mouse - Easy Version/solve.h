#pragma once

#include <string>
#include <range/v3/algorithm/count.hpp>

std::string cat_mouse(std::string x)
{
	return ranges::count(x, '.') > 3 ? "Escaped!" : "Caught!";
}
