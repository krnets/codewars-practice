#pragma once

#include <string>
#include <fmt/core.h>

std::string to_time(unsigned seconds)
{
	int minutes = seconds / 60 % 60;
	int hours = seconds / 60 / 60;

	return fmt::format("{} hour(s) and {} minute(s)", hours, minutes);
}
