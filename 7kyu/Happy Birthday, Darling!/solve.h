#pragma once

#include <fmt/core.h>

std::string womens_age(unsigned n)
{
	return fmt::format("{}? That's just {}, in base {}!", n, 20 + n % 2, n / 2);
}
