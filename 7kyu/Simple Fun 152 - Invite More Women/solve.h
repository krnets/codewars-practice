#pragma once

#include <range/v3/numeric/accumulate.hpp>

bool invite_more_women(const std::vector<int>& invited)
{
	return ranges::accumulate(invited, 0) > 0;
}
