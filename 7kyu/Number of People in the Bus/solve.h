#pragma once

#include <utility>
#include <vector>

unsigned int number(const std::vector<std::pair<int, int>>& busStops)
{
	unsigned passengers = 0;

	for (auto bus_stop : busStops)
	{
		passengers += bus_stop.first;
		passengers -= bus_stop.second;
	}

	return passengers;
}
