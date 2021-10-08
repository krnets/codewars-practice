#pragma once

class Tortoise
{
public:
	static std::vector<int> race(int v1, int v2, int g)
	{
		if (v1 >= v2)
			return {-1, -1, -1};

		int seconds_in_hour = 60 * 60;
	
		g = seconds_in_hour * g / (v2 - v1);

		int hour = g / seconds_in_hour;
		int min = g % seconds_in_hour / 60;
		int sec = g % 60;

		return {hour, min, sec};
	}
};
