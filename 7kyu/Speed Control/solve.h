#pragma once

class GpsSpeed
{
public:
	static int gps(int s, std::vector<double>& x)
	{
		int max_speed = 0;

		for (size_t i = 1; i < x.size(); ++i)
		{
			double section_distance = x[i] - x[i - 1];
			int section_speed = (3600 * section_distance) / s;

			max_speed = std::max(max_speed, section_speed);
		}

		return max_speed;
	}
};
