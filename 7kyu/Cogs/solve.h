#pragma once

double cog_rpm(const std::vector<int>& cogs)
{
	return (cogs.size() & 1 ? 1.0 : -1.0) * cogs.front() / cogs.back();
}
